def prv_tidy(value):
    s = list(map(int, value))
    for i in reversed(range(1, len(s))):
        if s[i] < s[i-1]:
            s[i-1] -= 1
            s[i:] = [9]*(len(s) - i)

    return int(''.join(str(x) for x in s))

with open('input/B-large-practice.in') as f:
    print(f.__next__())

    i = 1
    for line in f:
        print('Case #{}: {}'.format(i, prv_tidy(line.strip())))
        i += 1
