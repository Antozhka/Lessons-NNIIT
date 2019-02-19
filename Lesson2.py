print('Начнем урок')
weight = 70
high = 176
name = 'Anton'
print(name)
man = (name, weight, high)
print (man)
x=3
y=x
x+=1
print(x)#Выведет разные числа, потому что
print(y)#целые - неизменяемые объекты
x = y = [1, 2, 3]
x.append(1)
print(x)#выведет одно и тоже
print(y)#
print(not True)
print(bool(""))
import math
x = (7, 3, 10)
print(type(x))
x='qwerty'
print(x[-2])
user = {
'name': 'Олег',
    'email': 'oleg@example.com',
    'address': {
        'city': 'Москва',
        'street': 'Тверская'

    },
    'hobby': ['рисование', 'пение']
}
l=user.get('hobby',[])
for i,v in enumerate(l):
    if v=='пение':
        l[i]='песни'
        break
print(user['hobby'])
