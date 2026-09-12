from tkinter import filedialog

def choose_file():
    print("Выберите файл:")
    filepath = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")]
    )
    return filepath

def choose_region(regions):
    print('Все регионы:')
    for index, region in enumerate(regions):
        print(index, '-', region)

    while True:
        try:
            region_id = int(input('Введите ID региона: '))
            if 0 <= region_id < len(regions):
                selected_region = regions[region_id]
                break
            else:
                print('Данного ID не существует, попробуйте снова')

        except ValueError:
            print('Введите число - ID региона, попробуйте снова')

    return selected_region


def choose_column(columns):
    print('Все колонки:')
    for index, column in enumerate(columns):
        print(index, '-', column)

    while True:
        try:
            column_id = int(input('Введите колонку для вычисления метрик: '))
            if 0 <= column_id < len(columns):
                selected_column = columns[column_id]
                break
            else:
                print('Данного ID не существует, попробуйте снова')
        except ValueError:
            print('Введите число - ID колонки, попробуйте снова')

    return selected_column

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
    print('Медиана:', statistics_result['median'])
    print()
    for percentile, value in statistics_result['percentiles'].items():
        print(f'Перцентиль {percentile}% : {round(value, 2)}')
        print('-----------------------')