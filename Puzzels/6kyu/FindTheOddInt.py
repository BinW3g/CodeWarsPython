# codewars challenge link
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def find_it(seq):
    numbers = dict()
    for num in seq:
        if num not in numbers:
            numbers[num] = 0
        numbers[num] += 1

    for num in numbers:
        if numbers[num] % 2 != 0:
            return num


if __name__ == '__main__':
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5)
    print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1)
    print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5)
    print(find_it([10]) == 10)
    print(find_it([10, 10, 10]) == 10)
    print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10)
    print(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1)
