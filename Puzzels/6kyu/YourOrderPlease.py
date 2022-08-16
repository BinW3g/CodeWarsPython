# codewars challenge link
# https://www.codewars.com/kata/55c45be3b2079eccff00010f
import re


def order(sentence):
    if not sentence:
        return ""
    words = sentence.split(" ")
    solution = [""] * len(words)
    for w in words:
        index = int(re.findall(r'\d+', w)[0])
        solution[index-1] =  w
    return ' '.join(solution) if len(solution) > 0 else ""


if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
    print(order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople")
    print(order("") == "")
