def flip(input, x, y):
    result = input[:]
    result[x:y] = [not x for x in input[x:y]]
    return result

def do_find_recursive(input, K):
    flips = [(x - K, x) for x in range(K, len(input) + 1)]
    memo = {tuple(True for x in input):0}

    def min_flips(input):
        key = tuple(input)

        if key not in memo:
            result = 2 ** 32
            memo[key] = result

            for x, y in flips:
                result = min(result, min_flips(flip(input, x, y)))

            memo[key] = result + 1

        return memo[key]

    result =  min_flips(input)

    return result if result < 2**32 else -1

from collections import deque

def is_final(input):
    return all(x for x in input)

def do_find_iterative(input, K):
    flips = [(x - K, x) for x in range(K, len(input) + 1)]

    visited  = set()

    todo = deque()
    todo.append((input, 0))

    while len(todo) > 0:
        (next_to_process, depth) = todo.popleft()

        key = tuple(next_to_process)
        if key not in visited:
            visited.add(key)

            if is_final(next_to_process):
                return depth

            for x, y in flips:
                todo.append((flip(next_to_process, x, y), depth + 1))

    return -1

def do_find_lineal(input, K):
    new_input = input
    flips = 0

    for i in range(0, len(input) - K + 1):
        if not new_input[i]:
            new_input = flip(new_input, i, i + K)
            flips += 1

    return flips if is_final(new_input) else -1


with open('input/A-large-practice.in') as f:
    print(f.__next__())
    i = 1
    a = lambda x: str(x) if x >= 0 else "IMPOSSIBLE"

    for line in f:
        split, K = line.strip().split(' ')
        result = do_find_lineal([x == '+' for x in split], int(K))
        print('Case #{}: {}'.format(i, a(result)))
        i += 1
