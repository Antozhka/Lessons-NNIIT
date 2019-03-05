def fizzbuzz(x):
    res = []
    for y in x:
        if not y % 15:
            res.append('FizzBuzz')
        elif not y % 5:
            res.append('Buzz')
        elif not y % 3:
            res.append('Fizz')
        else:
            res.append(y)
    return res



class NonValidInput(Exception):
    pass

def to_roman(x):
    d = ['I','V','X','L','C','D','M','N']
    res=[]
    if type(x) != int or x <= 0 or x > 5000:
        raise NonValidInput()
    for i in range(4):
        y = (x % (10 ** (i+1))) // (10 ** i)
        z = y % 5
        if z < 4:
            for j in range(z):
                res.insert(0, d[2 * i])
            if y >= 5:
                res.insert(0, d[2 * i + 1])
        if y == 4:
            res.insert(0, d[2 * i + 1])
            res.insert(0, d[2 * i])
        if y == 9:
            res.insert(0, d[2 * i + 2])
            res.insert(0, d[2 * i])
    return ''.join(res)