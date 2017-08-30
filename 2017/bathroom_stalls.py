from queue import PriorityQueue


def do_find(N, K):
    queue = PriorityQueue()

    memo = {N:1}
    queue.put(-N)

    left, right = 0, 0

    while K > 0:
        longest = -queue.get()
        count = memo.pop(longest)

        left = (longest - 1) // 2
        right = (longest - 1) - left

        if left not in memo.keys():
            queue.put(-left)
        memo[left] = memo.setdefault(left, 0) + count

        if right not in memo.keys():
            queue.put(-right)
        memo[right] = memo.setdefault(right, 0) + count

        K -= count

    return max(left ,right), min(left, right)


with open('input/C-large-practice.in') as f:
    print(f.__next__())

    i = 1
    for line in f:
        N, K = map(int, line.strip().split(' '))
        max_, min_ = do_find(N, K)
        print('Case #{}: {} {}'.format(i, max_, min_))
        i += 1
