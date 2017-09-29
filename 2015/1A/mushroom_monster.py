def mushroom_eating_method_1(snapshots) :
    return sum(filter(lambda x : x>0, evolution(snapshots)))


def mushroom_eating_method_2(snapshots) :
    min_consumption_speed = max(evolution(snapshots))
    return sum(map(lambda x : min(x, min_consumption_speed), snapshots[:-1]))


def evolution(snapshots):
    return [j-i for i, j in zip(snapshots[1:], snapshots[:-1])]


with open('input/A-large-practice.in') as f:
    lines = f.read().split('\n')
    for i in range(int(lines[0])):
        M = list(map(int, lines[2 * i + 2].split(' ')))
        print('Case #{}: {} {}'.format(i + 1, mushroom_eating_method_1(M), mushroom_eating_method_2(M)))