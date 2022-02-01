# https://www.hackerrank.com/challenges/py-set-add/problem




def find_different_brand(n):
    brands=[]
    if 0< n <1000:
        for i in range(0, n):
            brand=input('brand:')
            brands.append(brand)
    print('muxtelif markalarin sayi: ',len(set(brands)))
find_different_brand(int(input('umumi markalarin sayi:')))