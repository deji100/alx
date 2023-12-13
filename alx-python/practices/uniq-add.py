def uniq_add(my_list=[]):
    return sum(list(map(lambda x: x, list(set(my_list)))))

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)

print(result)