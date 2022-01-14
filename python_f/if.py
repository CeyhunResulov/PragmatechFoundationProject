# # 1.Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin
# task='Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin'
# print(task)



# 2.ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. 
# Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.

# ad='ceyhun'
# soyad='resulov'
# tam_ad=f'salam,{ad.title()} {soyad.title()}!'
# print(tam_ad)




# 3.sep parametrindən istifadə edərək 4 müxtəlif şəhər adını * işarəsi ilə ayırın

# print('baki', 'gence', 'lenkeran', 'sumqayit',sep='*')




# 4. “Macarıstan” sözünü tərsinə çapa verin


# a="Macarıstan"
# print(a[::-1])




# 5.Bir sətir koddan istifadə edərək aşağıdakı yazını göründüyü kimi çapa verin. Languages: Python C JavaScript


# print('Languages: Python C JavaScript')




# 6.istenilen bir mətnin tam yarısını çap edin.



# x='istenilen bir mətnin tam yarısını çap edin.'

# print(x[0:(int(len(x)/2)+1)])






# 7.  x = 10, y = 55 “and”-dən istifadə edərək x və y müqayisə edərək boolen dəyərləri çapa verin.

# x=10
# y=55
# z=33
# # print(x>y and z<y)  false
# print(x<z and y>x) true




# 8. inputdan boshluqla ayrilmish iki eded daxil edin. Birinci ededi ikinci eded qeder quvvete yukseldin ve 
# ashagidaki kimi ekrana yazdirin (f stringden istifade ederek)

# Ededleri daxil edin: 2 5

# Netice: 2 üstü 5 32-dir.



# x=input('numbers:')
# y=x.split()
# z=int(y[0]) ** int(y[1])
# print(input(f'netice: {y[0]} ustu {y[1]} {z}-dir'))




# 9. word = “istədiyiniz sözü yaza bilərsiz” məsələn word = ‘culture’ 
# “Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"cüməsini bir dəyişkənə mənimsədin və
#  həmin dəyişkəndə saxlayın və word-ə verdiyiniz sözün bu dəyişkəndə olub-olmamasını yoxlayın.
#  Əgər söz varsa, ekranda belə bir nəticə çıxarın; “Culture” sözü mətndə var. Əgər yoxdursa, “Not found” çapa verin.



# txt="""Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"""
# word=input('soz daxil et: ')


# if word in txt:
#     print(f"bu metmde {word} sozu var")

# else:
#     print('NOT FOUND')



# 10. 65 ədədinin 22 ədədinə olan qalığı ilə nisbətinin hasilini çapa verin.


# a=65
# b=22
# c=(a%b)*(int(a/b))
# print(c)





# 11. x-ə istənilən bir ədəd mənimsədin, sonra isə şərt verərək yoxlayın. X 10-dan böyükdürsə və cüt ədədirsə,
#  ekrana “OKAY” yazılsın, əgər yuxarıdakı iki şərtdən biri ödənirsə “NOT OKAY” yazılsın, heç bir şərt ödənməzsə, “BAD” yazılsın


# x=7
# if x>10 and x%2==0:
#     print("OKAY")
# elif x>10 or x%2==0:
#     print('NOT OKAY')

# else:
#     print('BAD')   
     






#  12. iki ədəd götürüb dəyişkənlərə mənimsədin.
#  Əgər ədələrin fərqi bir-birlərinə olan nisbətin tam hissəsindən böyükdürsə, ekrana “Greater”, 
# bərabərdirsə, “EQUAL” 
# yox əgər kiçikdirsə, “SMALLER” yazılsın.



# a=12
# b=8
# ferq=a-b
# nisbet=int(a/b)
# if ferq > nisbet:

#  print('GREATER')

# elif ferq==nisbet:
#     print('EQUAL')

# elif ferq<nisbet:
#     print('SMALLER')






# 13. String data tipi yaradın və dəyərini 5.567-yə bərabər edin. Sonra bu dəyişkənin dəyərin 10- luqlara qədər yuvarlaqlaşdırın.



# a='5.567'

# b=float(a)

# print(b)






# 17. x = “5.89” stringinin tam hissəsinin kubunu tapın.
# x=5.89
# y=int(float(x))
# kub=pow(y,3)
# print(kub)




# yeni tapsiriqlar


# 1.





# 2. Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.


a=5
b=8
c=10
d=15