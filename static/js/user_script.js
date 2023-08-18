//Changing the state of the submit button using javascript
document.addEventListener('DOMContentLoaded', () => {

    const submitButton = document.querySelector('#submit')
    var username = document.querySelector('#username')
    var password = document.querySelector('#password')

    function updateSubmitButtonState() {
        if (username.value.trim() !== '' && password.value.trim() !== '') {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    }

    username.addEventListener('input', updateSubmitButtonState);
    password.addEventListener('input', updateSubmitButtonState);

    updateSubmitButtonState(); // Check the initial state when the page loads

})

