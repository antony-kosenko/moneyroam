const commentIcons = document.getElementsByClassName("comment-icon")

for (const icon of commentIcons){
    icon.addEventListener("mouseover", () => expandComment(icon));
    icon.addEventListener("mouseout", () => hideComment(icon));
}

function expandComment(element) {
    let parentDiv = element.parentNode

    // getting comment's text from hiden element
    let commentTextContainer = parentDiv.querySelector('.transaction-comment')
    let commentText = commentTextContainer.textContent

    // Creating new block to display pop-up info
    let popupDiv = document.createElement("div")
    popupDiv.setAttribute("class", "popupDiv")
    let commentContainer = document.createElement("span")
    commentContainer.setAttribute("class", "receiptComment")
    parentDiv.appendChild(popupDiv)
    popupDiv.appendChild(commentContainer)
    commentContainer.textContent = commentText

    // adding styles to display popup container
    if (popupDiv.classList.contains("hided_item")) {
        popupDiv.classList.remove("hided_item")
        popupDiv.classList.add("revealed_item")
    }else{
        popupDiv.classList.add("revealed_item")
    }       
}

function hideComment(element) {
    let parentDiv = element.parentNode
    let popupDiv = parentDiv.querySelector(".popupDiv")
    let popupComment = popupDiv.querySelector(".receiptComment")
    if (popupDiv.classList.contains("revealed_item")) {
        popupDiv.classList.remove("revealed_item")
        popupDiv.classList.add("hided_item")
    }else{
        popupDiv.classList.add("hided_item")
    }
    popupDiv.removeChild(popupComment)
    parentDiv.removeChild(popupDiv)
}
