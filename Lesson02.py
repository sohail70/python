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
    