# functions

def greet_according_to_time(taketime):
    if taketime >= 5 and taketime <= 10:
        print("good morning dosto")
    elif taketime >= 11 and taketime <= 16:
        print("good afternoon dosto")
    elif taketime >= 17 and taketime <= 20:
        print("good evening dosto")
    elif taketime >= 21 and taketime <= 23:
        print("good night dosto")
    elif taketime >= 00 and taketime <= 4:
        print("mid night dosto")
    else:
        print("enter valid time (00-23)")
        
    