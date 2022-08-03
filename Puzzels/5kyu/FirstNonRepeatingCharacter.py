# codewars challenge link
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    for c in string:
        if string.lower().count(c.lower()) == 1:
            return c
    return ''


if __name__ == '__main__':
    print(first_non_repeating_letter('a') == 'a')
    print(first_non_repeating_letter('stress') == 't')
    print(first_non_repeating_letter('moonmen') == 'e')
    print(first_non_repeating_letter('') == '')
    print(first_non_repeating_letter('abba') == '')
    print(first_non_repeating_letter('aa') == '')
    print(first_non_repeating_letter('~><#~><') == '#')
    print(first_non_repeating_letter('hello world, eh?') == 'w')
    print(first_non_repeating_letter('sTreSS') == 'T')
    print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ',')
