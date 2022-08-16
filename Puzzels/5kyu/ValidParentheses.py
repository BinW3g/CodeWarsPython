# codewars challenge link
# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    open_bracket = 0
    for c in string:
        if c == "(":
            open_bracket += 1
        if c == ")":
            open_bracket -= 1
        if open_bracket < 0:
            return False
    if open_bracket != 0:
        return False
    return True


if __name__ == '__main__':
    print(valid_parentheses("  (") == False)
    print(valid_parentheses(")test") == False)
    print(valid_parentheses("") == True)
    print(valid_parentheses("hi())(") == False)
    print(valid_parentheses("hi(hi)()") == True)
