def is_prime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False

    return True

def get_primes(num_list):
    primes = []
    for y in num_list:
        if is_prime(y):
            primes.append(y)

    print(primes)

get_primes(range(3, 15))
