# https://www.hackerrank.com/challenges/python-string-split-and-join/problem





def SplitAndJoin(n):
    n = n.split(' ')
    new_text = '-'.join(n)
    print(new_text)
SplitAndJoin(input())
