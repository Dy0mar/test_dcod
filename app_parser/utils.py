from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError(u'extension is not .csv')


def get_data_info(data):
    all_list = []
    records = {}
    regions = []
    i = True

    for line in data:
        if i or line.strip() == '':
            i = False
            continue
        all_list.append(line.strip())
        tmp_list = line.split(',')
        region = tmp_list[0].strip()

        if region not in regions:
            regions.append(region)

    for region in regions:
        records[region] = []
        for line in all_list:
            tmp_list = line.split(',')
            current_region = tmp_list[0].strip()

            if region == current_region:
                city = tmp_list[1]
                value = tmp_list[2]
                d = {'city': city, 'value': int(value)}
                records[region].append(d)

    return records
