N = 32
J = 500

max_base = 10
min_base = 2

base_conversion_values = [None] * min_base
for base in range(min_base, max_base + 1):
    base_array = [1]
    for step in range(N - 1):
        base_array.append(base * base_array[-1])
    base_conversion_values.append(base_array)


def increment(bit_vector):
    i = 0
    while bit_vector[i]:
        bit_vector[i] = 0
        i += 1
    bit_vector[i] = 1

    return bit_vector


def bit_vector_iterator(size):
    result = [0] * size
    result[0] = 1
    result[-1] = 1

    yield result
    while ~all(result):
        result = increment(increment(result))
        yield result


low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def nontrivial_divisor(value):
    for prime in low_primes:
        if value % prime == 0:
            if value > prime:
                return prime
            else:
                return -1

    return -1


def to_base(bits, base):
    return sum(map(lambda val: val[0] * val[1], zip(bits, base_conversion_values[base])))


def nontrivial_divisors_for_bases(vector, bases):
    divisors = []

    for base in bases:
        divisor = nontrivial_divisor(to_base(vector, base))

        if divisor < 0:
            return divisors

        divisors.append(divisor)

    return divisors


base_range = range(min_base, max_base + 1)
print('Case #1:')
for bit_vector in bit_vector_iterator(N):
    if J == 0:
        break

    divisors = nontrivial_divisors_for_bases(bit_vector, base_range)

    if len(divisors) == len(base_range):
        print(''.join(map(str, bit_vector[::-1])) + ' ' + ' '.join(map(str, divisors)))
        J -= 1
