amount = 50

while True:
    print("Amount Due:", amount)
    money = int(input("Insert Coin: "))
    if money == 25 or money == 10 or money == 5:
        if(money >= amount):
            print("Change Owed:", money-amount)
            break
        amount -= money
    else:
        continue