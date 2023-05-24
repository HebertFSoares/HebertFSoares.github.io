// login.js

// Função para alternar entre o modo escuro e modo claro
function toggleDarkMode() {
    var body = document.body;
    body.classList.toggle('dark-mode');
  }
  
  // Selecionar o botão de alternar modo escuro
  var darkModeButton = document.getElementById('dark-mode-button');
  
  // Adicionar evento de clique no botão
  darkModeButton.addEventListener('click', function() {
    toggleDarkMode();
  });
  