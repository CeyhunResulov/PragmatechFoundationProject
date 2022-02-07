tpl=(23,45,12,67)

def addToTuple(element):
    
    _list=list(tpl)
    _list.append(int(element))
    return _list
    
print(addToTuple((input('tuple elave etmek istediyini elementi yazin:'))))

# Tələblər
# addToTuple metodunun vəzifəsi tpl strukturunun içinə yeni bir element əlavə edilə bilməsini təmin etməkdir.Metod icra olunduğu zaman nəticə olaraq yeni element əlavə edilmiş formada ekranda çap olunmalıdır.
