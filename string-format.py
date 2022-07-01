# str.format = optional method that gives users
#              more control when displaying output
import numbers

animal = "cow"
item = "moon"

#print("The "+animal+ " jumped over the"+item)
print("The {} jumped over the {} ".format(animal,item,))
print("The {1} jumped over the {0} ".format(animal,item,))  #positional arg
print("The {animal} jumped over the {item} ".format(animal="haw zebi",item="rrrrmoon",))  #keyword arg

print("-----------------------------------------------")
# f jdiiid

text = "The {} jumped over the {} "
print(text.format("bagra","sta7"))
print(text.format(animal,item))
print("------------------------------------------------")
#next section

name = "firas"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you ".format(name)) # {:10} sets a padding to the format
print("Hello my name is {:<10}. Nice to meet you ".format(name)) #align the format to the left within the padding you've set
print("Hello my name is {:>10}. Nice to meet you ".format(name)) # align the format the the right within the padding you've set
print("Hello my name is {:^10}. Nice to meet you ".format(name)) # center the format within the padding you've set
print("-------------------------------------------------------------------------")
#next section

number = 1000
print("the number pi is {:.7f}".format(number)) # tziiid kad matheb asfar bad lfasel
print("the number pi {:,}".format(number))     # tamel fasel automatic
print("the number pi {:b}".format(number))       # trodou binary number
print("the number pi {:o}".format(number))         # trodou octal number
print("the number pi {:X}".format(number))          # trodou hexadecimal
print("the number pi {:E}".format(number))         #mafhemtech zokomha ama trodou in scientific notation

















