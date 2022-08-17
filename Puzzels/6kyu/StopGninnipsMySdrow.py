# codewars challenge link
# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    out = ""
    for word in sentence.split():
        if len(word) < 5:
            out += word + " "
        else:
            out += word[::-1] + " "
    return out[:-1]


if __name__ == '__main__':
    print(spin_words("Welcome") == "emocleW")
    print(spin_words("to") == "to")
    print(spin_words("CodeWars") == "sraWedoC")
    print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")
    print(spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes")

