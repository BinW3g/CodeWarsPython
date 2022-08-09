# codewars challenge link
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

def ips_between(start, end):
    start = start.split(".")
    end = end.split(".")
    dif = 0
    for i in range(0, len(start)):
        dif += (int(end[i]) - int(start[i])) * pow(256, (3 - i))
    return dif


if __name__ == '__main__':
    print(ips_between("10.0.0.0", "10.0.0.50") == 50)
    print(ips_between("20.0.0.10", "20.0.1.0") == 246)
