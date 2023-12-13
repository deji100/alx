for x in range(0, 100):
    if x == 0 or x == 99:
        continue
    for y in range(0, x+1):
        if x < y:
            print(f"{x:02}", end=", ")