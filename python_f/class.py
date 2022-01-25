# 1. Bir dənə Restoran classı yaradın. Bu classa init() metdou bu classın adını (restaurant_name) və
#  mətbəx növü (cuisine_type) adlı iki atribitunu saxlamalıdır. 
# describe_restaurant() adlı bir metod yaradın hansı ki restoranın adını və mətbəxin növünü ekrana print etsin.
#  Restoranın açıq olmasını mesaj verən open_restaurant() adlı başqa bit metdi yaradın. 
# Sonra restoran adlı obyekt yaradın bu class-dan və restotanın adını, mətbəxinin növünü, restoran haqqında məlumatları və 
# açıq olmasını çapa verin. Bu Restoran classından daha iki obyek yaradın və describe_restaurant metodunu yeni yaratdığınız hər iki obyekt üçün tətbiq edin.






# from pydoc import describe


# class restorant:
#     def __init__(self,restaurant_name,cuisine_type,info):
#         self.name=restaurant_name
#         self.metbex_novu=cuisine_type
#         self.sual=info

#     def describe_restaurant(self):
#         print(f'resatoranin adi:{restorant_.name}\nmetbex novu:{restorant_.metbex_novu}')
# restorant_=restorant('LEVENGI','cenub metbexi','beli restoran hal hazirda aciqdir')
# restorant_.describe_restaurant()
# restorant_.melumat=input('sualiniz varmi?')
# if 'restoran aciqdirmi' in restorant_.melumat or 'restoran isleyirmi' in restorant_.melumat or 'open' in restorant_.melumat:
#     print(restorant_.sual)



# class restoran(restorant):
#     def __init__(self, restaurant_name, cuisine_type, info,address,menu):
#         super().__init__(restaurant_name, cuisine_type, info)
#         self.yer=address
#         self.esasmenu=menu
# r=restoran('LEVENGI','cenub metbexi','beli restoran hal hazirda aciqdir', 'Lenkeran', 'levengi plov')
# print(r.yer)



# 2. User adlı yeni class yaradın. first_name, last_name və age atributları verin bu class-a.
#  describe_user metdou yaradın user haqqında məlumatları çapa vermək üçün. greet_user adlı başqa bir metod yaradın hansı ki userin ad və
#  soyadına salam verən bir mesaj ekrana yazdırsın. Bir neçə obyekt yaradın bu User class-ndan və hər birinin atribut və metodlarını istifadə edin.
#  Ardinca login_attempts adlı bir atribut verin User classına. increment_ login_attempts adlı metod yaradın hansı ki hər dəfə işə düşəndə login_attempts 1 vahid artırır.
#  reset_login_attempts adlı bir metod yaradın hansı ki login_attemptsləri sıfırlayır. Sonra bir user obyekti yaradın bu class-dan və
#  increment_ login_attemptsi bir neçə dəfə istifadə etdikdən sonra userin neçə dəfə cəhd etdiyini çapa verin. Daha sonra cəhdlərin sayını sıfırlayın və 
# yenidən cəhdlərin sayını çapa verin






# class user:
#     def __init__(self,firstname, lastname, age, login_attemps):
#         self.fname=firstname
#         self.lname=lastname
#         self._age=age
#         self.login=login_attemps

#     def describe_user(self,):
#         return f'ad:{self.fname}\nsoyad:{self.lname}:\nyas:{self._age}'

#     def greet_user(self):
#         return f'salam {self.fname} {self.lname}\n=========================================' 

#     def increment_login_attempts(self):
#         artim=info_ferhad.login
#         artim+=1
#         info_ferhad.login=artim
#         return f'giris cehdiniz:{artim}-dir'

#     def reset_login_attempts(self):
#         info_ferhad.login=0
#         return f'giris cehdleri sifirlandi:{info_ferhad.login}-dir'

# info_ceyhun=user('ceyhun', 'resulov',21,0)
# info_ferhad=user('ferhad', 'salmanov', 20,0)
# print(info_ceyhun.increment_login_attempts())
# print(info_ceyhun.increment_login_attempts())
# print(info_ceyhun.reset_login_attempts())
# print(info_ceyhun.describe_user())
# print(info_ceyhun.greet_user())

  
   