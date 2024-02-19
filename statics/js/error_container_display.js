document.addEventListener('DOMContentLoaded', function() {
    var messages = document.getElementById('messages');
    if (messages) {
        if (messages.querySelector('.error')) {
            messages.classList.add('error-background');
        } else if (messages.querySelector('.success')) {
            messages.classList.add('success-background');
        } else {
            messages.classList.add('default-background');
        }
    }
});