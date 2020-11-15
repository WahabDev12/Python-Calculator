// Creating a  Generic Function

function copyText(htmlElement){
    // If the text we are copying is not an html element then dont do anything
    if(!htmlElement){
        return;
    }
    // else if it is an html element then execute code
    // element Text is the password being copied
    let elementText = htmlElement.innerText;
    // Creating a temporal input field to house the password
    let inputElement = document.createElement("input");
    inputElement.setAttribute("value", elementText)
    //Appending the passwor generated to the input field
    document.body.appendChild(inputElement);
    // input.select selects/highlights the text to be copied (password generated)
    inputElement.select()
    //This command allows you to copy text to clipboard
    document.execCommand("copy")
    // Killing/ removing the input field from the DOM
    inputElement.parentNode.removeChild(inputElement)
}

document.getElementById("copy").onclick = function(){
    copyText(document.getElementById("text"))
    //Alerts the user of copy status
    alert("Text has being copied to Clipboard")
}

