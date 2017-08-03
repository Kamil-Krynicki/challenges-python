from itertools import chain


def distribute_x(occupied, size):
    free_x = set(range(size)) - set(x for (x, y) in occupied)
    free_y = set(range(size)) - set(y for (x, y) in occupied)

    return occupied | set(zip(free_x, free_y))


def distribute_p(occupied, N):
    sum = lambda x, y: y + x
    dif = lambda x, y: y - x
    blocked_y_l = {f(x, y) for f in (sum, dif) for (x, y) in occupied}
    blocked_y_r = {f(b, N - 1) for f in (sum, dif) for b in blocked_y_l}

    return occupied | set((0, y) for y in set(range(N - 1)) - blocked_y_l) \
           | set((N - 1, y) for y in set(range(N - 1)) - blocked_y_r)


def read_line(f):
    return str(f.__next__()).split(' ')


def read_test_case(f):
    N, M = map(int, str(f.__next__()).split(' '))
    x_positions = set()
    p_positions = set()
    o_positions = set()

    for i in range(M):
        pos_type, x, y = read_line(f)

        if pos_type == '+':
            p_positions.add((int(x) - 1, int(y) - 1))
        elif pos_type == 'x':
            x_positions.add((int(x) - 1, int(y) - 1))
        elif pos_type == 'o':
            o_positions.add((int(x) - 1, int(y) - 1))

    return x_positions, p_positions, o_positions, N


# for x in distribute_p({(0, 2)}, 3):
#    print(x)


with open('input/test_input.in') as f:
    T = int(f.__next__())

    for i in range(T):
        in_x_pos, in_p_pos, in_o_pos, N = read_test_case(f)

        out_p_pos = distribute_p(in_p_pos | in_o_pos, N)
        out_x_pos = distribute_x(in_x_pos | in_o_pos, N)
        out_o_pos = out_p_pos & out_x_pos

        out_p_pos -= out_o_pos
        out_x_pos -= out_o_pos

        print('Case #{}: {} {}'.format(i + 1, len(out_p_pos) + len(out_x_pos) + 2 * len(out_o_pos),
                                       len(out_p_pos - in_p_pos) + len(out_x_pos - in_x_pos)
                                       + len(out_o_pos - in_o_pos)))

        for point in out_o_pos - in_o_pos:
            print('o {} {}'.format(point[0] + 1, point[1] + 1))

        for point in out_p_pos - in_p_pos:
            print('+ {} {}'.format(point[0] + 1, point[1] + 1))

        for point in out_x_pos - in_x_pos:
            print('x {} {}'.format(point[0] + 1, point[1] + 1))
