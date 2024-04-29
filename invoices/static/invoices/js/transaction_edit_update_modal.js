document.querySelectorAll('.edit-object-button').forEach(item => {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        const url = this.getAttribute('data-url');
        const targetModalId = this.getAttribute('data-target');
        const modalContent = document.getElementById(targetModalId + 'Content');
        const modal = document.getElementById(targetModalId);

        fetch(url)
            .then(response => response.text())
            .then(data => {
                modalContent.innerHTML = data;
                modal.style.display = 'block';

                const form = modalContent.querySelector('form');
                if (targetModalId === 'deleteModal') {
                    form.action = url;
                } else if (targetModalId === 'updateModal') {
                    form.action = url;
                }
                const uploadImageSection = form.querySelector("#div_id_receipt > div")
                // elements to be groupped in newly created div
                const clearLabel = uploadImageSection.querySelector("label[for='receipt-clear_id']")
                const clearCheckbox = uploadImageSection.querySelector("#receipt-clear_id")
                // creating new div to containe unput and checkbox tags together
                uploadImageSection.setAttribute("class", "img-manage-container")
                const clearElemenetsContainer = document.createElement("div")
                clearElemenetsContainer.setAttribute("class", "clear-box")
                uploadImageSection.insertBefore(clearElemenetsContainer, uploadImageSection.querySelector("br"))

                clearElemenetsContainer.appendChild(clearLabel)
                clearElemenetsContainer.appendChild(clearCheckbox)

            })
            .catch(error => console.error('Error:', error));
    });
});