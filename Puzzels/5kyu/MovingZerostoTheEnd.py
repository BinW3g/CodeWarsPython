# codewars challenge link
# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    count_0 = 0
    erg_lst = list()
    for n in lst:
        if n == 0:
            count_0 += 1
        else:
            erg_lst.append(n)
    erg_lst.extend(list(map(int, list("0"*count_0))))
    return erg_lst


if __name__ == '__main__':
    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(move_zeros([0, 0]) == [0, 0])
    print(move_zeros([0]) == [0])
    print(move_zeros([]) == [])