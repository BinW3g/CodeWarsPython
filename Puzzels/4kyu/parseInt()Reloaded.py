# codewars challenge link
# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}


def parse_int(string):
    string = string.lower()
    if string == "one million":
        return 1000000
    if string == "zero":
        return 0
    result = 0
    hundreds = 0
    for part in string.split():
        if part == "and":
            continue
        if part == "thousand":
            result += hundreds * 1000
            hundreds = 0
        elif part == "hundred":
            hundreds *= 100
        elif "-" in part:
            parts = part.split("-")
            hundreds += number_dict[parts[0]]
            hundreds += number_dict[parts[1]]
        else:
            hundreds += number_dict[part]
    return result + hundreds


if __name__ == '__main__':
    print(parse_int('one') == 1)
    print(parse_int('twenty') == 20)
    print(parse_int('two hundred forty-six') == 246)
    print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen') == 783919)
