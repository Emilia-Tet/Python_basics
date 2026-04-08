#crash course p. 79-80
# dataframe
guest_list = ["John", "Rudolf", "Elsa"]

# function printing an invitation for the person x
def invitation(x):
    print(f"Dear {x}, please be invited for a dinner.")

# ex. 1: printing an invitation for every person from the list
for i in guest_list:
    invitation(i)

# ex. 2: someone can't come, replace him. 
print(f"{guest_list[0]} can't come.")
guest_list[0] = "Olaf"
for i in guest_list:
    invitation(i)

# ex. 3: bigger table
for i in guest_list:
    print(f"Dear {i}, I found a bigger table. Let's meet in a larger groupe.")

guest_list.insert(0, "Amanda")
guest_list.insert(2, "Frog")
guest_list.append("Luke Skywalker")

for i in guest_list:
    invitation(i)

# ex. 4: smaller table
for i in guest_list:
    print(f'''Dear {i}, 
I am extremely sorry.\n The new table won'y arrive on time. I have to cancel our meeting''')

first = guest_list.pop(2)

def anti_invit(y):
    print(f"Dear {y}, I am extremely sorry, but I cannot invite you to my dinner. The table is too small.")

anti_invit(first)

second = guest_list.pop(3)
anti_invit(second)
print(guest_list)

third = guest_list.pop(0)
anti_invit(third)
print(guest_list)

fourth = guest_list.pop(2)
anti_invit(fourth)
print(guest_list)

for i in guest_list:
    invitation(i)

# ex. 5: empty list 
del guest_list[0:2]
print(guest_list)


#sorting & lenght
# 3-8. p. 83

places = ["Japan", "Kalahari", "Finland", "New Zealand", "Morocco"]
print(places)
sorted(places)
print(places)
sorted(places, reverse = True)
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

#3-9 Dinner Guests
len(guest_list)
print(f"Hi, actually I'n inviting {len(guest_list)} people for the dinner.")


#4-1 Pizzas p. 94
pizzas = ['margharita', 'las-pizza', 'goat-cheese']
for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love pizza.")

print(dir(int))

