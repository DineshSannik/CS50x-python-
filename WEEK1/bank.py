bank = input("Greeting: ")
bank = bank.lower().strip()
if bank.startswith("hello"):
    print("$0")
elif bank[0] == "h":
    print("$20")
else:
    print("$100")