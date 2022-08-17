# codewars challenge link
# https://www.codewars.com/kata/52597aa56021e91c93000cb0

# a bit unperformed append as much as possible at once (found out throw other solutions)
def is_merge(s, part1, part2):
    for position, c in enumerate(s):
        if len(part1) > 0 and c is part1[0] and len(part2) > 0 and c is part2[0]:
            equal_part1 = 0
            equal_part2 = 0
            while (len(part1) > equal_part1 or len(part2) > equal_part2) and equal_part1 == equal_part2:
                if s[position + equal_part1] == part1[equal_part1]:
                    equal_part1 += 1
                if s[position + equal_part2] == part2[equal_part2]:
                    equal_part2 += 1
            if equal_part1 >= equal_part2:
                part1 = part1[1:]
            elif equal_part1 < equal_part2:
                part2 = part2[1:]
        elif len(part1) > 0 and c is part1[0]:
            part1 = part1[1:]
        elif len(part2) > 0 and c is part2[0]:
            part2 = part2[1:]
        else:
            return False
    if len(part1) > 0 or len(part2) > 0:
        return False
    return True


if __name__ == '__main__':
    print(is_merge("Bananas from Bahamas", "Bahas", "Bananas from am"))
    print(is_merge('codewars', 'code', 'wars'))
    print(is_merge('codewars', 'cdw', 'oears'))
    print(not is_merge('codewars', 'cod', 'wars'))
