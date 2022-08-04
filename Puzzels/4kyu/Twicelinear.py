# codewars challenge link
# https://www.codewars.com/kata/5672682212c8ecf83e000050

import math


def dbl_linear(n):
    u = [1]
    iterations = round(math.log2(n))+3
    calc(u, 1, iterations)
    u = list(set(u))
    u.sort()
    return u[n]


def calc(u, x, iterations_left):
    if iterations_left == 0:
        return
    y = 2 * x + 1
    z = 3 * x + 1
    u.append(y)
    u.append(z)
    calc(u, y, iterations_left-1)
    calc(u, z, iterations_left-1)


if __name__ == '__main__':
    print(dbl_linear(10) == 22)
    print(dbl_linear(20) == 57)
    print(dbl_linear(30) == 91)
    print(dbl_linear(50) == 175)
    print(dbl_linear(500) == 3355)
    print(dbl_linear(60000) == 1511311)