var exampleModal1 = document.getElementById('exampleModal1')
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    var modalTitle = exampleModal.querySelector('.modal-title')
    var modalBodyInput = exampleModal.querySelector('.modal-body input')

    modalTitle.textContent = 'New message to ' + recipient
    modalBodyInput.value = recipient
})

var WaterConnection = document.getElementById('WaterConnection')
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    var modalTitle = exampleModal.querySelector('.modal-title')
    var modalBodyInput = exampleModal.querySelector('.modal-body input')

    modalTitle.textContent = 'New message to ' + recipient
    modalBodyInput.value = recipient
})

var loginModal = document.getElementById('loginModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    var modalTitle = exampleModal.querySelector('.modal-title')
    var modalBodyInput = exampleModal.querySelector('.modal-body input')

    modalTitle.textContent = 'New message to ' + recipient
    modalBodyInput.value = recipient
})

document.querySelector('.offcanvas-trigger').addEventListener('click', function () {
    document.getElementById('offcanvasMenu').classList.toggle('offcanvas');
});

document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Perform form validation
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var message = document.getElementById("message").value.trim();

    if (name === "" || email === "" || message === "") {
        alert("Please fill in all fields");
        return;
    }

    if (!validateEmail(email)) {
        alert("Please enter a valid email address");
        return;
    }

    // Form is valid, display success message
    document.getElementById("contactForm").reset();
    document.getElementById("successMessage").classList.remove("hidden");
});

// Email validation function
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function validateForm(event) {
event.preventDefault(); // Prevent form submission

// Retrieve form values
var houseNo = document.getElementById("houseNo").value;
var householderName = document.getElementById("householderName").value;

// Perform validation
if (houseNo.trim() === "") {
alert("Please enter your house number.");
return;
}

if (householderName.trim() === "") {
alert("Please enter the householder's name.");
return;
}

// Validation successful, proceed with login
alert("Login successful!");
document.getElementById("loginForm").reset(); // Reset form
}