# scope = The region that a variable is recognized
#        A variable is only avaible from inside of the region it is created
#        A global and locally scoped versions of a variable can be created

name = "Bro"    #global scope (avaible inside and outside functions)

def display_name():
   # name = "code"    #local scope (avaible only inside this function)
    print(name)

print(name)
display_name()   # l function ki met7otelhech local scope bech tekhou l global scope*
