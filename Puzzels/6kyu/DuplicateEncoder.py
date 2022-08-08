# codewars challenge link
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

def duplicate_encode(word):
    word = word.lower()
    new_string = ""
    for c in word:
        new_string += "(" if word.count(c) == 1 else ")"
    return new_string


if __name__ == '__main__':
    print(duplicate_encode("din") == "(((")
    print(duplicate_encode("recede") == "()()()")
    print(duplicate_encode("Success") == ")())())")
    print(duplicate_encode("(( @") == "))((")