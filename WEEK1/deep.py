a = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
answer1 = a.strip()
if a == "42":
    print("yes")
elif a == "forty-two":
    print("yes")
elif a==("forty two"):
    print("yes")
elif a==("Forty Two"):
    print("yes")
elif answer1 in ("42"):
    print("yes")
elif a==("FoRty TwO"):
    print("yes")
else:
    print("no")