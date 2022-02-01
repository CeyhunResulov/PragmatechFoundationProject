# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem



def numscalc(a,b):
    if 1 <= a <= pow(10,10) and 1 <= b <= pow(10,10):
        sum = a+b
        differ = a-b
        product = a*b
        print(sum,differ,product, sep="\n")
    else:
        print('daxil edilen ededler sertleri odemir!')
numscalc(int(input('a=')),int(input('b=')))