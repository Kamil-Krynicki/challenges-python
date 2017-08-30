def last_before_sleep(N):
    if N == 0:
        return 'INSOMNIA'

    digits = set()
    current = 0

    while len(digits) < 10:
        current += N
        digits |= set(str(current))

    return current


with open('input/A-large-practice.in') as f:
    f.__next__()

    i = 1
    for N in f:
        print('Case #{}: {}'.format(i, last_before_sleep(int(N))))
        i += 1
