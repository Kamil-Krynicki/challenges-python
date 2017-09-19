def mushroom_eating_method_1(snapshots) :
    return sum(filter(lambda x : x>0, evolution(snapshots)))


def mushroom_eating_method_2(snapshots) :
    min_consumption_speed = max(evolution(snapshots))
    return sum(map(lambda x : min(x, min_consumption_speed), snapshots[:-1]))


def evolution(snapshots):
    return [j-i for i, j in zip(snapshots[1:], snapshots[:-1])]


val = list(map(int, '23 90 40 0 100 9'.split(' ')))
print(mushroom_eating_method_1(val))
print(mushroom_eating_method_2(val))