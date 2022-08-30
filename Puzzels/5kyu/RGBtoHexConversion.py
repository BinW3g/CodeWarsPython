# codewars challenge link
# https://www.codewars.com/kata/513e08acc600c94f01000001/

def rgb(r, g, b):
    r = 0 if r < 0 else r
    g = 0 if g < 0 else g
    b = 0 if b < 0 else b
    r = 255 if r > 255 else r
    g = 255 if g > 255 else g
    b = 255 if b > 255 else b
    return (str(hex(r))[2:].zfill(2) + str(hex(g))[2:].zfill(2) + str(hex(b))[2:].zfill(2)).upper()


if __name__ == '__main__':
    print(rgb(0, 0, 0) == "000000")
    print(rgb(1, 2, 3) == "010203")
    print(rgb(255, 255, 255) == "FFFFFF")
    print(rgb(254, 253, 252) == "FEFDFC")
    print(rgb(-20, 275, 125) == "00FF7D")

