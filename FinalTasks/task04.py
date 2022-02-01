# https://www.hackerrank.com/challenges/python-loops/problem


def loop_nams_pow(n):
    if 1 <= n <= 20:
        for i in range(0,n):
            pow_num = pow(i,2)
            print(pow_num)
loop_nams_pow(int(input()))