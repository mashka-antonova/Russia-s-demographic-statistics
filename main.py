import csv
import os

import console
import csv_reader
import data_service
import statistics_service

MAX_FILE_SIZE = 100 * 1024 * 1024


def load_data(filepath):
    if os.path.getsize(filepath) > MAX_FILE_SIZE:
        raise ValueError('Файл слишком большой. Максимальный размер - 100 МБ.')

    data = csv_reader.read_csv(filepath)
    data_service.validate_data(data)

    return data


def main():
    filepath = console.choose_file()

    if not filepath:
        print('Файл не выбран')
        return

    try:
        data = load_data(filepath)

    except FileNotFoundError:
        print('Файл не найден.')
        return

    except PermissionError:
        print('Нет прав для чтения файла.')
        return

    except csv.Error:
        print('Файл не является корректным CSV или имеет повреждённую структуру. ')
        return

    except UnicodeDecodeError:
        print('Не удалось прочитать файл: неподдерживаемая кодировка.')
        return

    except ValueError as error:
        print(error)
        return

    except OSError as error:
        print('Другая ошибка файловой системы:', error)
        return

    regions = data_service.get_regions(data)
    columns = data_service.get_columns(data)
    while True:
        selected_region = console.choose_region(regions)
        filtered_data = data_service.filter_by_region(data, selected_region)
        console.print_table(filtered_data)

        while True:
            selected_column = console.choose_column(columns)

            try:
                column_values, missing_count = data_service.get_column_values(filtered_data, selected_column)
                console.print_missing_values_info(missing_count)

            except ValueError as error:
                print(error)
                continue

            try:
                statistics_result = statistics_service.calculate_statistics(column_values)
            except ValueError as error:
                print(error)
                continue
            console.print_statistics(statistics_result)

            action = console.ask_action()

            if action == 0:
                return
            elif action == 1:
                continue
            elif action == 2:
                break


if __name__ == '__main__':
    main()




