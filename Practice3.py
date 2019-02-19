for i in range(1,101):
    if not i%15:
        print('FizzBuzz')
    elif not i%3:
        print('Fizz')
    elif not i%5:
        print('Buzz')
    else:
        print(i)

my_list = [1,2,3,4,5,6,7,8,9]
x=0
for v in my_list:
    x += v
print(x)

x=0
i=0
while i != len(my_list):
    x += my_list[i]
    i += 1
print(x)


#teorema Pifagora
a = 3 # значение первого катета
b = 4 # значение второго катета
c = a * a + b * b
from math import sqrt
c = sqrt(c)
print('Гипотенуза равна {}'.format(c))

#Деление на разряды
print('введите 5и значное число')
input
arr = [0,3,24,2,3,7]
#for i in range(len(arr)-1):
#    for j in range()