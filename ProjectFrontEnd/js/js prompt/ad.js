/* 1.prompt() istifadə edərək ad və soyad tələb edin və
 bu daxil edilən məlumatlardan istifadə edərək alert() metodu ilə ekrana "Memmed Hesenov sən xoş gəlmisən" formatında 
yazı çıxarın . Template Literal mövzusu faydalı ola bilər. (Yazılan kodlar ad.js faylında olmalıdır)

let firstname = prompt("firstname")
let lastname = prompt("lastname")
if (firstname == 'ceyhun' && lastname == "resulov") {
    alert("Ceyhun xos gelmisen ")
} else {
    alert("melumatlar sehvdir")
}

*/


/* 2.
3+(2-true+false)/3&&true complex ifadəsinin nəticəsi nə olacaq və 
bunun hansı sıralamalı ilə həllediləcəyi kod yazaraq izah edin
*/

// let a = 3
// let b = 2
// let c = true
// let d = false

// let hesabla = a + (b - c + d) / a && c
// console.log(hesabla) 
// cavab=true



/*3.prompt parol ilə sifarişdən istifadəçi adı və tələb olunur.bu daxil edilmiş məlumatlara əsasən işlər görülməlidir.
 Əgər istifadəçi adı və ya parol bos buraxılıbsa ekrana alert ilə 'Deyerler bos ola bilməz' yazısı çıxsın

İstifadəçi adı 'admin' və parol '123456' - dirsa ekrana alert vasitesi ilə 'Tebriklər siz sistemə daxil oldugunuz'

Daxil edilen deyerlerden her hansi biri duz deyilse ona uygun mesaj cixsin.Meselen username duz deyil*/


// let istifadeci = prompt("istfadeci ad:")
// let parol = prompt("parol:")
// if (istifadeci == "" || parol == "") {
//     alert("deyerler bos ola bilmez")
// } else if (istifadeci == "admin" && parol == "123456") {
//     alert("tebrikler sisteme daxil oldunuz")
// } else if (istifadeci != "admin") {
//     alert("istifadeci adi duzgun deyil!")
// } else if (parol != "123456") {
//     alert("parol duzgun deyil!")
// }






/*while və ya üçün istifadə olunan tapşırıqları yazın
1 - 1000 ədəd ədədləri ekrana çap edin
1 - 1000 ədəd tək ədədləri ekrana çap edin
1 - 1000 3 - ə bölünən ədədləri ekrana çap edin
1 - 1000 ədədlərin cəmini hesablayıb ekrana çap edin*/


// 1.
// let a=0
// while(a<1000){
//     a++
//     console.log(a)
// }


// 2.
// for(let i=1;i<=1000;i++)
// console.log(i)

// 3.
// let a=1
// while(a<1000){

//     console.log(a)
//     a += 2
// }


// 4.
// for (let i = 1; i < 1000; i+=2)
// console.log(i)


// 5.
// let a=3
// while (a<1000) {
//    console.log(a)
//    a+=3

// }


// 6.
// for(let i=3; i<1000; i+=3)
// console.log(i)



// 7.
// let cem=0
// let a=0
// while(a<=1000){
//     console.log(cem)
//      a++
//      cem+=a


// }



// 8.
// let cem = 0
// for (let i = 0; i <= 1000; i++)
//     cem += i
// console.log(cem)

