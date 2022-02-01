# https://www.hackerrank.com/challenges/python-loops/problem


def print_nums_line(n):
    c = ''
    if 1  <= n <= 150:
        for i in range(1,n+1):
            c += str(i)
    print(c)
print_nums_line(int(input()))
