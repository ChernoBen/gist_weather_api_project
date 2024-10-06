from collections import defaultdict


def normalize_temperatures(data):
    temp_sum = defaultdict(int)
    temp_count = defaultdict(int)

    for item in data:
        dt = item['dt']
        temp = int(item['temp'])
        temp_sum[dt] += temp
        temp_count[dt] += 1

    result = [
        {'dt': dt, 'average_temp': int(temp_sum[dt] / temp_count[dt])}
        for dt in temp_sum
    ]

    return result
