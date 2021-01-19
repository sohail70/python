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