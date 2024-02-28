// Selecting elements
const optionMenu = document.querySelector(".select-menu");
const selectBtn = optionMenu.querySelector(".select-btn");
const options = optionMenu.querySelectorAll(".option");
const optionList = optionMenu.querySelector(".options");

// Function to close the dropdown menu and hide options list
function closeDropdown() {
  optionMenu.classList.remove("active");
  optionList.classList.remove("show");
}

// Adding event listener to close dropdown menu when clicking outside of it
document.addEventListener("click", (event) => {
  if (!optionMenu.contains(event.target)) {
    closeDropdown();
  }
});

// Adding event listener to toggle dropdown menu on button click
selectBtn.addEventListener("click", () => {
  optionMenu.classList.toggle("active");
  if (optionMenu.classList.contains("active")) {
    optionList.classList.add("show");
  } else {
    optionList.classList.remove("show");
  }
});

// Adding event listener to handle option selection
options.forEach((option) => {
  option.addEventListener("click", () => {
    closeDropdown();
  });
});

// Ensure dropdown menu is closed and options list is hidden on page load
document.addEventListener("DOMContentLoaded", () => {
  closeDropdown();
});






{/* <div class="adsbox ads ad adsbox doubleclick ad-placement carbon-ads" id="google_ads_iframe_/6355419/Travel/Europe/France/Paris_0__container__" bis_skin_checked="1">&nbsp;</div> */}