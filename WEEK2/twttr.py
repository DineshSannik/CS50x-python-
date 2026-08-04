string = input("Input: ")
vowels = "aeiouAEIOU"
for c in string:
    if c in vowels:
        print("", end="")
    else:
        print(c, end="")
        