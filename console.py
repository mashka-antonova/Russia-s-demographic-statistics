from tkinter import filedialog

def choose_file():
    print("Выберите файл:")
    filepath = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")]
    )
    return filepath

def choose_item(items, list_text, invitation_text):
    print(list_text)
    for index, item in enumerate(items):
        print(index, '-', item)

    while True:
        try:
            item_id = int(input(invitation_text))
            if 0 <= item_id < len(items):
                selected_item = items[item_id]
                return selected_item
            else:
                print('Данного ID не существует, попробуйте снова')
        except ValueError:
            print('ID - это целое число, попробуйте снова')


def choose_region(regions):
    return choose_item(regions,
                       'Все регионы:',
                       'Введите ID региона: ')

def choose_column(columns):
    return choose_item(columns,
                       'Все колонки:',
                       'Введите колонку для вычисления метрик: ')

def print_table(data):
    column_width = get_column_widths(data)
    for column, width in column_width.items():
        print(f' {column:^{width}} ', end='|')
    print()
    for row in data:
        for column, width in column_width.items():
            print(f' {row[column]:^{width}} ', end='|')
        print()

def get_column_widths(data):
    column_widths = {}
    for column in data[0].keys():
        max_len = len(column)
        for row in data:
            if len(str(row[column])) > max_len:
                max_len = len(str(row[column]))
        column_widths[column] = max_len
    return column_widths


def print_statistics(statistics_result):
    print()
    print('Минимум:', statistics_result['minimum'])
    print('Максимум:', statistics_result['maximum'])
    print('Среднее:', round(statistics_result['mean'], 2))
    print('Медиана:', round(statistics_result['median'], 2))
    print()
    for percentile, value in statistics_result['percentiles'].items():
        print(f'Перцентиль {percentile}% : {round(value, 2)}')
        print('-----------------------')
    print('Меры разброса:')
    print('Размах:', round(statistics_result['range'], 2))
    print('Дисперсия:', round(statistics_result['variance'], 2))
    print('Стандартное отклонение:', round(statistics_result['standard_deviation'], 2))
    print('Количество выбросов:', statistics_result['outliers_count'])

def print_missing_values_info(missing_count):
    if missing_count > 0:
        print('Количество строк с пустыми значениями: ', missing_count,
            '\nСтроки с пустыми значениями не участвуют в расчете')

def ask_action():
    print('\nЧто сделать дальше?')
    print('1 - выбрать другую колонку')
    print('2 - выбрать другой регион')
    print('0 - выйти')
    while True:
        try:
            action = int(input('Введите номер действия: '))
            if action in (0, 1, 2):
                return action
            else:
                print('Такого действия нет, попробуйте снова')
        except ValueError:
            print('Номер действия - целое число, попробуйте снова')