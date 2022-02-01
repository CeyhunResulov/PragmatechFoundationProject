# https://www.hackerrank.com/challenges/python-string-formatting/problem



def show_num_sys(n):
    for i in range(1, n+1):
        if 1 <= n <= 99:
            a=''
            a += str(i)
            a += str(oct(i)).replace('0o','   ')
            a += str(hex(i)).replace('0x','   ')
            a += str(bin(i)).replace('0b','   ')
            print(a)
show_num_sys(int(input()))