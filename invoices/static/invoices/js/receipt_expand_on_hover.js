var receiptIcons = document.getElementsByClassName("receipt-icon")

for (const image of receiptIcons){
    image.addEventListener("mouseover", () => receiptPreview(image));
    image.addEventListener("mouseout", () => receiptPreview(image, true));
}

function receiptPreview(image, hide = false) {
    let parentDiv = image.parentNode;
    let receiptImg = parentDiv.querySelector(".receipt-img");
    if (hide) {
        receiptImg.style.display = "none";
    }else{
        receiptImg.style.display = "block";
    }
}
