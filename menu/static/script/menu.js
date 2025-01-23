var modals = document.querySelectorAll("[id^='modal-']");
var btns = document.querySelectorAll("[id^='btn-']");
var closebtns = document.querySelectorAll(".close");

btns.forEach(function(btn, index) {
    btn.addEventListener("click", function() {
        modals[index].style.display = "block";
    });
});


closebtns.forEach(function(closebtn, index) {
    closebtn.addEventListener("click", function() {
        modals[index].style.display = "none";
    });
});

window.addEventListener("click", function(event) {
    modals.forEach(function(modal) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
});
