def wait(total, rate):
    return total / rate


def find_min(rate, C, F, X):
    result = wait(X, rate)
    time = 0
    while time < result:
        time += wait(C, rate)
        rate += F
        result = min(result, time + wait(X, rate))

    return result


with open('input/B-large-practice.in') as f:
    T = int(next(f))
    for t in range(1, T + 1):
        C, F, X = map(float, next(f).split(' '))

        print('Case #{}: {:.7f}'.format(t, round(find_min(2, C, F, X), 7)))
