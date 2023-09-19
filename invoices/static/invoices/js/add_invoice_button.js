// Отримуємо необхідні елементи DOM
var modal = document.getElementById('myModal');
var openModalBtn = document.getElementById('openModalBtn');
var closeBtn = document.getElementsByClassName('close')[0];
var postForm = document.getElementById('postForm');


// Функція для відкриття модального вікна
function openModal() {
    modal.style.display = 'block';
    modal.style.animation = "slideInRight 0.5s"; // Додали анімацію вправо
}

// Функція для закриття модального вікна
function closeModal() {
    modal.style.animation = "slideOutRight 0.5s"; // Додали анімацію закриття вправо
    setTimeout(function() {
        modal.style.display = 'none';
    }, 500); // Затримка, щоб анімація закінчилася перед закриттям
}

// Показати модальне вікно при кліку на кнопку
openModalBtn.addEventListener('click', openModal);

// Закрити модальне вікно при кліку на хрестик
closeBtn.addEventListener('click', closeModal);

// Закрити модальне вікно при кліку поза ним
window.addEventListener('click', function(event) {
    if (event.target == modal) {
        closeModal();
    }
});