import sys 

for line in sys.stdin:
    if line.strip() == "q":
        break
    print(f"Line : {line}")

print("Exit")

sys.stdout.write("Hello World")