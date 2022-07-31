# codewars challenge link
# https://www.codewars.com/kata/5839edaa6754d6fec10000a2


def find_missing_letter(chars):
    for i, char in enumerate(chars, start=-1):
        if i == -1:
            continue
        if ord(char) - ord(chars[i]) - 1 != 0:
            return chr(ord(char)-1)


# tests
if __name__ == "__main__":
    print(find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e')
    print(find_missing_letter(['O', 'Q', 'R', 'S']) == 'P')
