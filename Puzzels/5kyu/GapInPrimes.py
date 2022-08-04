# codewars challenge link
# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4

import math


def gap(g, m, n):
    for i in range(m, n + 1, 1):
        if is_prime(i):
            for j in range(i + 1, n + 1, 1):
                if is_prime(j):
                    if j - i == g:
                        return [i, j]
                    break


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(gap(2, 100, 110) == [101, 103])
    print(gap(4, 100, 110) == [103, 107])
    print(gap(6, 100, 110) == None)
    print(gap(8, 300, 400) == [359, 367])
    print(gap(10, 300, 400) == [337, 347])
    print(gap(2, 100, 103) == [101, 103])
    print(gap(2, 3, 10) == [3, 5])
    print(is_prime(4))
