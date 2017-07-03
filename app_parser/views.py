from django.http import JsonResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.generic.base import TemplateView

from app_parser import utils
from app_parser.forms import PlaceForm, UploadFileForm
from app_parser.models import Region, Place


class HomePageView(TemplateView):
    template_name = 'app_parser/info.html'
    form = PlaceForm()

    def get_context_data(self, **kwargs):
        regions = Region.objects.all()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['regions'] = regions
        context['form'] = self.form
        context['title'] = 'Test task d-cod.com'
        return context


def change_region(request):
    id = 0
    title = ''
    inj = True

    name = str(request.GET.get('name', None))
    regions = Region.objects.all()

    for region in regions:
        if name == region.region_name:
            title = region.region_name
            id = region.id
            inj = False
            break

    if not inj:
        places = Place.objects.filter(region__region_name=name).order_by('value')
    else:
        r = Region.objects.order_by('id')[0]
        places = Place.objects.filter(region=r.id)
        title = r.region_name
        id = r.id

    lst = []
    for record in places:
        d = {'city': record.city, 'value': record.value}
        lst.append(d)
    data = {
        'id': id,
        'title': title,
        'lst': lst,
    }
    return JsonResponse(data)


def update_info(records):
    regions = Region.objects.all()
    places = Place.objects.all()
    changed = {}

    for region_name, records in records.items():
        not_exists_region_name = True

        for region in regions:
            if region_name == region.region_name:
                not_exists_region_name = False
                break
        if not_exists_region_name:
            region_obj = Region(region_name=region_name)
            region_obj.save()
        else:
            region_obj = Region.objects.get(region_name=region_name)

        for record in records:
            not_exists_city = True

            for place in places:
                if record['city'] == place.city:
                    not_exists_city = False
                    break
            if not_exists_city:
                Place(region=region_obj, city=record['city'], value=record['value']).save()
                d = {'city': record['city'], 'value': record['value']}
                if region_obj.region_name in changed:
                    changed[region_obj.region_name].append(d)
                else:
                    changed[region_obj.region_name] = [d]
    return changed


def import_file(request):
    context = {}
    if request.method == 'POST':
        context.update(csrf(request))
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csvfile = request.FILES['file'].read()
            csvfile = csvfile.decode('utf-8')
            data = csvfile.split('\r\n')

            records = utils.get_data_info(data)
            regions = Region.objects.all()
            places = Place.objects.all()

            if regions or places:
                changed = update_info(records)
                if changed:
                    msg = 'Was new records'
                else:
                    msg = 'Do not was update'
                context = {
                    'msg': msg,
                    'title': 'update data',
                    'records': changed,
                }
                return render(request, 'app_parser/change_info.html', context)
            else:
                all = records
                for region_name, records in records.items():
                    r = Region(region_name=region_name)
                    r.save()
                    for record in records:
                        Place(region=r, city=record['city'], value=record['value']).save()
                context = {
                    'title': 'import data',
                    'msg': 'Data import was successful',
                    'records': all,
                }
                return render(request, 'app_parser/change_info.html', context)
    else:
        form = UploadFileForm()

    context = {
        'title': 'Upload',
        'form': form
    }
    return render(request, 'app_parser/import.html', context)
