# Method 1
fibo_list = [0, 1]

while len(fibo_list) <= 10:
    next_fibo = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(next_fibo)
else:
    print(fibo_list)

# Method 2

a, b = 0, 1

while a <= 10:
    print(a)
    a, b = b, a + b