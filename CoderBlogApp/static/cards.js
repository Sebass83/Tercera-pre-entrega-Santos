

const cards = document.querySelectorAll('.card')
const URL = document.URL


cards.forEach(card => {
    card.addEventListener('click', () => {
        const data = card.getAttribute('data');
        window.location.href = `${URL}post/?termino=@${data}`
    })

});

