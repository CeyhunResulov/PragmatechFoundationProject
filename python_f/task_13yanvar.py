#  1. Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.
# my_list=[3, 6, 24, 12]
# cem=0
# for i in my_list:
#     cem+=i
# print(cem)




# 2. Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

# my_list=[1, 11, 8, 9, 66, 5, 6, 4, 25]
# my_list.sort()
# print("max:",my_list[len(my_list)-1])
    


# 3. Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.


# my_list=[16, 11, 8, 9, 66, 5, 6, 4, 25]
# my_list.sort()
# print("min:",my_list[0])





# 4. Sətir uzunluğunun 2 və ya daha çox olduğu, 
# ilk və sonuncu simvolun verilmiş sətirlər siyahısından eyni olduğu sətirlərin sayını hesablamaq üçün Python proqramı yazın. 
# Nümunə Siyahısı : ['abc', 'xyz', 'aba', '1221'] Gözlənilən Nəticə : 2
  

# my_list=['abcda', 'xzyx', 'ahg', '232', '123', 'askjskaja', 'aba']
# say=0
# for i in my_list:
#     if i[0]==i[len(i)-1]:
#         new_list=()
#         index=len(new_list)+1
#         say+=index
        
# print('netice:', say)



# 5. list boş olub olmadığını yoxlamaq üçün Python proqramı yazın.




# my_list=[]
# my_list.append('ceyhun')
# if my_list[0]=='ceyhun':
#     print('list bosdur')
# else:
#     print('list bos deyil')







# 6.  my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and 
# last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.



# my_text = "Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."
# a=my_text.split()
# a.sort()
# txt=''
# for i in a:
#     txt=txt+i+' '

# print(txt)




# 7. Siyahının tək elementlərini seçmək üçün Python proqramı yazın.


# my_list=[3, 6, 12, 33, 124, 67, 91,5]
# tek_ededler=[]
# for i in my_list:
#     if i%2!=0:
#         tek_ededler.append(i)
# print('tek ededler:', tek_ededler)
    