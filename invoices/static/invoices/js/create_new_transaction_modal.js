document.getElementById("openModalBtn").addEventListener("click", function() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
  });
  
  document.getElementById("closeModalBtn").addEventListener("click", function() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
  });
  
  window.addEventListener("click", function(event) {
    var modal = document.getElementById("myModal");
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });