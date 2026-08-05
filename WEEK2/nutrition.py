food = input("Item: ")
food = food.lower()
match food:
    case "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "strawberries" | "tangerine":
        print("Calories: 50")
    case "grapefruit" | "nectarine" | "peach":
        print("Calories: 60")
    case "apple":
        print("Calories: 130")
    case "banana":
        print("Calories: 110")
    case "grapes" | "kiwifruit":
        print("Calories: 90")
    case "lime":
        print("Calories: 20")
    case "orange":
        print("Calories: 80")
    case "pear" | "sweet cherries":
        print("Calories: 100")
    case "plums":
        print("Calories: 70")
    case "watermelon":
        print("Calories: 80")
    case __:
        end = ""