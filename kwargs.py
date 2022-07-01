# **kwargs = parameter that will pack all args into a dictionary
#            useful so that a function can accept a varying amount of keyword args

#def hello(**kwargs):
#    print("Hello " + first + " " + last + " " + middle)
#hello(first="firas",last="charrada",middle="toffeha")

def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

#    print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first="firas",last="char",dynamite="Hola",toffeha="tannana")