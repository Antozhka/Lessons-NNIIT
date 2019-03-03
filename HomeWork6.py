from itertools import chain
print(list(chain([1, 2, 3], [4, 5], [6, 7])))

from itertools import filterfalse
print(list(filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])))

def count_digits(num):
    x = str(num)
    res=0
    for i in x:
        res += int(i)
    return res

print(count_digits(126))

def count_words(list_of_words):
    res=0
    for i in range(len(list_of_words)):
        sign = True
        for j in range(i+1, len(list_of_words)):
            if list_of_words[i] == list_of_words[j]:
                sign = False
                break
        if sign:
            res += 1
    return res

list_of_strings = ['hello', 'hi', 'hello', 'goodbye', 'chao', 'hi']
result_number = count_words(list_of_strings)
print(result_number)

