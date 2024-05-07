// Selecting elements
const selectMenu = document.getElementsByClassName("select-menu")[0]
const dropdownOptions = selectMenu.querySelector(".options");

// Ensure dropdown menu is closed and options list is hidden on page load
document.addEventListener("DOMContentLoaded", () => {
  closeDropdown();
});

// Function to close the dropdown menu and hide options list
function closeDropdown() {
  dropdownOptions.classList.remove("active")
  dropdownOptions.classList.add("hidden")
}

// Function to toggle dropdown menu
function toggleDropdown() {
  
  if (dropdownOptions.classList.contains("active")) {
    dropdownOptions.classList.remove("active");
    dropdownOptions.classList.add("hidden");
  } else if (dropdownOptions.classList.contains("hidden")){
    dropdownOptions.classList.remove("hidden");
    dropdownOptions.classList.add("active")   
  }
}

// Adding eventlistener to toggle dropdown menu
selectMenu.addEventListener("click", toggleDropdown)
