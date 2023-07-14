'use strict';
const switcher = document.querySelector('.btn');
const submit = document.querySelector('submit');

switcher.addEventListener('click', function() {
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    const className = document.body.className;
    if(className == "light-theme") {
        this.textContent = "Dark";
    } else {
        this.textContent = "Light";
    }

    console.log('current class name: ' + className);
});
function summary(username, includeForks) {
    
}
function displayjson() {
    var username = document.getElementById("username").value;
    var includeForks = document.getElementById("forkedCheck").checked;
    var result = document.getElementById("info");   
    // text.textContent = "";
    // text.textContent += "Username: " + username;
    // if (includeForks == false)
    // {
    //     text.textContent += "\r\n include forks: false";
    // }
    // else
    // {
    //     text.textContent += "\r\n include forks: true";
    // }
    var enteredUsername = document.getElementById("enteredUsername");
    var forksVal = document.getElementById("forksVal");
    enteredUsername.textContent = username;
    forksVal.textContent = includeForks.toString();
    result.style.display = "block";
    res = summary(username, includeForks)
}