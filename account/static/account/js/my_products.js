// const ViewCont = document.getElementById('preview')
// const Preview = document.querySelectorAll('image-cont')

document.addEventListener('click', function(event) {
    if (event.target.closest('.image-cont')) {
        console.log('Кликнули на .image-cont:', event.target);
        preview_win(event.target);
    }
});

function preview_win(element) {
    console.log(element.querySelector('img'))
    var imageSrc = null
    if (element.querySelector('img') === null){
        imageSrc = element.src
    } else {
        imageSrc = element.querySelector('img').src;
    }


    console.log('Изображение:', imageSrc);

}