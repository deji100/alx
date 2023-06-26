def print_list(arg_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            if i != x-1:
                print("{:d}".format(arg_list[i]), end=" ")
            else:
                print("{:d}".format(arg_list[i]))
            count += 1
        except IndexError:
            print("x index is out of range")

    return count

print(print_list([1, 2, 3, 4, 5], 5))