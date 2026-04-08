names = ["Ania", "Weronika", "Aneta", "Paula", "Andrzej"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

def greeting(name):
    print(f'Hello {name}, have a nice day!')
    return greeting

greeting(names[0])
greeting(names[3])
greeting(names[2])
greeting(names[4])

transport_list = ["train", "car", "bike", "longboard"]
print(f'I love riding the Pendolino {transport_list[0]}.')
print(f'I love riding my old Augustina {transport_list[2]}.')
print(f'I love to ride my {transport_list[-1]}, even if I often fall off.')