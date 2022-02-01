# https://www.hackerrank.com/challenges/write-a-function/problem





def find_leap_year(year):
    if year%4 == 0 and 1900 <= year <= pow(10,5):
        print(True)
    else:
        print(False) 
find_leap_year(int(input()))