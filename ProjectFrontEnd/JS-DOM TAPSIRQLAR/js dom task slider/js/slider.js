let slides = document.querySelector(".slides")
let slider = document.querySelector(".slider")
let slideAll = document.querySelectorAll(".slide")
let pos = 0
let sliderwidth = 1000
let sliderheight = 200
// slider width and height
slider.style.width = `${sliderwidth}px`
slider.style.height = `${sliderheight}px`


// slide width 
for (let slide of slideAll)
    slide.style.width = `${sliderwidth / 2}px`



// slides width and height
slides.style.width = `${sliderwidth / 2 * slideAll.length}px`


function left() {

    if (pos < 0) {
        pos += sliderwidth / 2
        slides.style.left = `${pos}px`;
    }



}

function right() {

    if (pos > -((slideAll.length - 2) * sliderwidth / 2)) {
        pos -= sliderwidth / 2
        slides.style.left = `${pos}px`;
    }


}