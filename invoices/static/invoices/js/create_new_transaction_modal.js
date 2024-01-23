document.getElementById("openModalBtn").addEventListener("click", function() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
  });
  
  // JavaScript для закриття модального вікна
  document.getElementById("closeModalBtn").addEventListener("click", function() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
  });
  
  // Закриття модального вікна, коли користувач клікає поза ним
  window.addEventListener("click", function(event) {
    var modal = document.getElementById("myModal");
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });