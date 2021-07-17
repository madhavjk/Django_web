const arr = [];
const props = {
    "main": $(".slideArea"),
    "speed": 1000,
    "int": {}
};

$(document).ready(function () {
    makelistImages();
    outputImages();
    props.int = setInterval(nextSlide, props.speed);
})

$('.contBtns').on('click', '.prevBtn', function () {
    prevSlide();
    props.int = setInterval(nextSlide, props.speed);
})
$('.contBtns').on('click', '.nextBtn', function () {
    nextSlide();
    props.int = setInterval(nextSlide, props.speed);
})

function updateSlideValue(newCur) {
    clearInterval(props.int);
    newCur.addClass('active');
}

function nextSlide() {
    const cur = $(".active");
    const next = cur.removeClass('active').next();
    const newCur = next.length ? next : cur.prevAll().last();
    updateSlideValue(newCur);

}

function prevSlide() {
    const cur = $(".active");
    const prev = cur.removeClass('active').prev();
    const newCur = prev.length ? prev : cur.nextAll().last();
    updateSlideValue(newCur);
}

function outputImages() {
    $.each(arr, function (index, value) {
        let tempActive = index == 0 ? 'active' : '';
        let html = `<div class="slide ${tempActive}"><img src='${value}'><span>Caption ${index+1}</span></div>`;
        props.main.append(html);
    })
}

function makelistImages() {
    for (let x = 0; x < 9; x++) {
        let temp = `//via.placeholder.com/400x400/${rClr()}/${rClr()}?text=Image ${x+1}`;
        arr.push(temp);
    }
}

function rClr() {
    return Math.random().toString(16).substr(2, 6);
}