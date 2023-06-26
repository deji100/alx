print('A = ', ord("A"))
print('65 = ', chr(65))


# exp2:
name = input("Pls fill in your name. ")
secret = ''
decrypted = ''

for x in name:
    secret += str(ord(x))

print(secret)

for y in range(0, len(secret)-1, 2):
    decrypted += chr(int(secret[y:y+2]))

print(decrypted)

