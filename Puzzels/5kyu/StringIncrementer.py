# codewars challenge link
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

def increment_string(string):
    number_start = -1
    for i in range(len(string) - 1, -1, -1):
        if ord('0') > ord(string[i]) or ord(string[i]) > ord('9'):
            number_start = i + 1
            break

    if number_start == len(string) or string == "":
        return string + "1"

    if number_start == -1:
        number = int(string) + 1
        number_digits = len(string) - len(str(number))
        return "0" * number_digits + str(number)

    number = int(string[number_start:]) + 1
    number_digits = len(string) - number_start - len(str(number))
    return string[:number_start] + "0" * number_digits + str(number)

# better to do with rstrip
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))


if __name__ == '__main__':
    print(increment_string("foo") == "foo1")
    print(increment_string("foobar001") == "foobar002")
    print(increment_string("foobar1") == "foobar2")
    print(increment_string("foobar00") == "foobar01")
    print(increment_string("foobar99") == "foobar100")
    print(increment_string("foobar099") == "foobar100")
    print(increment_string("foob20564ar099") == "foob20564ar100")
    print(increment_string("") == "1")
    print(increment_string("1") == "2")
    print(increment_string("009") == "010")
    print(increment_string("{32629000000000566") == "{32629000000000567")
