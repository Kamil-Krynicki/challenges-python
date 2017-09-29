class AttendedQueue:
    def __init__(self, barbers):
        self.barbers = barbers
        self.size = len(barbers)

    def __getitem__(self, item):
        return sum(map(lambda b: item // b, self.barbers)) + self.size


def when_attended(my_pos, attended_queue):
    def approx_range():
        time = 1
        while attended_queue[time] < my_pos:
            time *= 2
        return (time // 2, time)

    (low, top) = approx_range()

    while low != top:
        mid = (low + top) // 2

        if attended_queue[mid] < my_pos:
            low = mid + 1
        else:
            top = mid

    return top


def which_barber(pos, barbers):
    queue = AttendedQueue(barbers)
    time = when_attended(pos, queue)

    # an adorably insane line of code
    return [i for i in range(len(barbers)) if (time % barbers[i]) == 0][pos - queue[time - 1] - 1] + 1


with open('input/B-large-practice.in') as f:
    lines = f.read().split('\n')
    for i in range(int(lines[0])):
        B, N = lines[2 * i + 1].split(' ')
        Bi = list(map(int, lines[2 * i + 2].split(' ')))
        print('Case #{}: {}'.format(i + 1, which_barber(int(N), Bi)))
