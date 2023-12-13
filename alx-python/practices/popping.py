fibo_list = [0, 1, 1, 2, 3, 5, 8, 13]
infos = [{"name": "deji", "age": 26}, {"name": "warith", "age": 24}]

popped = fibo_list.pop(3)
# print(popped)
# print(fibo_list)

index = fibo_list.index(5, 4, 7)
print(index)

infos.sort(key=lambda x: x["age"])
print(infos)
