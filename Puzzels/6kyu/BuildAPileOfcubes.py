# codewars challenge link
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/

def find_nb(m):
    erg = 0
    base = 1
    while erg != m:
        if erg > m:
            return -1
        erg += pow(base, 3)
        base += 1
    return base-1


if __name__ == '__main__':
    print(find_nb(4183059834009) == 2022)
    print(find_nb(24723578342962) == -1)
    print(find_nb(135440716410000) == 4824)
    print(find_nb(40539911473216) == 3568)
    print(find_nb(26825883955641) == 3218)
