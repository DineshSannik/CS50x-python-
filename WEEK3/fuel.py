while True:
    fuel = input("Fraction: ")
    if fuel == "-1":
        break
        
    try:
        if "/" not in fuel:
            continue
            
        numerator, denominator = fuel.split("/")
        x = int(numerator)
        y = int(denominator)

        if x < 0 or y <= 0 or x > y:
            continue
            
        percentage = round((x / y) * 100) 
        
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
            
        break # Exit the loop after a successful print
        
    except (ValueError, ZeroDivisionError):
        pass
