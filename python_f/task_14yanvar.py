# 1.  Siyahının tək elementlərini seçmək üçün Python proqramı yazın.

# def odd(my_list):
#     tek=[]
#     for i in my_list:
#         if i%2!=0:
#             tek.append(i)
#     print(tek)
# odd([1, 3 , 8, 28, 39,107])




# 2. Siyahıdakı bütün ededleri cəmləmək üçün Python funksiyasını yazın.

# def sum(my_list):
#     cem=0
#     for i in my_list:
#         cem+=i
#     print(cem)
# sum([4, 2, 5, 7])




# 3. Sample List : (8, 2, 3, 0, 7) Expected Output : 20

# def sum(my_list):
#     cem=0
#     for i in my_list:
#         cem+=i
#     print('netice:',cem)
# sum((8, 2, 3, 0, 7))




# 4. Siyahıdakı bütün ədədləri vurmaq üçün Python funksiyasını yazın.

# def vurma(my_list):
#     vur=1
#     for i in my_list:
#         vur=vur*i
#     print(vur)
#vurma((1, 3, 4, 8, 10))





# 5. returnDay adlı funksiyanı yazın. Bu funksiya bir parametr götürür (1-7 arası rəqəm) və
#  həftənin gününü qaytarır (1 bazar, 2 bazar ertəsi və s.). Rəqəm 1-dən kiçik və ya 7-dən böyükdürsə, funksiya Yox qaytarmalıdır.
 


# def returnDay(day):
#     if 1<=day<=7:
#         if day==1:
#                 print(f'{day} bazarertesi')
#         if day==2:
#                 print(f'{day} cersenbe axsami')
#         if day==3:
#                 print(f'{day} cersenbe')
#         if day==4:
#                 print(f'{day} cume axsami')
#         if day==5:
#                 print(f'{day} cume')
#         if day==6:
#                 print(f'{day} senbe')
#         if day==7:
#                 print(f'{day} bazar')
#     else:
#             print('YOX!')
# returnDay(int(input('gun daxil et:')))





# 6. 'admin' adı da daxil olmaqla beş və ya daha çox istifadəçi adının siyahısını tərtib edin. 
# Təsəvvür edin ki, hər bir istifadəçi vebsayta daxil olduqdan sonra ona salam yazacaq kod yazırsınız. 
# Siyahıda dövr edin və hər bir istifadəçi üçün salamı çap edin: • İstifadəçi adı 'admin'dirsə, salam admin kimi xüsusi salamı çap edin, 
# status hesabatını görmək istərdinizmi? • Əks halda, Salam Eric kimi ümumi salamı çap edin, yenidən daxil olduğunuz üçün təşəkkür edirik.


# def inputsite(*username):
#     for i in username:
#         if i=='ceyhun':
#             print(f'salam admin.Status hesabatını görmək istərdinizmi?')
#         if i=='ferhad':
#             print(f'salam {i}.yenidən daxil olduğunuz üçün təşəkkür edirik.')
#         if i=='resad':
#             print(f'salam {i}.yenidən daxil olduğunuz üçün təşəkkür edirik.')
#         if i=='hezret':
#             print(f'salam {i}.yenidən daxil olduğunuz üçün təşəkkür edirik.')
#         if i=='asif':
#             print(f'salam {i}.yenidən daxil olduğunuz üçün təşəkkür edirik.')
       
# inputsite(input('username: '))




# 7. dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#  Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin. Bunun ucun userden input alin.
#  Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki user ne sorushmaq isteyir.
#  Meselen born ve when sozleri varsa cumlede user cox guman ki “When was Plato born?” sualina cavab axtarir. 
# Proqram o sozleri gorub sorushsun ki, “Maybe did you mean “When was Plato born?” “. Bu suali sorushduqda yes ve no secimleri verin. 
# Eger yes yazsa dictionarydeki datadan istifade ederek Platonun doguldugu ili usere gosterin.
# Meselen country daxil etse proqram texmin etsin ki user platonun doguldugu yeri axtarir ve siz de ele proqram yazin ki ona uygun cavab qaytarin.
#  Eger mentiqsiz soz daxil edilse not found verin ekrana.
# dict={"ad": "Platon", "olke": "Ancient Greece", "il": -427, "muellim": "Sokrat", "telebe": "Aristotel"}
# user=input('sual:')
# if user=='ad':
#     a=input('Bəlkə “Platonun adi nedir?” demək istəyirdiniz?')
#     if a=='he':
#         print(dict["ad"])
#     else:
#         print('tapilmadi')
# if user=='olke':
#     a=input('Bəlkə “Platon hansi olkede dogulub?” demək istəyirdiniz?')
#     if a=='he':
#         print(dict["olke"])
#     else:
#         print('tapilmadi')
# if user=='il':
#     a=input('Bəlkə “Platon necenci ilde dogulub demek isteyirdiniz?” demək istəyirdiniz?')
#     if a=='he':
#         print(dict["il"])
#     else:
#         print('tapilmadi')
# if user=='muellim':
#     a=input('Bəlkə “Platonun muellimi kim olub demek isteyirdiniz?” demək istəyirdiniz?')
#     if a=='he':
#         print(dict["muellim"])
#     else:
#         print('tapilmadi')
# if user=='telebe':
#     a=input('Bəlkə “Platonun telebesi kim olub demek isteyirdiniz?” demək istəyirdiniz?')
#     if a=='he':
#         print(dict["telebe"])
#     else:
#         print('tapilmadi')
        





# 8. len() funksiyasini ozunuz yazmaga calishin.

# my_list=[9, 1, 3,'ceyhun', True, False,[1234,'sasfaf'], 123]
# _len=0
# for i in my_list:
#     _len+=1
# print(_len)



# 9. funksiya yazin ededlerden ibaret list qebul etsin ve eger listin birinci ve sonuncu elementleri beraberdise return True qaytarsin.
#  Mes: [1,2,3,1] bu halda True qaytaracag



# def sertiyoxla(my_list):
#     if my_list[0]==my_list[len(my_list)-1]:
#         return True
#     return 'birinci ve sonuncu element beraber deyil'
# print(sertiyoxla([5,'ceyhun',3, True,5]))




# 10. Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki reqemler dictioneryde yoxdusa onlari silmelidi ve
#  sonda listi return etmelidi. (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.


def dictandlist(_list, dict):
    a=[]
    for i in range(0,len(_list)-1):
        if _list[i]==dict:
            a.append(_list[i])

    print(a)
print(dictandlist([17, 23, 35], {"tural": 17,"soltan": 35}))
    


# a={"tural": 17,"soltan": 35}
# x=a.values()
# print(x)

