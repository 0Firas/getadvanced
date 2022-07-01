import random

x = random.randint(1, 6)# random int
print(x)
print("-------------------------")
#next
y = random.random()      # random float
print(y)
print("--------------------------")
#next

mylist = ['rock','paper','scissors']
z = random.choice(mylist)
print(z)
print("---------------------------")
#next

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)
print(cards)
