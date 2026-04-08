name = 'Eric'
print(f'Hello {name}, would you like to learn some Python today?')

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.casefold())

famous_person = 'The Little Prince'
print(f'''{famous_person} once said, "It is only with the heart that one can see rightly; 
what is essential is invisible to the eye."''')

name = '   \t Johan    \n Johannssonn   '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.replace('\n', '').strip().replace('\t', '').replace('    ', ''))

filename = 'python_course.txt'
print(filename.removesuffix('.txt'))

print(5+3)
print(12-4)
print(2*4)
print(int(16/2))


def favnumb():
    while True:
        try: 
            favourite_number = int(input("What's your favourite number?"))
            break
        except:
            print("It's not a number.")
            continue
    return f'Yey your favourite number is {favourite_number}'
print(favnumb())

import this

    