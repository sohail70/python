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