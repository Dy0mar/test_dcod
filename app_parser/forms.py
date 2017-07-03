from django.forms import forms, Select, ModelForm, ModelChoiceField

from app_parser.models import Region
from .utils import validate_file_extension


class PlaceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.fields['region_name'] = ModelChoiceField(
            queryset=Region.objects.all().order_by('region_name'),
            widget=Select(),
            initial='',
            required=True,
        )

    class Meta:
        model = Region
        fields = ('region_name',)


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Import csv ', label_suffix='', validators=[validate_file_extension])
