# codewars challenge link
# https://www.codewars.com/kata/5629db57620258aa9d000014
import functools


def mix(s1, s2):
    chars1 = dict()
    chars2 = dict()
    length = len(s1) if len(s1) > len(s2) else len(s2)
    for i in range(0, length):
        if i < len(s1) and ord('a') <= ord(s1[i]) <= ord('z'):
            c = s1[i]
            if c not in chars1:
                chars1[c] = 1
            else:
                chars1[c] += 1
        if i < len(s2) and 97 <= ord(s2[i]) <= 122:
            c = s2[i]
            if c not in chars2:
                chars2[c] = 1
            else:
                chars2[c] += 1
    chars1 = remove_unnecessary_values(chars1)
    chars2 = remove_unnecessary_values(chars2)
    solution = list()
    for i in range(ord('a'), ord('z')+1):
        char = chr(i)
        if char in chars1.keys() and char in chars2.keys():
            if chars1[char] == chars2[char]:
                solution.append("=:" + char * chars1[char] + "/")
            else:
                solution.append((("1:" + char * chars1[char]) if chars1[char] > chars2[char] else (
                            "2:" + char * chars2[char])) + "/")
        elif char in chars1.keys():
            solution.append("1:" + char * chars1[char] + "/")
        elif char in chars2.keys():
            solution.append("2:" + char * chars2[char] + "/")
    solution = sorted(solution, key=functools.cmp_to_key(compare))
    return "".join(solution)[:-1]


def compare(x, y):
    if len(x) == len(y):
        if x > y:
            return 0
        return 1 if x > y else -1
    return 1 if len(x) < len(y) else -1


def remove_unnecessary_values(chars):
    keys = list(chars.keys())
    for key in keys:
        if chars[key] == 1:
            chars.pop(key)
    return chars


if __name__ == '__main__':
    print(mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs",
              "MynwdKizfd$lvse+gnbaGydxyXzayp") == '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
    print(mix("looping is fun but dangerous",
              "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    print(mix(" In many languages",
              " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    print(mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo")
    print(mix("codewars", "codewars") == "")
    print(mix("A generation must confront the looming ",
              "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
