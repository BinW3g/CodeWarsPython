# codewars challenge link
# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    solution = list()
    for elm in a:
        if elm not in b:
            solution.append(elm)
    return solution


if __name__ == '__main__':
    print(array_diff([1, 2], [1]) == [2])
    print(array_diff([1, 2, 2], [1]) == [2, 2])
    print(array_diff([1, 2, 2], [2]) == [1])
    print(array_diff([1, 2, 2], []) == [1, 2, 2])
    print(array_diff([], [1, 2]) == [])
    print(array_diff([1, 2, 3], [1, 2]) == [3])
