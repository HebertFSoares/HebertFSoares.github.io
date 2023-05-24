document.getElementById("user-type").addEventListener("change", function() {
    var userType = this.value;
    
    var estudanteFields = document.querySelector(".estudante-fields");
    var anfitriaoFields = document.querySelector(".anfitriao-fields");
    
    if (userType === "estudante") {
      estudanteFields.style.display = "block";
      anfitriaoFields.style.display = "none";
    } else if (userType === "anfitriao") {
      estudanteFields.style.display = "none";
      anfitriaoFields.style.display = "block";
    } else {
      estudanteFields.style.display = "none";
      anfitriaoFields.style.display = "none";
    }
  });

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
  
  