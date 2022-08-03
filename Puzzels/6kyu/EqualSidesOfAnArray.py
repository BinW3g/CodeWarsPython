# codewars challenge link
# https://www.codewars.com/kata/550f22f4d758534c1100025a

def find_even_index(arr):
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


if __name__ == '__main__':
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3)
    print(find_even_index([1, 100, 50, -51, 1, 1]) == 1)
    print(find_even_index([1, 2, 3, 4, 5, 6]) == -1)
    print(find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3)
    print(find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0)
    print(find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6)
    print(find_even_index(list(range(1, 100))) == -1)
    print(find_even_index([0, 0, 0, 0, 0]) == 0)
    print(find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3)
    print(find_even_index(list(range(-100, -1))) == -1)
