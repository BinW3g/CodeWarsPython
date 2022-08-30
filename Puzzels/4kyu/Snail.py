# codewars challenge link
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    if snail_map == [[]]:
        return []
    solution = list()
    i = 0
    while len(snail_map) > 0:
        match i % 4:
            case 0:
                solution.extend(snail_map.pop(0))
            case 1:
                for l in snail_map:
                    solution.append(l.pop(-1))
            case 2:
                snail_map[-1].reverse()
                solution.extend(snail_map.pop(-1))
            case 3:
                snail_map.reverse()
                for l in snail_map:
                    solution.append(l.pop(0))
                snail_map.reverse()
        i += 1
    return solution


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(snail(array) == expected)

    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(snail(array) == expected)
