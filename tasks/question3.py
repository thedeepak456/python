light = input("enter the name")
match light:
    case "red":
        print("stop")
    case "green":
        print("you can goo")
    case "yellow":
        print("wait") 
    case _:
        print("aage apki marzi")