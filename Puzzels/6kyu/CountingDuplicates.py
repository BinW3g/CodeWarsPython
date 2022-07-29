# codewars challange link
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    occurred_char = dict()
    for char in text.lower():
        if char in occurred_char:
            occurred_char[char] += 1
        else:
            occurred_char[char] = 1
    return len(list(filter(lambda v: v > 1, occurred_char.values())))

# testing
if __name__ == "__main__":
    print(duplicate_count(""))  # 0
    print(duplicate_count("abcde"))  # 0
    print(duplicate_count("abcdeaa"))  # 1
    print(duplicate_count("abcdeaB"))  # 2
    print(duplicate_count("Indivisibilities"))  # 2
