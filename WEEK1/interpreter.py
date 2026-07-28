x, y, z = input("Expression: ").split()
x = int(x)
z = int(z)
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    if z == 0:
        print("Error: Division by zero")
    else:
        print(f"{x / z:.1f}")
