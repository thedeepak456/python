# def abc(name):
#     print("disco dance ",name)

# abc('munni')
# abc('munna')
# abc('chunna')


# functions to sum the values

# def jhethalal(a=0,b=0,c=0):
#     result =a+b+c
#     print('tumne mere ko itne ruppe diye',result)

# jhethalal(500,400)

def starCounting(end):
    while end >= 1:
        print('*' * end)
        end -= 1

starCounting(3)

def abb(end):
    for x in range(end):
        print('*'*end)
        end -=1

abb(5)