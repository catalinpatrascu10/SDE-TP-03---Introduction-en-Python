# liste qui contient 5 noms de fruits
fruits = ["Apple", "AliApricots", "Banana","Blueberries","Cherry"]

# Trier cette liste alphabétiquement
fruits.sort()




# afficher chaque nom avec sa longueur

print("The lentgh of the list is: " + str(length))
lengths = [len(i) for i in fruits[:5]]
print(lengths)

# ajoutez 3 noms de couleurs a cette liste
fruits.append("Blue")
fruits.append("Red")
fruits.append("Green")
print(fruits)

# inverser les éléments et affichez la liste
fruits.reverse()
print(fruits)