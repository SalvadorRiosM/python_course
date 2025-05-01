import sys

try:        # Trata de realizar algo cuando se pide los valores
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1)                             # Error de estado 1


print(f"{x} / {y} = result {result}")
