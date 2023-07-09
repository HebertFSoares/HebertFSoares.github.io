window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    navbarShrink();

    document.addEventListener('scroll', navbarShrink);

    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

document.addEventListener('DOMContentLoaded', function() {
    var progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(function(progressBar) {
      var value = progressBar.getAttribute('aria-valuenow');
      progressBar.style.width = value + '%';
    });
  });
  

  function animateText(element, text) {
    var index = 0;
    var typingSpeed = 200; // Velocidade de digitação (ajuste conforme necessário)
    var eraseSpeed = 80; // Velocidade de apagamento (ajuste conforme necessário)
    var pauseBetweenAnimations = 1000; // Tempo de pausa entre as animações (ajuste conforme necessário)
  
    function type() {
      if (index < text.length) {
        element.textContent += text.charAt(index);
        index++;
        setTimeout(type, typingSpeed);
      } else {
        setTimeout(erase, pauseBetweenAnimations);
      }
    }
  
    function erase() {
      if (index > 0) {
        element.textContent = text.substring(0, index - 1);
        index--;
        setTimeout(erase, eraseSpeed);
      } else {
        setTimeout(type, pauseBetweenAnimations);
      }
    }
  
    // Inicia a animação de digitação
    type();
  }
  
  // Obtém os elementos para animação
  var heading = document.querySelector('.masthead-heading');
  var subheading = document.querySelector('.masthead-subheading');
  
  // Textos para animação
  var headingText = 'Hebert Soares'; // Substitua pelo texto desejado
  var subheadingText = 'Programador Python - Desenvolvedor Web Django'; // Substitua pelo texto desejado
  
  // Chama a função para iniciar a animação nos elementos
  animateText(heading, headingText);
  animateText(subheading, subheadingText);
  
  $(document).ready(function () {
    $("#skills-carousel").owlCarousel({
        loop: true,
        margin: 30,
        nav: true,
        dots: false,
        responsive: {
            0: {
                items: 1,
            },
            576: {
                items: 2,
            },
            768: {
                items: 3,
            },
            992: {
                items: 4,
            },
            1200: {
                items: 5,
            },
        },
        navText: ['<i class="fas fa-chevron-left"></i>', '<i class="fas fa-chevron-right"></i>'],
    });
});

  
  
  
  