################################## Comparisons

########################## 1
import random
def you_won(prices):
    val = random.choice(prices)
    print(val>10)

groceriesPrices = [9.42,5.67,3.25,13.40,7.50]
you_won(groceriesPrices)

########################## 2
favSnack = "MixedNuts"
def snack_check(snack):
    print(snack==favSnack)

snack_check("MixedNuts")



################################## If

######################## 1
def snack_check(snack):
    if snack==favSnack:
        print("That's your favorite snack")
    else:
        print("That's not your favorite snack")

snack_check("tomato")

######################## 2
groceries = ["spinach","carrot","potatoe","MixedNuts","tomato"]
def in_grocery_list(grocery_item):
    if grocery_item in groceries:
        print(grocery_item,"is in",groceries)
    else:
        print(grocery_item,"is not in",groceries)

in_grocery_list("spinach")

######################## 3

def in_grocery_list(grocery_item):
    if type(grocery_item) != str:
        print("Pls give me a string not a",type(grocery_item))
    elif grocery_item in groceries:
        print(grocery_item,"is in",groceries)
    else:
        print(grocery_item,"is not in",groceries)

in_grocery_list(1)

######################## 4
def you_won(prices):
    val = random.choice(prices)
    if val>10 :
        print("You won",abs(val-10),"dollar")
    else:
        print("You didn't win but here is the",abs(val-10),"dollar change")

you_won(groceriesPrices)

######################## 5


def curTime():
    import datetime
    t = datetime.datetime.now().time()
    if t.hour > 9 & t.hour<10:
        print("Morning lecture time!")
    elif t.hour >= 0 & t.hour <= 7:
        print("You should be sleep right now")

curTime()  


################################## While

###################### 1
i=0
while i<10:
    print(favSnack)
    i+=1

###################### 2
i=0
while i<10:
    print( (favSnack+" ")*i)
    i+=1

###################### 3

i=0 
while i<10:
    print((favSnack+" ")*10,end="")
    i+=1



################################## For

##################### 1

for ch in "blood-oxygenation level dependent functional magnetic resonance imaging":
    print(ch)

##################### 2
print("Note to self, buy:")
for i in groceries:
    print(i)

#################### 3
j=0
for i in groceries:
    print(j,i)
    j+=1

#################### 4

print("Note to self, buy:")
for i in groceries:
    print(i)
    if i==favSnack:
        break

#################### 5
st = "blood-oxygenation level dependent functional magnetic resonance imaging"
for i in st.split():
    print(i)


################################## For range

################## 1

for i in range(len(groceries)):
    print(i,groceries[i])

################## 2

for (i,j) in enumerate(groceries):
    print(i,j)

################## 3

for i in range(10):
    print(favSnack)

################## 4

i=0
j=100
guess =  random.randint(i,j)

while True:
    userGuess = input("Guess a number between "+"["+str(i)+","+str(j)+"]"+":")
    try:
        userGuess = int(userGuess)
    except:
        print("That's not a number")
        continue

    if userGuess==guess:
       print("You Won")
       break
    elif userGuess<guess:
        print("Go higher")
        i=userGuess
    else:
        print("Go lower")
        j=userGuess