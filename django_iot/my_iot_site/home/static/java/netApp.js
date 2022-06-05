const menu = document.querySelector('.menu')
const close = document.querySelector('.close')
const nav = document.querySelector('nav')

// function goPython(){
//         $.ajax({
//         url: "MYSCRIPT.py",
//         context: document.body
//         }).done(function() {
//         alert('finished python script');;
//         });
//     }

menu.addEventListener('click', () => {
    nav.classList.add('open-nav')
})
close.addEventListener('click', () => {
    nav.classList.remove('open-nav')
})
