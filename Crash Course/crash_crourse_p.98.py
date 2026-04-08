squares = []
for i in range(0, 10):
    square = i ** 2
    squares.append(square)
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

squares = [i ** 2 for i in range(1,10)]
print(squares)

# ex. 4-3/98
twenty = []
for i in range(0,21):
    print(i)

# ex. 4-4/98
million = [i for i in range(1000001)]
print(million)

# ex. 4-5/98
min(million)
max(million)
sum(million)


# ex. 4-6/98
odds = [print(i) for i in range(1, 20, 2)]

# ex. 4-7/98
three = [i for i in range(3, 31, 3)]
for i in three:
    print(i)
print(three)

# ex. 4-8/98
cubes = []
for i in range(1,11):
    cubes.append(i**3)
    print(i**3)

# ex. 4-9/98
cubes = [i**3 for i in range(1,11)]
for i in cubes:
    print(i)
print(cubes)


# slicing a list
players = ['au', 'bb', 'ct', 'dn', 'em']
print(players[0:3])
print(players)
print(players[:4])
print(players[3:])

# looping through a slice
print("Here are the first three players: ")
for player in players[:3]:
    print(player.title())

# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(f"My favourite foods are {my_foods[0]}, {my_foods[1]} and {my_foods[2]} and my friend's favourite foods are {friend_foods[0]}, {friend_foods[1]} and {friend_foods[2]}.")
my_foods.append("vanilla ice cream")
friend_foods.append("cake")
print(my_foods)

# 4-10 slices
new = ["pumpkin soup", "French fries", "quiche"]
my_foods.extend(new)
print(f"The first three items in the list are: {my_foods[0:3]}")
print(f"The three items from the middle of the list are: {my_foods[2:5]}")
print(f"The last three items in the list are: {my_foods[-3:]}")

# 4-11
pizzas = ["Margherita", "Hawajska", "Capriciosa"]
friends_pizzas = pizzas.copy()
pizzas.append("Wiejska")
friends_pizzas.append("4 Fromages")

#sposob1

def formatowanie(lista):
    sformatowane = ""
    for i in lista:
        sformatowane += f"{i}, "
    return sformatowane.rstrip(", ")
   
print(f"My favourite pizzas are: {formatowanie(pizzas)}.")
print(f"My favourite pizzas are: {formatowanie(friends_pizzas)}.")

# sposob2

def printuj_iprintuj(lista):
    print(f"My favourite pizzas are: ")
    for element in lista:
        print(element)
    
printuj_iprintuj(pizzas)
printuj_iprintuj(friends_pizzas)

ulubione = ["Margarita", "Pepperoni", "Capricciosa"]
print("moje ulubione pizze to:")
print(*ulubione, sep='\n')

def drukuj_i_zwracaj(lista):
    wynik = "\n".join(map(str, lista))
    print(wynik)
    return wynik

wynik = drukuj_i_zwracaj(ulubione)
print(f"moje ulubione pizze to:\n{wynik}")

# map(str, lista)  - konwertuje na string kazdy el listy
# "\n".join - laczy te elementy w jeden ciag znakow iddzielajac je nowa linia
# return wynik - zwraca ten sformatowany ciag znakow zeby moc go ponownie wykorzystac


