from collections import namedtuple

import math
import itertools

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Vector = namedtuple('Vector', ['x', 'y'])


def cross(a, b):
    return a.y * b.x - a.x * b.y


def dot(a, b):
    return a.x * b.x + a.y * b.y


def angle(a, b):
    atan = math.atan2(cross(a, b), dot(a, b))

    return atan if atan >= 0 else atan + 2 * math.pi


def vector(p1, p2):
    return Vector(p2.x - p1.x, p2.y - p1.y)


def is_convex(A, B, C):
    return angle(vector(B, A), vector(B, C)) <= math.pi




def radial_sort(center, points):
    points.sort(key=lambda a: angle(Vector(1, 0), Vector(a.x - center.x, a.y - center.y)))


def min_trees(center, points):
    radial_sort(center, points)

    starts = iter(points)
    ends = itertools.chain(points[1:], points)

    max_trees = 0

    start = next(starts)
    end = next(ends)

    trees = 2

    try:
        while True:
            while not is_convex(start, center, end):
                start = next(starts)
                trees -= 1

            while is_convex(start, center, end):
                end = next(ends)
                trees += 1

                if end == start:
                    return 0

            max_trees = max(max_trees, trees - 1)
    except:
        return len(points) - max_trees

with open('input/C-large-practice.in') as f:
    T = int(next(f))
    for t in range(T):
        print('Case #{}:'.format(t + 1))

        N = int(next(f))
        points = []
        for n in range(N) :
            x, y = next(f).split(' ')
            points.append(Point(x=int(x), y=int(y)))

        if N <= 3:
            for point in range(N):
                print(0)
        else:
            for point in range(N):
                print(min_trees(points[point], points[:point] + points[point + 1:]))

