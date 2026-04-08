list = ['dog', 'turtle', 'cat']
for i in list: 
    print(f'A {i} would make a great pet.')
print("Any of these animals would live in the zoo.")

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6]
min(digits)
max(digits)
sum(digits)


squares = [value**2 for value in range(1,11)]
print(squares)