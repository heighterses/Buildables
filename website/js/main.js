document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }
    
    document.querySelectorAll('.nav-menu li a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!hamburger.contains(e.target) && !navMenu.contains(e.target) && navMenu.classList.contains('active')) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
    
    // Mobile dropdown toggle
    const dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('active');
        });
    });
    
    document.addEventListener('click', () => {
        dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
    });
    
    // Hero Slider
    const slides = document.querySelectorAll('.hero-slider .slide');
    const dots = document.querySelectorAll('.slider-dots .dot');
    const prevBtn = document.querySelector('.prev-slide');
    const nextBtn = document.querySelector('.next-slide');
    let currentSlide = 0;
    
    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));
        
        slides[index].classList.add('active');
        dots[index].classList.add('active');
        currentSlide = index;
    }
    
    if (prevBtn && nextBtn) {
        prevBtn.addEventListener('click', function() {
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            showSlide(currentSlide);
        });
        
        nextBtn.addEventListener('click', function() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        });
    }
    
    if (dots.length > 0) {
        dots.forEach((dot, index) => {
            dot.addEventListener('click', function() {
                showSlide(index);
            });
        });
    }
    
    // Auto slide for hero slider
    let slideInterval = setInterval(function() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }, 5000);
    
    // Pause auto slide on hover
    const heroSlider = document.querySelector('.hero-slider');
    if (heroSlider) {
        heroSlider.addEventListener('mouseenter', function() {
            clearInterval(slideInterval);
        });
        
        heroSlider.addEventListener('mouseleave', function() {
            slideInterval = setInterval(function() {
                currentSlide = (currentSlide + 1) % slides.length;
                showSlide(currentSlide);
            }, 5000);
        });
    }
    
    // Testimonials Slider
    const testimonials = document.querySelectorAll('.testimonial');
    const testimonialDots = document.querySelectorAll('.testimonial-dots .dot');
    let currentTestimonial = 0;
    
    function showTestimonial(index) {
        testimonials.forEach(testimonial => testimonial.classList.remove('active'));
        testimonialDots.forEach(dot => dot.classList.remove('active'));
        
        testimonials[index].classList.add('active');
        testimonialDots[index].classList.add('active');
        currentTestimonial = index;
    }
    
    if (testimonialDots.length > 0) {
        testimonialDots.forEach((dot, index) => {
            dot.addEventListener('click', function() {
                showTestimonial(index);
            });
        });
    }
    
    // Auto slide for testimonials
    let testimonialInterval = setInterval(function() {
        if (testimonials.length > 0) {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            showTestimonial(currentTestimonial);
        }
    }, 4000);
    
    // Newsletter Form Submission
    const newsletterForm = document.querySelector('.newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            
            // Here you would typically send the email to your server
            // For now, we'll just show an alert
            alert(`Thank you for subscribing with ${email}! You'll receive our updates soon.`);
            this.reset();
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Scroll to top button
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollTopBtn.classList.add('scroll-top');
    document.body.appendChild(scrollTopBtn);
    
    scrollTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Show/hide scroll to top button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollTopBtn.classList.add('show');
        } else {
            scrollTopBtn.classList.remove('show');
        }
    });
    
    // Add scroll to top button styles
    const style = document.createElement('style');
    style.textContent = `
        .scroll-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: var(--primary-color);
            color: white;
            border: none;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 99;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.2rem;
        }
        
        .scroll-top.show {
            opacity: 1;
            visibility: visible;
        }
        
        .scroll-top:hover {
            background-color: #3a5ecc;
            transform: translateY(-3px);
        }
    `;
    document.head.appendChild(style);

    // Fellowship Application Form
    const fellowshipForm = document.getElementById('fellowshipForm');

    if (fellowshipForm) {
        fellowshipForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(fellowshipForm);
            const data = Object.fromEntries(formData.entries());
            
            try {
                // Show loading state
                const submitButton = fellowshipForm.querySelector('button[type="submit"]');
                const originalText = submitButton.textContent;
                submitButton.textContent = 'Submitting...';
                submitButton.disabled = true;
                
                // Simulate API call (replace with actual API endpoint)
                await new Promise(resolve => setTimeout(resolve, 1500));
                
                // Show success message
                alert('Thank you for your application! We will contact you soon.');
                fellowshipForm.reset();
                
                // Reset button
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                
            } catch (error) {
                console.error('Error submitting form:', error);
                alert('There was an error submitting your application. Please try again.');
            }
        });
    }

    // Contact Form Handling
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData.entries());
            
            try {
                // Show loading state
                const submitButton = contactForm.querySelector('button[type="submit"]');
                const originalText = submitButton.textContent;
                submitButton.textContent = 'Sending...';
                submitButton.disabled = true;
                
                // Simulate API call (replace with actual API endpoint)
                await new Promise(resolve => setTimeout(resolve, 1500));
                
                // Show success message
                alert('Thank you for your message! We will get back to you soon.');
                contactForm.reset();
                
                // Reset button
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                
            } catch (error) {
                console.error('Error sending message:', error);
                alert('There was an error sending your message. Please try again.');
            }
        });
    }

    // FAQ Toggle
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            const icon = question.querySelector('.faq-toggle i');
            
            // Toggle answer visibility
            answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
            
            // Toggle icon
            icon.classList.toggle('fa-plus');
            icon.classList.toggle('fa-minus');
            
            // Close other answers
            faqQuestions.forEach(otherQuestion => {
                if (otherQuestion !== question) {
                    const otherAnswer = otherQuestion.nextElementSibling;
                    const otherIcon = otherQuestion.querySelector('.faq-toggle i');
                    otherAnswer.style.display = 'none';
                    otherIcon.classList.remove('fa-minus');
                    otherIcon.classList.add('fa-plus');
                }
            });
        });
    });

    // Fellowship Application Custom File Input Handler
    const fileInput = document.getElementById('resume');
    const fileLabel = document.querySelector('.custom-file-label');
    const fileSelected = document.querySelector('.custom-file-selected');
    if (fileInput && fileLabel && fileSelected) {
        fileInput.addEventListener('change', function() {
            if (this.files && this.files.length > 0) {
                fileSelected.textContent = this.files[0].name;
            } else {
                fileSelected.textContent = 'No file chosen';
            }
        });
    }
});
