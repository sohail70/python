################################################## Variables

######################## 1
favSnack = "MixedNuts"
print(favSnack*100)
######################## 2
neighborsFavSnack = "FrozenFruit"
concat = favSnack + neighborsFavSnack
print (concat*100)
######################## 3
groceries = ["spinach","carrot","potatoe","MixedNuts","tomato"]
favSnack in groceries
print(favSnack in groceries)
######################## 4
print(neighborsFavSnack in groceries)
######################## 5
favSnack,neighborsFavSnack = neighborsFavSnack,favSnack
print(favSnack,neighborsFavSnack)
favSnack,neighborsFavSnack = neighborsFavSnack,favSnack

################################################## Functions

######################## 1
groceriesPrices = [9.42,5.67,3.25,13.40,7.50]
mostExpensive = max(groceriesPrices)
cheapest = min(groceriesPrices)
print("The most expensive item is %s with price of %.2f" %(groceries[groceriesPrices.index(mostExpensive)], mostExpensive))
print("The cheapest item in your groceriy list is %s with price %s" %(groceries[groceriesPrices.index(cheapest)] , cheapest))

######################## 2
import random
n = random.randint(0,100)
print(n*favSnack)

######################## 3
print("One random item in grocery list is:", random.choice(groceries))

######################## 4
print("A random price rounded to the nearest integer is: ",round(random.choice(groceriesPrices)))

####################### 5
randPrice = random.choice(groceriesPrices)
print("Amount of change is",abs(randPrice-10))

################################################## Own functions

####################### 1
def all_the_snacks(snack):
    print(100*snack)

all_the_snacks(groceries[0])
all_the_snacks(groceries[1])
all_the_snacks(groceries[2])
all_the_snacks(groceries[3])
all_the_snacks(groceries[4])
all_the_snacks(2) 

####################### 2
def all_the_snacks(snack,spacer):
    print(100*(snack+spacer))

all_the_snacks(groceries[0]," ")
all_the_snacks(groceries[1]," ")
all_the_snacks(groceries[2]," ")
all_the_snacks(groceries[3]," ")
all_the_snacks(groceries[4]," ")
all_the_snacks("Soheil","Saman")
all_the_snacks(3,2)
#all_the_snacks(2,"Soheil") #ERROR

######################## 3
def all_the_snacks(snack,spacer,num):
    print(num*(snack+spacer))

all_the_snacks(groceries[0]," ",5)

######################## 4
def in_grocery_list(item):
    return item in groceries #function knows the outside var?! is it global?

print(in_grocery_list("MixedNuts"))
print(in_grocery_list("Peach"))

######################## 5
def price_matcher():
    print(random.choice(groceries),random.choice(groceriesPrices))
price_matcher()
######################## 6
def price_matcher():
    item = random.choice(groceries)
    price = random.choice(groceriesPrices)
    return item,price

def free_change():
    item,price = price_matcher()
    print("Change is %.2f" %abs(price-10),"for",groceries[groceriesPrices.index(price)])

free_change()
    

################################################## Arguments, Keyword Arguments, and defaults

######################## 1
def all_the_snacks(snack,spacer=',',num=100):
    print(num*(snack+spacer))

all_the_snacks(favSnack)

######################## 2
all_the_snacks(favSnack,'|')
all_the_snacks(favSnack,num=42) #using default spacer although its the second argument
all_the_snacks(favSnack,num=42,spacer='|')


################################################## Scope, input

######################## 1
my_color = input("What's you favorite color? ")
neighbor_color = input("What's the neighbor favorite color? ")

######################## 2
my_num = input("What's you favorite number? ")
#my_num+2 #ERROR because you can't string to number
print(float(my_num)+2)

######################## 3
def color_swapper(my_color,neighbor_color):
    my_color,neighbor_color = neighbor_color,my_color #I can swap them because they are global but it doesnt effect the global var(if you want that you need to use global my_color,)
    print("My favorite color is %s and my neighbor's favorite color is %s"%(my_color,neighbor_color))

color_swapper(my_color,neighbor_color)
print("my color is:", my_color) 
print("neighbor's color is:", neighbor_color)

######################## 4
def global_color_swapper(): #age vorodi func e bala ro bezari into error mide!
    global my_color
    global neighbor_color
    temp = my_color
    my_color = neighbor_color
    neighbor_color = temp #I can swap them because they are global but it doesnt effect the global var(if you want that you need to use global my_color,)

global_color_swapper() #This function is a bad idea
print("my color is:", my_color) 
print("neighbor's color is:", neighbor_color)



################################################## Review

####################### 1

def volume(width,length,height):
    return width*length*height

####################### 2
def volume2(width,length,height=1):
    return width*length*height

####################### 3
import datetime
#dir(datetime)
#dir(datetime.datetime)
#help(datetime.datetime.today)
print(datetime.datetime.today())
print(datetime.datetime.now())