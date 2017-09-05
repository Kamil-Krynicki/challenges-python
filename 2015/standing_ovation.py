def people_needed(max_shyness, public):
    up = 0
    needed = 0
    for i in range(max_shyness):
        up += public[i]
        if up + needed <= i:
            needed += 1

    return needed

with open('input/A-large-practice.in') as f:
    f.__next__()

    i = 1
    for N in f:
        S_max, S = N.strip().split(' ')
        print('Case #{}: {}'.format(i, people_needed(int(S_max), list(map(int, S)))))
        i += 1