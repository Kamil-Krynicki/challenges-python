def can_be_placed(R, C, M):
    if M == 0:
        return print_map(R, C, R, C)

    empty = R * C - M

    if empty == 1:
        return print_map(R, C, 1, 1)

    if C == 1:
        return print_map(R, C, empty, 1)

    if R == 1:
        return print_map(R, C, 1, empty)


    for y in range(C, 1, -1):
        for x in range(R, 1, -1):
            r = empty - x*y

            if r == 0:
                return print_map(R, C, x, y)
            if r > 1:
                if r <= y and x < R:
                    return print_map(R, C, x, y, r, 0)
                if r <= x and y < C:
                    return print_map(R, C, x, y, 0, r)
                if r <= x + y and x < R and y < C:
                    r_1 = min(y, r//2)
                    r_2 = r - r_1

                    if r_1 != 1 and r_2 != 1:
                        return print_map(R, C, x, y, r_1, r_2)

    return "Impossible"



def print_map(rows, columns, empty_rows, empty_columns, empty_cells_below = 0, empty_cells_right = 0):
    result =  [['*' for b in range(columns)] for a in range(rows)]

    for row in range(empty_rows):
        for column in range(empty_columns):
            result[row][column] = '.'

    for row in range(empty_cells_right):
        result[row][empty_columns] = '.'

    for column in range(empty_cells_below):
        result[empty_rows][column] = '.'

    result[0][0] = 'c'

    return '\n'.join([''.join(u) for u in result])

with open('input/C-large-practice.in') as f:
    T = int(next(f))
    for t in range(1, T + 1):
        R, C, M = map(int, next(f).split(' '))

        print('Case #{}:'.format(t))
        # print('R {} C {} M {}:'.format(R, C, M))
        print(can_be_placed(R, C, M))


# R = 5
# C = 4
# for M in range(0, R*C + 1):
#     print('R {} C {} M {} empty {}:'.format(R, C, M, R*C-M))
#     print(can_be_placed(R, C, M))

