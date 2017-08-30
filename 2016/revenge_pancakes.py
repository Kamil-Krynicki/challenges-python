negate = lambda x: -x


def flip(stack, top):
    return list(map(negate, stack[:top]))[::-1] + stack[top:]


stack = [-1, -1, 1, -1]


def fix_pancake_stack(stack):
    history = [stack]

    i = len(stack)
    while i >= 0:
        j = 0
        if history[-1][i - 1] < 0:
            while history[-1][j] > 0:
                j += 1

            if j > 0:
                history.append(flip(history[-1], j))

            history.append(flip(history[-1], i))

        i -= 1 + j

    return history


with open('input/B-large-practice.in') as f:
    f.__next__()

    i = 1
    for N in f:
        stack = list(map(lambda x: 1 if x == '+' else -1, list(N.strip())))
        print('Case #{}: {}'.format(i, len(fix_pancake_stack(stack)) - 1))
        i += 1
