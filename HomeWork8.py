import threading
import multiprocessing
import time

def odd_primes(end, begin = 3):
    res = [2, 3]
    for j in range(begin+1,end+1):
        stop = j ** 0.5 # дальше можно не искать делители
        for i in res: # перебирать делители только из простых чисел
            if j % i == 0:
                break
            if i > stop:
                res.append(j)
                break
    res.remove(2)
    return res

start = time.time()

odd_primes(10000)
odd_primes(20000, 10001)
odd_primes(30000, 20001)

print('Общее время вычислений в милисекундах: {}'.format(round((time.time() - start)*1000)))


start = time.time()
threads = []
thr = threading.Thread(target=odd_primes, args=(10000, 3))
thr.start()
threads.append(thr)

thr = threading.Thread(target=odd_primes, args=(20000, 10001))
thr.start()
threads.append(thr)

thr = threading.Thread(target=odd_primes, args=(30000, 20001))
thr.start()
threads.append(thr)

for thr in threads:
    thr.join()
print('Общее время вычислений в милисекундах: {}'.format(round((time.time() - start)*1000)))

'''start = time.time()
processes = []
prc = multiprocessing.Process(target=odd_primes, args=(10000, 3))
processes.append(prc)
prc.start()

prc = multiprocessing.Process(target=odd_primes, args=(20000, 10001))
processes.append(prc)
prc.start()

prc = multiprocessing.Process(target=odd_primes, args=(30000, 20001))
processes.append(prc)
prc.start()

for prc in processes:
    prc.join()
print('Общее время вычислений в милисекундах: {}'.format(round((time.time() - start)*1000)))

'''

#Шифр Цезаря

def cezar(phrase, key):
    alphabeth = 'a b c d e f g h i j k l m n o p q r s t u v w x w z'
    alph_new = alphabeth.split(' ')
    res = []
    for i in range(key):
        alph_new.append(alph_new[i])
    for s in phrase:
        if s.isalpha() and s.islower():
            res.append(alph_new[alph_new.index(s)+key])
        elif s.isalpha() and s.isupper():
            res.append(alph_new[alph_new.index(s.lower())+key].upper())
        else:
            res.append(s)
    return ''.join(res)

print(cezar('Anton Gashturi', -3))