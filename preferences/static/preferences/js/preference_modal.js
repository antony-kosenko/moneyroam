// toggle preferences modal window to display and hide
const preferencesToggleButtons = document.getElementsByClassName("preferences-trigger")
var preferencesModal = document.getElementById("preferencesModal")
const closeModal = document.querySelector("#preferencesModal>.preferences_modal_content>span.close")

for (var trigger of preferencesToggleButtons) {
    trigger.addEventListener("click", function(){
        tabActivation(firstTab)
        preferencesModal.style.display = "block";
    });
}

closeModal.addEventListener("click", function(){
    preferencesModal.style.display = "none";
});


// Preferences tab switching

const preferenceTabsParent = document.getElementsByClassName("preferences_tabs")[0]
const preferencesTabs = preferenceTabsParent.children
const firstTab = preferencesTabs[0]
const preferencesForms = document.getElementsByClassName("preferences_content")[0].children
const editProfileButton = document.getElementById("profileEditButton")

// attaching EventListener for each tab press
for (const tab of preferencesTabs) {
    tab.addEventListener("click", function(){tabActivation(tab)});
};


// function to preferences tab activation
function tabActivation(tab) {
    for (var object of preferencesTabs) {
        object.classList.remove("active");
    }
    tab.classList.add("active");
    let tabName = tab.id.split("-")[0]

    for (const form of preferencesForms) {
        if (form.id.includes(tabName)) {
            form.style.display = "flex";
        } else {
            form.style.display = "none";
        };
    };
}

// Profile edit button link to profile tab
editProfileButton.addEventListener("click", ()=>{
    tabActivation(preferenceTabsParent.querySelectorAll('[id^="profile"]')[0])
}
);
