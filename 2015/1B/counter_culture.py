steps = [0]

import math

for i in range(1, 20):
    steps.append(steps[-1] + 10 ** math.floor(i / 2) + 10 ** math.ceil(i / 2) - 1)


def isPowerOfTen(num):
    return int(str(num)[::-1]) == 1


def min_steps(end):
    s_end = str(end)
    l_end = len(s_end)

    if (l_end == 1):
        return end

    result = steps[l_end - 1]

    upper_half = int(s_end[:math.floor(l_end / 2)][::-1])
    lower_half = int(s_end[-math.ceil(l_end / 2):])

    if lower_half == 0:
        return min_steps(end - 1) + 1

    result += lower_half

    if not isPowerOfTen(upper_half):
        result += upper_half

    return result


with open('input/A-large-practice.in') as f:
    lines = f.read().split('\n')
    for i in range(int(lines[0])):
        print('Case #{}: {}'.format(i + 1, min_steps(int(lines[i + 1]))))
