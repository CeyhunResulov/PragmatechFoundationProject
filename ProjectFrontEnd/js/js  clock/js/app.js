let second = document.querySelector(".second")
let secondrotate = 0
function saniye() {
    second.style.transform = `rotate(${secondrotate}deg)`
    secondrotate+=6
    
}
setInterval(saniye,1000)
let minute = document.querySelector(".minute")
let minuterotate = 0
function minute(){
    
    minute.style.transform=`rotate(${minuterotate}deg)`
    minuterotate+=6
}
setInterval(minute,1000)