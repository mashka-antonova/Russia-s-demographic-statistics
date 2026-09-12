import csv_reader
import data_service
import console
import statistics_service
import csv
import os

MAX_FILE_SIZE = 100 * 1024 * 1024

filepath = console.choose_file()

if not filepath:
    print('Файл не выбран')
    exit()

try:
    if os.path.getsize(filepath) > MAX_FILE_SIZE:
        print('Файл слишком большой. Максимальный размер — 100 МБ.')
        exit()
    
    data = csv_reader.read_csv(filepath)
    data_service.validate_data(data)
except FileNotFoundError:
    print('Файл не найден.')
    exit()
except PermissionError:
    print('Нет прав для чтения файла.')
    exit()
except csv.Error:
    print('Файл не является корректным CSV или имеет повреждённую структуру.')
    exit()
except UnicodeDecodeError:
    print('Не удалось прочитать файл: неподдерживаемая кодировка.')
    exit()
except ValueError as error:
    print(error)
    exit()
except OSError as error:
    print('Другая ошибка файловой системы:', error)
    exit()

regions = data_service.get_regions(data)
columns = data_service.get_columns(data)

selected_region = console.choose_region(regions)
filtered_data = data_service.filter_by_region(data, selected_region)
console.print_table(filtered_data)

while True:
    selected_column = console.choose_column(columns)
    try:
        column_values = data_service.get_column_values(filtered_data, selected_column)
        break
    except ValueError as error:
        print(error)


statistics_result = statistics_service.calculate_statistics(column_values)
console.print_statistics(statistics_result)





