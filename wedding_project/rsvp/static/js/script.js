let startX;
let startY;
let startScrollX;

document.addEventListener('touchstart', function(e) {
    startX = e.touches[0].pageX;
    startY = e.touches[0].pageY;
    startScrollX = window.scrollX;
});

document.addEventListener('touchmove', function(e){
    let currnentX = e.touches[0].pageX;
    let currnentY = e.touches[0].pageY;
    let diffX = startX - currnentX;
    let diffY = startY -  currnentY;
})

// check if horizontal swipe

if (Math,abs(diffX) > Math.abs(diffY)){
    e.preventDefault();

    window.scrollTo(startScrollX + diffX, window.scrollY);
}