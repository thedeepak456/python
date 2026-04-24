day = input("Enter the Day name")

match day:
    case "monday":
        print("We need to work today")
    case "tuesday":
        print("We need to work today")
    case "Wednesday":
        print("We need to work today")
    case "thusday":
        print("We need to work today")
    case "friday":
        print("We need to work today")
    case "saturday":
        print("Today is holiday")
    case "sunday":
        print("Today is holiday")
    case "good friday":
        print("Today is holiday")
    case "diwali":
        print("Today is holiday")
    case "holi":
        print("Today is holiday")
    case _:
        print('Invalid day name')