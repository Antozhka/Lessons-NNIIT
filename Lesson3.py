i=2
print(type(i))
привет=2
from random import randint
print(привет)
n=randint(1,100)
my_list = [1,2,3,4]
for v in my_list:
    print(v)
for i in range(1,20,2):#3 третий аргумент это шаг. Если аргумент только 1, то цикл от нуля
    print(i)


# ФУНКЦИИ
def SummNum(my_list, x=0):
    for v in my_list:
        x += v
    print(x)
    return x
L1 = [1,2,3,4,5,6,7,8,9]
print(SummNum(L1))

res=filter(lambda x: x > 10, [1,19,3,7,28])
print(list(res))

def gt_10(x):
    return x > 10
res=filter(gt_10, [1,19,3,7,28])
print(list(res))

from typing import List
def test(x: List[int]):# подсказка какого типа параметр должен быть
    pass

x = 50
def test():
    global x
    print("1: {}".format(x))
    x = 51
    print("2: {}".format(x))
test()
print("3: {}".format(x))


