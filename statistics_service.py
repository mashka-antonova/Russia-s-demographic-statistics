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

def calculate_variance(values, mean):
    sum_of_squares = 0
    for value in values:
        sum_of_squares += (value - mean) ** 2
    return sum_of_squares / len(values) - 1

def detect_outliers(values, q1, q3):
    iqr = q3 - q1
    lower_bound = q1 - iqr * 1.5
    upper_bound = q3 + iqr * 1.5

    outliers = []
    for value in values:
        if value > upper_bound or value < lower_bound:
            outliers.append(value)

    return outliers

def calculate_statistics(values):
    if not values:
        raise ValueError('Список пустой. Расчет метрик невозможен')

    minimum = calculate_min(values)
    maximum = calculate_max(values)
    median = calculate_median(values)
    mean = calculate_mean(values)
    percentiles = calculate_percentiles(values)

    range_value = maximum - minimum
    variance = calculate_variance(values, mean)
    standard_deviation = variance ** 0.5
    outliers = detect_outliers(values, percentiles[25], percentiles[75])

    statistics = {'minimum' : minimum, 'maximum' : maximum, 'median' : median, 'mean' : mean,
                  'percentiles' : percentiles, 'range' : range_value, 'variance' : variance,
                  'standard_deviation' : standard_deviation, 'outliers_count' : len(outliers)}
    return statistics
