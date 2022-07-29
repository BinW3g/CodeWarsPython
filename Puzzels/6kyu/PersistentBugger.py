# codewars puzzle link
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    return calc_new_number(n, 0)


# with recursion
def calc_new_number(n, count):
    if n < 10:
        return count
    else:
        new_n = 1
        while n != 0:
            new_n *= n % 10
            n = int(n / 10)
        return calc_new_number(new_n, count + 1)


# tests
if __name__ == "__main__":
    print(persistence(39))
    print(persistence(4))
    print(persistence(25))
    print(persistence(999))
