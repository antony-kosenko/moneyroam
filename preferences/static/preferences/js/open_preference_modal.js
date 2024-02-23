document.addEventListener("DOMContentLoaded", function() {
    var openModalLink = document.getElementById("openPreferencesModal");
    var modal = document.getElementById("preferencesModal");
    var span = modal.querySelector(".close");
    var preferencesContent = modal.querySelector(".preferences_content");
    var tabs = modal.querySelectorAll(".tab");

    // Відкриття модального вікна та встановлення активною першої вкладки
    openModalLink.addEventListener("click", function(event) {
        event.preventDefault();
        modal.style.display = "block"; // Встановлюємо стиль блоку при відкритті модального вікна

        // Видаляємо клас 'active' з усіх вкладок
        tabs.forEach(function(tab) {
            tab.classList.remove('active');
        });

        // Встановлюємо клас 'active' для першої вкладки
        tabs[0].classList.add('active');

        // Отримуємо url першої вкладки та завантажуємо вміст
        var firstTabUrl = tabs[0].getAttribute("data-url");
        fetch(firstTabUrl)
            .then(response => response.text())
            .then(data => {
                preferencesContent.innerHTML = data;
            })
            .catch(error => {
                console.error('Error fetching content:', error);
            });
    });

    span.addEventListener("click", function() {
        modal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    // Обробка кліку на вкладці
    tabs.forEach(function(tab) {
        tab.addEventListener("click", function(event) {
            event.preventDefault();

            // Видаляємо клас 'active' з усіх вкладок
            tabs.forEach(function(tab) {
                tab.classList.remove('active');
            });

            // Додаємо клас 'active' до вибраної вкладки
            tab.classList.add('active');

            var url = tab.getAttribute("data-url");
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    preferencesContent.innerHTML = data;
                })
                .catch(error => {
                    console.error('Error fetching content:', error);
                });
        });
    });

    // Додаємо обробник подій для посилання Edit
    var editLink = modal.querySelector(".base_info a[href='']");
    editLink.addEventListener("click", function(event) {
        event.preventDefault();
        // Активуємо вкладку Profile
        tabs.forEach(function(tab) {
            if (tab.getAttribute("href") === "#profile") {
                tab.click();
            }
        });
    });

    // Додаємо обробник подій для кнопки Apply
    var applyButton = modal.querySelector(".apply-button");
    applyButton.addEventListener("click", function(event) {
        event.preventDefault();
        // Закриваємо модальне вікно
        modal.style.display = "none";
    });
});