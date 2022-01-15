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


# 1. Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

# a=int(input("firstnum:"))
# b=int(input("secondnum:"))
# c=int(input("thirdnum:"))
# d=int(input("fourthnum:"))
# if a==b==c==d:
#     print("kavadratin sahesi:",a*b)
# else:
#     print("ededlerin cemi:",a+b+c+d)



# 2. Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
# a=[int(input('fnum:')), int(input('snum:')), int(input('thnum:')), int(input('fthnum:'))]
# print('maksimum eded:',max(a))




# 3. Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin 
# və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). 
# Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.


# print(input("meyveler menyusu: alma, gilas, armud, heyva, alca"))
# meyveler=['alma', 'gilas', 'armud', 'heyva', 'alca']
# qiymetler=['2 azn', '5 azn', '3 azn', '4 azn', '7 azn']
# meyve=input('secim: ' )

# if meyve in meyveler:
#     qiymet=qiymetler[meyveler.index(meyve)]
#     print('qiymet: ',qiymet)
# else:
#     print('ERROR')





# 4. Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə,
#  soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin.
#  Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın,
#  tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır.
#  Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə,
#  Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. 
# Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə,
#  hər verdiyibiz şərtə uyğun error tipli mesaj verin.
#  Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin.
#  ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789
#  ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.


ad=input('adinizi daxil edin:')
if 3<=len(ad)<=11:
    soyad=input('soyadinizi daxil edin:')       
    if 5<=len(soyad)<=15:
            il=input('dogum ilinizi daxil edin:')
            if len(il)==4:
                email=input('email daxil edin:')
                if 10<=len(email)<=22:
                    spl=email.split('@')
                    if spl[1]=='gmail.com':
                        parol=input('parol daxil edin:')                 
                        if 6<=len(parol)<=13:
                            tesdiq=input('parolu tesdiqleyin:')
                            if tesdiq==parol:
                                print("qydiyyat tamamlandi")
                                sual=input('qeydiyyatin detallari gosterilsinmi?')
                                if sual=='he':
                                    print(f'Ad:{ad} Soyad:{soyad} il:{il} Email:{email} Parol:{parol}')
                                
                                elif sual=='yox':
                                    print(f'{ad}, ugurlar!')                    
                            else:
                                print('parolu duzgun tesdiq edin!')        
                        else:
                            print('parolun simvol sayi duzgun deyil') 
                    else:
                        print('emailin sonunda @gmail.com yazilmalidir!')                        
                else:
                    print("email simvol sayi duzgun deyil") 
            else:
                print("il daxil ederken simvol sayi 4 olmalidir")
    else:
            print("soyad simvol sayi 5-15 araliginda olmalidir")
else:
    print('ad simvol sayi 3-11 araliginda olmalidir')                               





