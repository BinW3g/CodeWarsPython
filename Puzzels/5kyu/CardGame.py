# codewars challenge link
# https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5

# todo needs optimization
def card_game(n):
    i = 0
    points = [0, 0]
    while n > 0:
        if n % 2 == 1 or (n / 2 % 2 == 0 and n / 2 != 2):
            points[i % 2] += 1
            n -= 1
        else:
            points[i % 2] += n/2
            n /= 2
        i += 1
    return points[0]


if __name__ == '__main__':
    print(card_game(10) == 8)
    print(card_game(4) == 3)
    print(card_game(5) == 2)
    print(card_game(12) == 9)
    print(card_game(100000000000) == 99999999950)
