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
    var isDeleting = false;
  
    function type() {
      if (index < text.length && !isDeleting) {
        element.textContent += text.charAt(index);
        index++;
      } else {
        isDeleting = true;
      }
  
      if (isDeleting) {
        element.textContent = text.substring(0, index);
  
        if (index === 0) {
          isDeleting = false;
        }
        index--;
      }
  
      var typingSpeed = isDeleting ? 100 : 200; // Velocidade de digitação e apagamento (ajuste conforme necessário)
      setTimeout(type, typingSpeed);
    }
  
    // Inicia a animação de digitação
    type();
  }
  
  // Obtém o elemento <h1> com a classe "error-animation"
  var heading = document.querySelector('.error-animation');
  
  // Texto para animação
  var text = 'Hebert Soares'; // Substitua pelo texto desejado
  
  // Chama a função para iniciar a animação
  animateText(heading, text);
  
  