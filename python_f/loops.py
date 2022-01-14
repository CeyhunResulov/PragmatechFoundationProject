#  1. Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.
# my_list=[3, 6, 24, 12]
# cem=0
# for i in my_list:
#     cem+=i
# print(cem)




# 2. Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

my_list=[1, 11, 8, 9, 5, 6, 4]
for i in range(len(my_list)):
  
  if my_list[i]>my_list[i+1]:
    print(my_list[i])

