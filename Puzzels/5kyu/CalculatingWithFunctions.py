# codewars challenge link
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def zero(statement=""):
    if statement != "":
        return int(eval("0" + statement))
    return "0"


def one(statement=""):
    if statement != "":
        return int(eval("1" + statement))
    return "1"


def two(statement=""):
    if statement != "":
        return int(eval("2" + statement))
    return "2"


def three(statement=""):
    if statement != "":
        return int(eval("3" + statement))
    return "3"


def four(statement=""):
    if statement != "":
        return int(eval("4" + statement))
    return "4"


def five(statement=""):
    if statement != "":
        return int(eval("5" + statement))
    return "5"


def six(statement=""):
    if statement != "":
        return int(eval("6" + statement))
    return "6"


def seven(statement=""):
    if statement != "":
        return int(eval("7" + statement))
    return "7"


def eight(statement=""):
    if statement != "":
        return int(eval("8" + statement))
    return "8"


def nine(statement=""):
    if statement != "":
        return int(eval("9" + statement))
    return "9"


def plus(statement=""):
    return "+" + statement


def minus(statement=""):
    return "-" + statement


def times(statement=""):
    return "*" + statement


def divided_by(statement=""):
    return "/" + statement


if __name__ == '__main__':
    print(seven(times(five())) == 35)
    print(four(plus(nine())) == 13)
    print(eight(minus(three())) == 5)
    print(six(divided_by(two())) == 3)
