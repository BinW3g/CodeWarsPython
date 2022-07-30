# codewars challenge link
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python


def find_outlier(integers):
    if integers[0] % 2 == integers[1] % 2:
        even = (integers[0] % 2 == 0)
    else:
        even = (integers[2] % 2 == 0)

    for n in integers:
        if even and n % 2 != 0:
            return n
        elif not even and n % 2 == 0:
            return n


if __name__ == "__main__":
    print(find_outlier([2, 4, 6, 8, 10, 3]))  # 3
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # 11
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # 160
