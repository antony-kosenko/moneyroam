const commentIcon = document.getElementById("commentIcon")
const commentElement = document.getElementById("transactionComment").textContent
const commentSection = document.getElementById("commentSection")

var commentDiv = document.createElement("div")
var commentContainer = document.createElement("span")

commentIcon.addEventListener("mouseover", expandComment)
commentIcon.addEventListener("mouseout", hideComment)

function expandComment() {
    // console.log(getMousePosition.posX)
    commentContainer.textContent = commentElement
    commentDiv.appendChild(commentContainer)
    commentSection.appendChild(commentDiv)

    if (commentDiv.classList.contains("hided_item")) {
        commentDiv.classList.remove("hided_item")
        commentDiv.classList.add("revealed_item")
    }else{
        commentDiv.classList.add("revealed_item")
    }
        
}

function hideComment() {    
    if (commentDiv.classList.contains("revealed_item")) {
        commentDiv.classList.remove("revealed_item")
        commentDiv.classList.add("hided_item")
    }else{
        commentDiv.classList.add("hided_item")
    }
    commentDiv.removeChild(commentContainer)
}