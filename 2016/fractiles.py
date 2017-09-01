def discover_gold(K, C, S):
    if C == 1:
        if S < K:
            return impossible()
        else:
            return ' '.join(map(str, every_bucket(K)))
    else:
        if S < K / 2:
            return impossible()
        else:
            return ' '.join(map(str, every_second_bucket(C, K)))


def impossible():
    return 'IMPOSSIBLE'


def every_bucket(K):
    return [bucket for bucket in range(1, K + 1)]


def every_second_bucket(C, K):
    bucket_size = K ** (C - 1)
    result = [(bucket - 1) * bucket_size + 1 + bucket for bucket in range(1, K, 2)]
    if K % 2 == 1:
        result.append(bucket_size * K)
    return result


K = 2
C = 3
S = 3

with open('input/D-large-practice.in') as f:
    f.__next__()

    i = 1
    for line in f:
        K, C, S = map(int, line.split(' '))
        print('Case #{}: {}'.format(i, discover_gold(K, C, S)))
        i += 1
