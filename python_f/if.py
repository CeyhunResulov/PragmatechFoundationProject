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



# a=input()
# b=input()
# # c=pow(a,b)
# x=input(f'numbers:{a} {b}')
# y=input(f'netice: {a} ustu {b} {pow(a,b)}-dir')


# print(x)
# print(y)