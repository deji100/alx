def solve_algebra(s):
    equationList = s.split()
    x = 0
    for y in equationList:
        try:
            if type(int(y)) == int:
                x += int(y)
        except ValueError:
            # print("y is not an int.")
            pass

    print('X = ', x)

solve_algebra("x + 6 + 5 = 15")

