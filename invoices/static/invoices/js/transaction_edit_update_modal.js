document.querySelectorAll('.edit-object-button').forEach(item => {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        const url = this.getAttribute('data-url');
        const targetModalId = this.getAttribute('data-target');
        const modalContent = document.getElementById(targetModalId + 'Content');
        const modal = document.getElementById(targetModalId);

        // AJAX для отримання HTML
        fetch(url)
            .then(response => response.text())
            .then(data => {
                modalContent.innerHTML = data;
                modal.style.display = 'block';

                // Встановлення відповідної дії для форми в модальному вікні
                const form = modalContent.querySelector('form');
                if (targetModalId === 'deleteModal') {
                    form.action = url;
                } else if (targetModalId === 'updateModal') {
                    // Встановлюємо URL для оновлення
                    form.action = url;
                }
            })
            .catch(error => console.error('Error:', error));
    });
});