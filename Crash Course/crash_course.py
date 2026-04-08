# str 56
message = 'this is a string'
print(message)

message = 'this is also a string'
print(message)

#str 59
first_name = 'alice'
last_name = 'wonderland'
full_name = f'{first_name} {last_name}'
print(full_name)

print(f"Hello, {full_name.title()}!")

lan = ' Python '
print(lan.rstrip())

#str 61
url = 'https://ec.europa.eu/taxation_customs/vies/#/vat-validation-result'
print(url.removeprefix('https://'))

str = '-'.join('hello')
print(str)

n = input('Jak sie nazywasz ?')
my_name = 'Emilia'
answer_1 = 'Czesc Emilia'
answer_2 = f'{n.title()}! Milo mi Cie poznac'
if n == my_name :
 print(answer_1)
else:
 print(answer_2)


 w = float(input('Podaj swoja wage w kilogramach:'))
 h = float(input('Podaj swoj wzrost w metrach:'))
 bmi = w/(h**2)
 print(f'Twoje BMI wynosi: {round(bmi, 2)}.')


 #kalkulator kola

promien = float(input('Podaj promien kola w cm:'))
if promien < 0:
 print('Pamietaj, ze promien musi byc dodatni!')
else:
 print(f'Pole kola wynosi {3.14*(promien**2)} cm2')
 print(f'Obwod kola wynosi {2*3.14*promien}')