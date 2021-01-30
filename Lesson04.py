############################## 1
a = [i for i in range(1000) if (i%3==0 or i%5==0)]
print (sum(a))

############################## 2
a1=[2,2,2,2,2,3,3,3,3] # a is just pointing to this (mutable) list as opposed to a=4 ,a+=1 which at first "a" points to 4 (integers are immutable) and then "a" points to 6 (numbers can't change bc they are immutables but "a" can point to another number! like 5 )
# but in the above list "a" is pointing to the list and bc lists are mutables the list it self can change and "a" still point to the same list!
animals1 = ["cow","pig","goat","horse","pig"]
def dupDel(b):
    if type(b)!=list :
        print("Not a good input")
        return
    b[0]=5 #FYI: immutables (including integers, floats, strings, Booleans, and tuples), lists and dictionaries are mutable.
    # That means a global list or dictionary can be changed even when it’s used inside of a function
    b=set(b)
    return list(b)

c = dupDel(a1)
print(c)
print(a1) #a changed! in the function because lists are mutable
# good info here: https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/#:~:text=This%20is%20because%20Python%20stores,function%2C%20where%20it%20is%20isolated.
print(dupDel(animals1), end="\n\n")




a2=[2,2,2,2,2,3,3,3,3] # a is just pointing to this (mutable) list as opposed to a=4 ,a+=1 which at first "a" points to 4 (integers are immutable) and then "a" points to 6 (numbers can't change bc they are immutables but "a" can point to another number! like 5 )
# but in the above list "a" is pointing to the list and bc lists are mutables the list it self can change and "a" still point to the same list!
animals2 = ["cow","pig","goat","horse","pig"]
def dupDel2(b): #Another version: preserves the order
    if type(b)!=list :
        print("Not a good input")
        return
    out=[]
    for i in b:
        if i not in out:
            out.append(i)
    return out

d = dupDel2(a2)
print(d)
print(a2)
print(dupDel2(animals2))


############################# 3

def convert_classification(s):
    if s=="U//FOUO":
        return "UNCLASSIFIED//FOR OFICIAL USE ONLY"
    elif s=="S// REL TO USA, FEVY":
        return "SECRET// REL TO USA, FEVY"
    else:
        print("UNKNOWN PORTION MARK")

print(convert_classification("U//FOUO"))