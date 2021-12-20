// emr 01--ekranin arxa fon rengini deyis
function backcolor() {
    document.querySelector("body").style.background = "red"

}

// emr 02--basligin rengini deyis
function headcolor() {
    document.querySelector(".card h1").style.color = "blue"
}

// emr 03--metnin rengini deyis
function textcolor() {
    document.querySelector(".card p").style.color = "green"
    document.querySelector(".card ul").style.color = "green"
}


// emr 04--metnin daxilinde nece herf oldugunu neticenin qarsisinda gosterin

function herflerisay() {
a = document.querySelector(".card p").innerHTML
x =document.querySelector("ul").innerHTML
c=a.length+x.length
b= [c]
document.querySelector(".card div").innerHTML+=b
}

// emr 05 --metnin daxilinde nece soz oldugunu neticenin qarsisinda gosterin
 function sozsayi(){
    a =document.querySelector(".card p").innerHTML.split(" ")
    b=document.querySelector("ul").innerHTML
    c =a.length
    d=[a]
     document.querySelector(".card div").innerHTML= d
 }

// emr 10
function listyerdeyis(a, b) {
    a = document.querySelector(".card ul li:nth-child(7)").innerHTML 
    b = document.querySelector(".card ul li:nth-child(1)").innerHTML 
    document.querySelector(".card ul li:nth-child(1)").innerHTML=a
    document.querySelector(".card ul li:nth-child(7)").innerHTML=b
}


