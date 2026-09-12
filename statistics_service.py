def calculate_min(values):
    minimum = values[0]
    for value in values:
        if value < minimum:
            minimum = value
    return minimum

def calculate_max(values):
    maximum = values[0]
    for value in values:
        if value > maximum:
            maximum = value
    return maximum

def calculate_mean(values):
    sum_all = 0
    for value in values:
        sum_all += value
    return sum_all / len(values)

def calculate_median(values):
    sorted_values = sorted(values)
    length = len(sorted_values)
    if length % 2:
        median = sorted_values[length // 2]
    else:
        median = calculate_mean([sorted_values[length // 2], sorted_values[length // 2 - 1]])
    return median

def calculate_statistics(values):
    if not values:
        raise ValueError('Список пустой. Расчет метрик невозможен')

    minimum = calculate_min(values)
    maximum = calculate_max(values)
    median = calculate_median(values)
    mean = calculate_mean(values)
    percentiles = calculate_percentiles(values)
    statistics = {'minimum' : minimum, 'maximum' : maximum, 'median' : median, 'mean' : mean,
                  'percentiles' : percentiles}
    return statistics

def calculate_percentiles(values):
    percentiles = {}
    sorted_values = sorted(values)
    n = len(sorted_values)
    for percentile  in range(0, 101, 5):
        h = (n - 1) * percentile / 100
        i = int(h)
        d = h - i
        if d == 0:
            percentiles[percentile] = sorted_values[i]
        else:
            percentiles[percentile] = sorted_values[i] + d * (sorted_values[i + 1] - sorted_values[i])
    return percentiles