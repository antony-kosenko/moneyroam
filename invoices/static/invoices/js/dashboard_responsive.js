// Restructurizing a body of "transaction item"
const transactionsList = document.getElementsByClassName("transaction_item");

// change the way transactions display depend on browser's window size
if (window.innerWidth <= 1000) {

    for (let transaction of transactionsList) {
        // selecting first element of transaction body
        const firstElement = transaction.children[0]
        const transactionItemDescription = transaction.getElementsByClassName("transaction_item_description")[0]
        // creating new head container
        let transactionResponsiveHead = document.createElement("div")
        transaction.insertBefore(transactionResponsiveHead, firstElement).classList.add("transaction_responsive_head")
        transactionResponsiveHead.appendChild(firstElement)
        transactionResponsiveHead.appendChild(transactionItemDescription)
    }
}
