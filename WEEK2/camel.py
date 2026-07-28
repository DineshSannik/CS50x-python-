camelcase = input("camelcase: ")
print("snake_case: ", end="")

for c in camelcase:
    if c.isupper():
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")

print()
