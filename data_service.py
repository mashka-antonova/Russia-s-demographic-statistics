def validate_data(data):
    if not data:
        raise ValueError('CSV-файл не содержит данных.')

    if 'region' not in data[0]:
        raise ValueError('В CSV отсутствует обязательная колонка region.')

def filter_by_region(data, region):
    filtered_data = []
    for row in data:
        if row['region'] == region:
            filtered_data.append(row)
    return filtered_data

def get_regions(data):
    regions = set()
    for row in data:
        regions.add(row['region'])
    return sorted(regions)

def get_columns(data):
    columns = []
    for column in data[0].keys():
        if column != 'region':
            columns.append(column)
    return columns

def get_column_values(data, column):
    column_values = []
    for index, row in enumerate(data, start=1):
        value = row[column]
        if value is None or value == '':
            raise ValueError(
                f'В столбце {column}, строка {index} отсутствует значение'
            )
        try:
            column_values.append(float(value))
        except ValueError:
            raise ValueError(
                f'Значение в столбце {column}, строка {index} - не число'
            )
    return column_values