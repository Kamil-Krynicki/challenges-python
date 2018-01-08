from numpy import full

import itertools


def max_noise_map(R, C):
    result = full((R, C), 4)

    for x in range(R):
        for y in [0, C - 1]:
            result[x][y] -= 1

    for x in range(C):
        for y in [0, R - 1]:
            result[y][x] -= 1

    return result


def min_unhappiness(R, C, N):
    def remove_noise_cause(unhappiness_map, row, column):
        unhappiness_map[row][column] = 0

        decrease(row - 1, column, unhappiness_map)
        decrease(row + 1, column, unhappiness_map)
        decrease(row, column - 1, unhappiness_map)
        decrease(row, column + 1, unhappiness_map)

    def decrease(row, column, unhappiness_map):
        if row < R and row > 0 and column < C and column > 0:
            unhappiness_map[row][column] -= 1 if unhappiness_map[row][column] > 0 else 0

    def min_noise(R, C, N, noise_sequence):
        left = R * C - N
        current_noise = 2 * R * C - R - C

        if (left <= 0):
            return current_noise

        noise_map = max_noise_map(R, C)
        for noise in noise_sequence:
            for (row, column) in itertools.product(range(R), range(C)):
                local_noise = noise_map[row][column]
                if local_noise >= noise:
                    current_noise -= local_noise
                    remove_noise_cause(noise_map, row, column)
                    left -= 1
                    if left == 0:
                        return current_noise
        return 0

    if R * C > 2 * N:
        return 0
    else:
        return min(min_noise(R, C, N, [4, 3, 2, 1]), min_noise(R, C, N, [3, 4, 2, 1]))


with open('input/B-large-practice.in') as f:
    lines = f.read().split('\n')
    for i in range(int(lines[0])):
        R, C, N = list(map(int, lines[i + 1].split(' ')))
        print('Case #{}: {}'.format(i + 1, min_unhappiness(R, C, N)))
