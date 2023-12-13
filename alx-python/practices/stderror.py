import sys

def print_to_stderr(*a):
    print(*a, file=sys.stderr)
    print()
    print(sys.path)
    print()
    print(sys.modules)

print_to_stderr("Hello World")