document.addEventListener("DOMContentLoaded", function () {
    // Auto slide functionality
    let slideIndex = 0;
    const slides = document.querySelectorAll(".slide");
    const autoBtns = document.querySelectorAll(".navigation-auto div");

    function showSlide(index) {
        const slideWidth = slides[0].clientWidth;
        document.querySelector(".slides").style.transform = `translateX(-${index * slideWidth}px)`;
        
        autoBtns.forEach((btn, i) => {
            btn.style.background = i === index ? "#0056b3" : "#ccc";
        });
    }

    function nextSlide() {
        slideIndex = (slideIndex + 1) % slides.length;
        showSlide(slideIndex);
    }

    setInterval(nextSlide, 5000); // Change slide every 5 seconds

    // Manual navigation (button clicks)
    document.querySelectorAll(".manual-btn").forEach((btn, index) => {
        btn.addEventListener("click", () => {
            slideIndex = index;
            showSlide(slideIndex);
        });
    });
});
