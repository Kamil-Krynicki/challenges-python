def response(card_set):
    if len(card_set) == 0:
        return "Volunteer cheated!"
    elif len(card_set) > 1:
        return "Bad magician!"
    else:
        return card_set.pop()


with open('input/A-small-practice.in') as f:
    def get_row(row):
        skip_rows(row - 1)
        result = set(map(int, next(f).split(' ')))
        skip_rows(4 - row)
        return result


    def skip_rows(row):
        while row > 0:
            next(f)
            row = row - 1


    T = int(next(f))
    for t in range(1, T + 1):
        row_a = get_row(int(next(f)))
        row_b = get_row(int(next(f)))

        print('Case #{}: {}'.format(t, response(row_a & row_b)))
