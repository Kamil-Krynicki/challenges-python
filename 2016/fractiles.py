def discover_gold(K, C, S):
    if S < K / C:
        return impossible()
    else:
        return ' '.join(map(str, buckets(K, C)))


def impossible():
    return 'IMPOSSIBLE'


def buckets(K, C):
    if C > K:
        C = K

    seed = sum(i * K ** (C - i - 1) for i in range(C))
    step = sum(K ** i for i in range(C))

    result = [seed + i * step + 1 for i in range(0, K - C + 1, C)]

    if not K % C == 0:
        result.append(seed + (K - C) * step + 1)

    return result


with open('input/D-large-practice.in') as f:
    f.__next__()

    i = 1
    for line in f:
        K, C, S = map(int, line.split(' '))
        print('Case #{}: {}'.format(i, discover_gold(K, C, S)))
        i += 1
