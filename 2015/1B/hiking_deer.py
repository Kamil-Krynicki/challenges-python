import bisect
import functools


def arrival_times(starting_angle, cycle_times):
    remaining_angle = (360 - starting_angle) / 360
    return list(zip([time * remaining_angle for time in cycle_times], cycle_times))


def arrive_before_me(arrival_times, my_time):
    return bisect.bisect_left(list(map(lambda x: x[0], arrival_times)), my_time)


def arrive_after_me(arrival_times, my_time):
    return len(arrival_times) - arrive_before_me(arrival_times, my_time)


def times_overtaken(arrival_times, my_time):
    return sum(filter(lambda x: x > 0, [(my_time - time) // travel_time for (time, travel_time) in arrival_times]))


def number_of_encounters(arrival_times, my_time):
    return int(arrive_after_me(arrival_times, my_time) + times_overtaken(arrival_times, my_time))


threshold = 5


def find_min(steps, cost_function):
    def find_min_seq2(steps):
        return min(map(cost_function, [x * 0.01 for x in range(5000)]))

    def find_min_seq(start, end, steps):
        i_val = cost_function(steps[start])
        for i in range(start + 1, end):
            i_val = min(i_val, cost_function(steps[i]))

        return i_val

    def find_min_rec(start, end, steps):
        if end - start < threshold:
            return find_min_seq(start, end, steps)

        mid = start + (end - start) // 2

        left_potential = cost_function(steps[start])
        mid_potential = cost_function(steps[mid])
        right_potential = cost_function(steps[end - 1])

        if left_potential == 0 or mid_potential == 0 or right_potential == 0:
            return 0

        if mid_potential <= right_potential and left_potential < mid_potential:
            return find_min_rec(start, mid, steps)

        if left_potential >= mid_potential and mid_potential > right_potential:
            return find_min_rec(mid, end, steps)

        return min(find_min_rec(start, mid, steps), find_min_rec(mid, end, steps))

    jajko = set(b for a in times for b in [ a[1] ] )

    return find_min_seq2(jajko)


def merge(a, b):
    c = []
    a_index = 0
    b_index = 0
    while len(a) > a_index and len(b) > b_index:
        if a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index += 1
        else:
            c.append(b[b_index])
            b_index += 1
    if len(b) > b_index:
        c += b[b_index:]
    else:
        c += a[a_index:]
    return c


with open('input/C-small-practice-2.in') as f:
    T = int(next(f))
    for t in range(1, T + 1):
        N = int(next(f))
        times = []
        for i in range(N):
            D, H, M = map(int, next(f).split(' '))
            times = merge(times, arrival_times(D, range(M, M + H)))

        potential = lambda t: number_of_encounters(times, t)

        print('Case #{}: {}'.format(t, min(map(potential, [x*0.01 for x in range(5000)]))))
