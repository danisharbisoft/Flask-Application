//Changing the state of the submit button using javascript
document.addEventListener('DOMContentLoaded', () => {

    const submitButton = document.querySelector('#submit')
    var content = document.querySelector('#content')

    function updateSubmitButtonState() {
        if (content.value.trim() === '') {
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;
        }
    }

    content.addEventListener('input', updateSubmitButtonState);

    updateSubmitButtonState(); // Check the initial state when the page loads

})

