// Color-picker --> https://github.com/Simonwep/pickr
const pickr = Pickr.create({
    el: '.color-picker',
    theme: 'nano', // or 'monolith', or 'nano'
    autoReposition: true,
    showAlways: true, // color picker is always on
    // inline: false,
    components: {

        // Main components
        preview: true,
        opacity: false,
        hue: true,

        // Input / output Options
        interaction: {
            hex: false,
            rgba: false,
            hsla: false,
            hsva: false,
            cmyk: false,
            input: false,
            clear: false,
            save: true,
        }
    }
});

pickr.show()

pickr.on('save', (color) => {
    document.getElementById("selectedColor").innerText = color.toRGBA();
})

// MENU
// const menu = document.querySelector('.menu');
// const close = document.querySelector('.close');
// const nav = document.querySelector('nav');

// menu.addEventListener('click', () => {
//     nav.classList.add('open-nav')
// })
// close.addEventListener('click', () => {
//     nav.classList.remove('open-nav')
// })

