document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM is fully loaded!");

    const title = document.querySelector('.shop-title');

    if (title) {
        setTimeout(function() {
            title.classList.add('sparkling');
        }, 1000);
    } else {
        console.error("Element '.shop-title' not found!");
    }
});
