# 1. Üç müxtəlif a, b, c ədədləri verilmişdir. Onlardan qiymətcə orta olanı tapın.
# Giriş verilənləri
# a, b, c ədədləri mütləq qiymətcə 1000-i aşmayan tam ədədlərdir.


# def edediorta(my_list):
#     orta=(my_list[0]+my_list[1]+my_list[2])/len(my_list)
#     print(orta)
# edediorta([int(input('firstnum:')),int(input('secondnum:')),int(input('thirdnum:'))])





# 2. Tort
# Proqramlaşdırma olimpiadasının ikinci turu bitdikdən sonra olimpiada iştirakçıları bu hadisəni qeyd etmək qərarına gəldilər.
#  Bu məqsədlə düzbucaqlı formada bir böyük tort sifarış verildi. Bu zaman iştirakçıların ətrafına toplaşdıqları masa dairəvi idi.
#  Təbii ki, onlarda sual yarandı: Düzbucaqlı tort masadan qırağa çıxmamaq şərti ilə masaya yerləşəcəkdirmi? Tortun ölçülərini və 
# masanın radiusunu bilərək, bu sualı cavablandırmalısınız.

# Giriş verilənləri
# Üç natural ədəd: masanın r (1 ≤ r ≤ 1000) radiusu, tortun w eni və l uzunluğu (1 ≤ w ≤ l ≤ 1000).

# Çıxış verilənləri
# Tort masaya yerləşirsə YES, əkshalda NO çap edin.

# Giriş verilənləri masanin radiusu=38 tortun eni=40 uzunlugu=60;    Çıxış verilənləri; YES
# Giriş verilənləri 35 20 70;    Çıxış verilənləri;NO

# r=35
# e=20
# u=70
# if r*2>u:
#     print('YES') 
# else:
#     print('NO')







# 3. Heyvanxanada n qəfəs bir sırada düzülmüşdür. Heyvanxanada digər sakinlərlə yanaşı, iki əntər meymun - Slava və Yura da yaşayırdılar.
#  Slava və Yura həmişə yaxşı dost olmuşdular və qonşu qəfəslərdə əyləşirdilər. Lakin indi onlar küsülü idilər və bir-birini görmək istəmirdilər.
#  Heyvanlara qulluq edən baxıcı də onları arzularına uyğun olaraq köçürmək istəyirdi, lakin problem yaranmışdı. 
# Slava və Yura çox savadlı meymunlar idilər (onların hər biri cəmi 8 sinif qurtarmışdı!). Onlar bilmək istəyirdilər ki,
#  onların qəfəslərinin qonşu olmaması üçün neçə köçürmə üsulu var və əlbəttə onların xanaları müxtəlif olmalıdır. 
# Belə hesab etmək olar ki, heyvanxananın digər sakinləri hara lazımdırsa köçürülməyə hazırdırlar, yəni bütün n hücrə əlyetərlidir.

# Heyvanlara qulluq edən əvvəlcə özü bunu hesablamaq istədi, haradasa begemotların ərazisində hesabı itirdi. Tamamilə aydındır ki,
#  sizin köməyiniz olmadan o bunun öhdəsindən gələ bilməyəcək!

# Giriş verilənləri
# Giriş verilənlərin birinci sətrində heyvanxanadakı qəfəslərin sayı olan n (2 ≤ n ≤ 100) ədədi yerləşir.

# Çıxış verilənləri
# Çıxışa bir ədəd - Slava və Yuranın qonşu olmaması üçün müxtəlif qəfəslərə köçürülmə üsullarının sayı verilir.




# qefes=[1, 2, 3, 4]





# 4. m natural ədədi n ədədinin o zaman bərabər böləni adlanır ki, n-nin m-ə bölünməsindən alınan tam və qalıq bərabər olsun. 
# Verilmiş n natural ədədinə görə onun bərabər bölənlərinin sayını tapın.

# Giriş verilənləri

# Müsbət n tam ədədi (1 ≤ n ≤ 106).

# Çıxış verilənləri

# Tələb olunan say.



# n=int(input('bolunen:'))
# m=n
# say=0
# for i in range(1,m):
#     if n%i==int(n/i):
#         say+=1
# print(say)






# 5. Verilmiş hesabi ifadədə toplama (+), çıxma (-) və vurma (*) əməllərinin ümumi sayını müəyyənləşdirin.

# Giriş verilənləri
# Yeganə sətirdə mötərizə və boşluq işarəsi olmayan hesabi ifadə verilir. İfadədə simvolların sayı 250-ni aşmır.

# Çıxış verilənləri
# Yeganə ədəd - göstərilən əməllərin sayı.



hesab=2+3-1*4+9-8+6+3*7
hesab.__str__
# say=0
# for i in hesab:
#     if i=='+':
#         say+=1
#     elif i=='*':
#         say+=1
#     elif i=='-':
#         say+=1


print(hesab)
