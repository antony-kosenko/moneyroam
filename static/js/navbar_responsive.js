function toggleSettingsBox() {
    var settingsBoxState = document.getElementById("settingsContainer")
    if (settingsBoxState !== null && settingsBoxState.style.display != "none") {
        settingsBoxState.style.display = "none";
    } else {
        let menuBody = document.createElement("div");
        menuBody.setAttribute("id", "settingsContainer");
        document.body.appendChild(menuBody);
    }
}

if (window.innerWidth <= 1000) {

    // selecting navbar profile button
    const profileButton = document.getElementById("settings");

    // processing the click event on profile button
    profileButton.addEventListener("click", toggleSettingsBox())

}