# https://www.hackerrank.com/challenges/py-if-else/problem


def tocomparenums(n):
    if n%2 != 0:
        print('weird')
    elif n%2 == 0 and 2<n<5:
        print('NOT weird')
    elif n%2 == 0 and 6<n<20:
        print('weird')
    elif n%2 == 0 and n > 20:
        print('NOT weird')
    else:
        print('hec bir sert odenmir!')
tocomparenums(int(input()))






2.