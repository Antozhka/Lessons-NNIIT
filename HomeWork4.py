#FUNCTIONS

#is_prime
'''def is_prime(x):
    if x < 0 or x >1000:
        print(x,' не число от 0 до 1000')
        return False
    elif x == 0 or x == 1:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

for i in range(-2, 1002):
    if is_prime(i):
        print(i)

#abs
def abs(x):
    if x >=0:
        return x
    else:
        return -x

print(abs(2))
print(abs(-3))

#timeit and wave
def timeit(f):
    from time import time
    def wrap(*arg):
        x = time()
        res = f(*arg)
        print(time()-x)
        return res
    return wrap

@timeit
def wave(s):
    ss = []
    for i in range(len(s)):
        if i==0:
            ss.append(s[0].upper())
        else:
            ss.append(s[0].lower())
        for j in range(1, len(s)):
            if j == i:
                ss[i] += s[j].upper()
            else:
                ss[i] += s[j].lower()
    return ss

print(wave('hElLo'))

#факториал
def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)

print(fact(10))

#CLASSES
# класс прямоугольников и квадратов
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def Sq(self):
        return self.lenght * self.width

    def Per(self):
        return 2 * self.width + 2 * self.lenght


class Square(Rectangle):
    def __init__(self, lenght):
        super().__init__(lenght,lenght)

x = Square(3)
print(x.Sq())
print(x.Per())

#Деньги
class Money:

    def __init__(self,rub,penny):
        self.rub = rub + penny // 100
        self.penny = penny % 100

    def penny_count(self):
        return self.rub * 100 + self.penny

    def __eq__(self, other):
        return self.penny_count() == other.penny_count()

    def __lt__(self, other):
        return self.penny_count() < other.penny_count()

    def __gt__(self, other):
        return self.penny_count() > other.penny_count()

    def __le__(self, other):
        return self.penny_count() <= other.penny_count()

    def __ge__(self, other):
        return self.penny_count() >= other.penny_count()

    def __add__(self, other):
        return Money((self.penny_count()+other.penny_count()) // 100,(self.penny_count()+other.penny_count()) % 100)

    def __sub__(self, other):
        return Money((self.penny_count()-other.penny_count()) // 100,(self.penny_count()-other.penny_count()) % 100)

    def __repr__(self):
        return '{} руб. {} коп.'.format(self.rub, self.penny)

m1 = Money(3, 30) # создаем объект равным 3 рублям и 30 копейкам
print(m1)
penny = m1.penny_count()

print('m1 в копейках равен {}'.format(penny))
# "m1 в копейках равен 330'

print(type(m1))
# <class '__main__.Money'>, а не int!!!

m2 = Money(4, 95)

m3 = m1 + m2

print('Мы получили {}'.format(m3))
# на экране появится "Мы получили 8руб. 25 коп."

if m1 == m2:
    print('{} и {} равны'.format(m1, m2))
elif m1 > m2:
    print('{} больше чем {}'.format(m1, m2))
else:
    print('{} меньше чем {}'.format(m1, m2))'''

#BaseNode
class BaseNode:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        pass

class File(BaseNode):
    def __repr__(self):
        return 'file: "{}"'.format(self.name)

class Dir(BaseNode):
    dir_list = [];

    def add(self,member):
        self.dir_list.append(member)

    def remove(self,member):
        self.dir_list.remove(member)

    def __repr__(self):
        if self.dir_list:
            return 'directory: "{}"{}'.format(self.name, self.dir_list)
#            output = 'directory: "{}"('.format(self.name)
#            for i in self.dir_list:
 #               output += repr(i)
  #          return output + ')'
        else:
            return 'Empty'


d1 = Dir('dir1') # папка на верхнем уровне
d1.add(File('text1.txt'))
d2 = Dir('dir2')
d1.add(d2)
d3 = Dir('dir3')
d1.add(d3)
d1.remove(d3) # пример удаления вложенной структуры
d4 = Dir('dir4')
d2.add(d4)
d4.add(File('image1.txt'))
d4.add(File('text2.txt'))
d1.add(File('paper1.pdf'))
d2.add(Dir('dir5'))
print(d1)
