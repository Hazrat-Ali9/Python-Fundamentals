# Loops: while and for loop

# for loop
from pprint import pprint
evens = range(0,101,2)
odds = range(1, 101, 2)
print(list(evens), list(odds))

# add all numbers from 0 to 100
total = 0
for num in range(101):
    total = total + num
print(total)

a = 0
while a < 11:
    print(a)
    a = a + 1

for i in range(11):
    print(f'{i} x {i} = {i * i}')


countries = ['Germany', 'America', 'France', 'Spain', 'Russia']

lst_lst = []
for c in countries:
    lst_lst.append([c, c.upper(), len(c), c.upper()[:3]])
pprint(lst_lst)

first_name = 'Hazrat'
last_name = 'Ali'
age = 24
full_name = first_name + ' ' + last_name
# I am Hazrat Ali. I am 24 years old. 
print('I am ' + full_name + '. ' + 'I am ' + str(age) + ' years old.')

a = 1000
b = 200

print(f'{a} x {b} = {a * b}')

for c in countries:
    print(f'I live in {c}. {c} is a very beautiful country.')


