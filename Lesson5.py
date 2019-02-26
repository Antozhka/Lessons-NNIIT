################################################
def my_len(l):
    x = 0
    for i in l:
        x += 1
    return x


print(my_len([0, 'k', [3,4]]))


def my_reversed(l):
    return l[::-1]


print(my_reversed([1, 2, 3]))


def my_range(stop, start=0, step=1):
    l = [start]
    i = start + step
    if step > 0:
        while i < stop:
            l.append(i)
            i += step
    else:
        while i > stop:
            l.append(i)
            i += step
    return l


print(my_range(5))


#######################COORDINATES
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def quadr_num(self):
        if self.x >= 0:
            if self.y >=0:
                return 1
            else:
                return 4
        else:
            if self.y >=0:
                return 2
            else:
                return 3

    def vector_length(self):
        return (self.y ** 2 + self.x ** 2) ** 0.5


a = Coordinate(0, 5)
print(a.quadr_num())
print(a.vector_length())


###############################
def to_title(s):
    s1 = s[0].upper()
    for i in range(len(s)-1):
        if s[i] == ' ' and s[i+1] != ' ':
            s1 += s[i+1].upper()
        else:
            s1 += s[i+1]
    return s1

print(to_title('гаштури антон петрович'))


def count_simbol(s, simb):
    i = 0
    for x in s:
        if x == simb:
            i += 1
    return i


print(count_simbol('гаштури антон петрович', 'т'))


def my_format(s,*args):
    arg = []
    s1 = []
    index = 0
    for i in args:
        arg.append(i)
    j=0
    while j < (len(s)-1):
        if s[j] == '{' and s[j+1] == '}':
            s1.append(str(arg[index]))
            index += 1
            j += 2
        else:
            s1.append(s[j])
            j+=1
    if s[len(s)-2] != '{':
        s1.append(s[len(s)-1])
    s2 = s1[0]
    for j in range(len(s1)-1):
        s2 += s1[j+1]
    return s2


print(my_format("My name is {}, I'm {} years old", 'Anton', 35))


#######################CLASS STORAGE
class Storage:
    def __init__(self, path):
        self.path = path

    def read_data(self):
        f=open(self.path, 'r')
        d=f.read()
        x = d.split('*br*')
        f.close()
        return x

    def save_new(self, data):
        f=open(self.path, 'a')
        f.write(data)
        f.write('*br*')
        f.close()

    def get_size(self):
        from os.path import getsize
        return getsize(self.path)


x = Storage('name.txt')
x.save_new('гаштури')
x.save_new('антон')
x.save_new('петрович')
print(x.read_data())
print(x.get_size())


#####################COPYFILE & COPYDIR
def copyfile(path1, path2):
    from os.path import exists
    if exists(path1):
        f1 = open(path1, 'rb')
        info = f1.read()
        f1.close()
        if exists(path2):
            print('ошибка: файл назначения существует')
        else:
            f2 = open(path2, 'wb')
            f2.write(info)
            f2.close()
    else:
        print('ошибка: файл источника не существует')


copyfile('name.txt', 'E:\\namecopy.txt')


def copydir(path1, path2):
    from os import listdir
    from os import mkdir
    from os.path import exists
    from os.path import abspath
    if exists(path1) and not exists(path2):
        mkdir(path2)
        for p in listdir(path1):
            copyfile(path1+'\\'+p, path2+'\\'+p)
    elif not exists(path1):
        print('ошибка: директории источника не существует')
    else:
        print('ошибка: директория назначения уже существует')


copydir('E:\\1', 'E:\\2')


#SHEDULER
'''class Sheduler:
    func = []
    period = []
    def __init__(self, runtime):
        self.runtime = runtime

    def add_func(self, func, period):
        self.func.append(func)
        self.period.append(period)

    def run(self):
        pass'''


#ЗЫ: к вопросу про ПРОСТЫЕ ЧИСЛА (первый вариант имеет сложность о(n) (даже если сократить вдвое цикл) для простых чисел, второй - о(n**0.5))
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

def is_prime_adv(x):
    if x < 0 or x >1000:
        print(x,' не число от 0 до 1000')
        return False
    elif x == 0 or x == 1:
        return False
    else:
        i = 2
        j = x
        while i < j:
            if x % i == 0:
                return False
            i += 1
            y = x // i + 1
        return True

for i in range(-2, 1002):
    if is_prime(i) or is_prime_adv(i):
        print(i,is_prime(i),is_prime_adv(i))'''#проверяем, что обе ф-ии дают один результат


