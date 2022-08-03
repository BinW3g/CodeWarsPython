# codewars challenge link
# https://www.codewars.com/kata/550f22f4d758534c1100025a


cancel = {"NORTH": "SOUTH",
          "SOUTH": "NORTH",
          "EAST": "WEST",
          "WEST": "EAST"}


def dirReduc(arr):
    i = 0
    while i < len(arr)-1:
        if cancel[arr[i]] == arr[i+1]:
            arr.pop(i)
            arr.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1
    return arr


if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(a) == ['WEST'])
    u = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(u) == ["NORTH", "WEST", "SOUTH", "EAST"])
