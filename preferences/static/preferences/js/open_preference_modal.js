document.addEventListener("DOMContentLoaded", function() {
    var openModalLink = document.getElementById("openPreferencesModal");
    var modal = document.getElementById("preferencesModal");
    var span = modal.querySelector(".close");
    var preferencesContent = modal.querySelector(".preferences_content");
    var tabs = modal.querySelectorAll(".tab");

    openModalLink.addEventListener("click", function(event) {
        event.preventDefault();
        modal.style.display = "block";

        tabs.forEach(function(tab) {
            tab.classList.remove('active');
        });

        tabs[0].classList.add('active');

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

    tabs.forEach(function(tab) {
        tab.addEventListener("click", function(event) {
            event.preventDefault();

            tabs.forEach(function(tab) {
                tab.classList.remove('active');
            });

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

    var editLink = modal.querySelector(".base_info a[href='']");
    editLink.addEventListener("click", function(event) {
        event.preventDefault();
        tabs.forEach(function(tab) {
            if (tab.getAttribute("href") === "#profile") {
                tab.click();
            }
        });
    });
});
