//get all radio buttons
let getRadios = document.querySelectorAll('#myForm > input[type="radio"]');
//get text area
let getTextArea = document.querySelector('#textarea-field');

//Loop through the radio button
getRadios.forEach(function (radio) {
    radio.addEventListener('change', function () {
        getTextArea.textContent = this.value //assign value to textArea
    })
})