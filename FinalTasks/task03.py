# https://www.hackerrank.com/challenges/python-division/problem


def intandfloat(a,b):
    integer_calc = a/b
    float_calc = a/b
    print(int(integer_calc),float(float_calc), sep='\n')
intandfloat(int(input('a=')), int(input('b=')))