# 1. Bir dənə Restoran classı yaradın. Bu classa init() metdou bu classın adını (restaurant_name) və
#  mətbəx növü (cuisine_type) adlı iki atribitunu saxlamalıdır. 
# describe_restaurant() adlı bir metod yaradın hansı ki restoranın adını və mətbəxin növünü ekrana print etsin.
#  Restoranın açıq olmasını mesaj verən open_restaurant() adlı başqa bit metdi yaradın. 
# Sonra restoran adlı obyekt yaradın bu class-dan və restotanın adını, mətbəxinin növünü, restoran haqqında məlumatları və 
# açıq olmasını çapa verin. Bu Restoran classından daha iki obyek yaradın və describe_restaurant metodunu yeni yaratdığınız hər iki obyekt üçün tətbiq edin.




# from pydoc import describe
# import re


# class restorant:
#     def __init__(self,restaurant_name,cuisine_type,info):
#         self.name=restaurant_name
#         self.metbex_novu=cuisine_type
#         self.melumat=info

#     def describe_restaurant(self):
#         print(f'resatoranin adi:{restorant_.name}\nmetbex novu:{restorant_.metbex_novu}')
# restorant_=restorant('qocet','italy','beli restoran hal hazirda aciqdir')

# restorant_.melumat=input('sualiniz varmi?')
# if 'restoran aciqdirmi' in restorant_.melumat or 'restoran isleyirmi' in restorant_.melumat or 'open' in restorant_.melumat:
#     print("beli restoran aciqdir")
# restorant_.describe_restaurant()       