# codewars challenge link
# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import re

def top_3_words(text):
    text = re.sub("[^A-Za-z']", " ", text.lower())
    text = re.sub("[^A-Za-z]'[^A-Za-z]\W", " ", text)
    words = text.split(" ")
    word_count = dict()
    for word in words:
        if word:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
    return sorted(word_count, key=word_count.get, reverse=True)[:3]


if __name__ == '__main__':
    print(top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"])
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e") == ["e", "ddd", "aa"])
    print(top_3_words("  //wont won't won't ") == ["won't", "wont"])
    print(top_3_words("  , e   .. ") == ["e"])
    print(top_3_words("  ...  ") == [])
    print(top_3_words("  '  ") == [])
    print(top_3_words("  '''  ") == [])
    print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
           mind, there lived not long since one of those gentlemen that keep a lance
           in the lance-rack, an old buckler, a lean hack, and a greyhound for
           coursing. An olla of rather more beef than mutton, a salad on most
           nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
           on Sundays, made away with three-quarters of his income.""") == ["a", "of", "on"])
