import functools

cycle_size = 4


def can_split(X, L, x):
    i_index = starts_with(x * cycle_size, 'i')

    if i_index < 0:
        return False

    k_index = ends_with(x * cycle_size, 'k')

    if k_index < 0:
        return False

    if i_index + k_index >= L * X:
        return False

    return reduce([reduce(x)] * int(L % cycle_size)) == '-1'  # this is a shocking line of code


def reduce(operands):
    return functools.reduce(lambda a, b: mul_sign(a, b), operands, '1')


def sign(a, b):
    return '-' if (a[0] == '-') ^ (b[0] == '-') else ''


def starts_with(values, expected):
    return compacts_to(values, expected, lambda acc, value: mul_sign(acc, value), 0, len(values))


def ends_with(values, expected):
    return compacts_to(values[::-1], expected, lambda acc, value: mul_sign(value, acc), 0, len(values))


def compacts_to(values, expected, reduction, at, max_len):
    i = at
    acc = '1'
    while i < max_len:
        acc = reduction(acc, values[i])
        i += 1

        if acc == expected:
            return i

    return -1


def mul_sign(a, b):
    result = mul(a[-1], b[-1])
    return sign(sign(a, b) + '1', result) + result[-1]


table = {'i': {'j': 'k', 'k': '-j'},
         'j': {'i': '-k', 'k': 'i'},
         'k': {'i': 'j', 'j': '-i'}}


def mul(a, b):
    if a == '1':
        return b
    if b == '1':
        return a
    if a == b:
        return '-1'

    return table[a][b]


with open('input/C-large-practice.in') as f:
    lines = f.read().split('\n')
    for i in range(int(lines[0])):
        X, L = lines[2 * i + 1].split(' ')
        x = lines[2 * i + 2]
        print('Case #{}: {}'.format(i + 1, 'YES' if can_split(int(X), int(L), x) else 'NO'))
