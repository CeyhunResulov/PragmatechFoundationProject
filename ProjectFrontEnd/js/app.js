let drdown=document.querySelector(".dropdown")
let close=document.querySelector(".close")
let openclose
function close() {
    drdown.style.display = "none"
}

function dropdown(){
    drdown.style.display="block"
}
if(close){
    drdown.style.display = "none"
}else if(dropdown){
    drdown.style.display = "block" 
}