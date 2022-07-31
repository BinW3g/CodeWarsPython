# codewars challenge link
# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

def high(x):
    high_score = 0
    for word in x.split(" "):
        current_score = 0
        for letter in word:
            current_score += abs(ord(' a') - ord(letter) - 1)
        if current_score > high_score:
            high_score = current_score
            word_with_hs = word
    return word_with_hs


# tests
if __name__ == "__main__":
    print(high('man i need a taxi up to ubud') == 'taxi')
    print(high('what time are we climbing up the volcano') == 'volcano')
    print(high('take me to semynak') == 'semynak')
    print(high('aa b') == 'aa')
    print(high('b aa') == 'b')
    print(high('bb d') == 'bb')
    print(high('d bb') == 'd')
    print(high("aaa b") == "aaa")
