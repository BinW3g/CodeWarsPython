# codewars challenge link
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/

def narcissistic(value):
    digits = len(str(value))
    calc = 0
    for digit in str(value):
        calc += pow(int(digit), digits)
    return calc == value


if __name__ == '__main__':
    print(narcissistic(7) == True)
    print(narcissistic(371) == True)
    print(narcissistic(122) == False)
    print(narcissistic(4887) == False)
