# codewars challenge link
# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n):
    n = list(map(str, n))
    return "(" + "".join(n[0:3]) + ") " + "".join(n[3:6]) + "-" + "".join(n[6:])


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
    print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111")
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
    print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890")
    print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000")