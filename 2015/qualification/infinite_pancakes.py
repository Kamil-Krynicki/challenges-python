def measure_redistribution_time(max, pancake_distribution):
    return sum(map(lambda pancake_stack: (pancake_stack - 1) // max, pancake_distribution))


def min_consumption_time(pancake_distribution):
    min_time = max(pancake_distribution)
    for consumption_time in range(2, max(pancake_distribution)):
        redistribution_time = measure_redistribution_time(consumption_time, pancake_distribution)
        min_time = min(min_time, consumption_time + redistribution_time)
    return min_time

with open('input/B-large-practice.in') as f:
    lines = f.read().split('\n')
    for i in range(int(lines[0])):
        distribution = lines[2 * i + 2].split(' ')
        print('Case #{}: {}'.format(i + 1, min_consumption_time(list(map(int, distribution)))))
