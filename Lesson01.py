############################ 1
item1 = "apple"
item2 = "orange"
item3 = "banana"
item4 = "peach"
item5 = "cherries"
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)
############################ 2-3
cost1 = 9.42
cost2 = 5.67
cost3 = 3.25
cost4 = 13.40
cost5 = 7.50

cardinality1 =1
cardinality2 =1
cardinality3 =1
cardinality4 =1
cardinality5 =5
wholeCost = (cardinality1 * cost1
            +cardinality2 * cost2 
            +cardinality3 * cost3
            +cardinality4 * cost4
            +cardinality5 * cost5)
print(wholeCost)
################################ 4

string1 = "blood-oxygenation level dependent functional magnetic resonance imaging"
print(len(string1))


################################ 5

#String class methods
favSnack = "MixedNuts "
print(favSnack*100 )

################################ 6
print("\n")
str1 = "soheil.e.nia@gmail.com"
str2 = str1.partition("@") #strings are immuatables hence you need to declare str2
#partition -> 3 parted tuple 

print(str2) #('soheil.e.nia', '@', 'gmail.com') 


print("My name is {1} and I'm an {0}".format("engineer","sohail")) #My name is sohail and I'm an engineer
print("My name is {name} and I'm an {major}".format(major = "engineer",name = "sohail"))

print("I'm gonna be a data scientist really soon".split()) #["I'm", 'gonna', 'be', 'a', 'data', 'scientist', 'really', 'soon']

print("Working with strings is a lot o fun".find("fun")) #32
print("Working with strings is a lot o fun".find("f")) #32

print("Working with strings is a lot o fun".index("f")) #32, The same as find but it gives an execption


print ("I like Soheil".replace("soheil","people"))
print ("I like Soheil".replace("Soheil","people")) #Tiny things matter!
print ("I like Soheil".replace("i","I"))

print (" ".join(["I" , "am" , "ok"])) #dict
print (",".join("abcdefg")) #string
print(" ".join(("I","am","ok"))) # tuple 

print("is is here is is".count("is"))
print("is is here is is".count("is",2)) #from position 2 to end
print("is is here is is".count("is",3,6)) #from position 3 to 6

#####################################7
print(item1,item2,item3,item4,item5)
