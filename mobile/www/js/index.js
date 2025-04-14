let toggleLoginForm = false; 
const form = document.getElementById("code-container");
form.classList.add("hide-code");

document.addEventListener("DOMContentLoaded", function() {
  const inputs = document.querySelectorAll('.code-input');
  


  inputs.forEach((input, index) => {
      input.addEventListener("input", function() {
          if (input.value.length === 1 && index < inputs.length - 1) {
              inputs[index + 1].focus();
          }
      });
  });
});


document.addEventListener("mousedown", function(e) {
  if (e.button === 0 && !toggleLoginForm) {
    toggleLoginForm = true;
    
  
    const loginForm = document.getElementById("container");
    const logo = document.getElementById("logo");
    const aisat = document.getElementById("aisat");
    
    loginForm.style.display = "block";
    loginForm.classList.add("show"); 
    logo.classList.add("show");
    aisat.classList.add("show");


  }
  
});  

function toggleLogin() {
  const form = document.getElementById("container");
  form.classList.remove("hide");
  form.classList.add("show");
}

function hideLogin() {
  const form = document.getElementById("container");
  form.classList.remove("show");
  form.classList.add("hide");
}

function toggleRegister() {
  const form = document.getElementById("reg-container");
  form.classList.remove("hide");
  form.classList.add("show");
}

function hideRegister() {
  const form = document.getElementById("reg-container");
  form.classList.remove("show");
  form.classList.add("hide");
  form.classList.remove("popupactive")
}

function togglePopup() {
  const form = document.getElementById("reset-container");
  form.classList.remove("hidepopup");
  form.classList.add("show");
  form.classList.add("popupactive")
}



function hidePopup() {
  const form = document.getElementById("reset-container");
  form.classList.remove("showpopup");
  form.classList.add("hidepopup");
}

hidePopup();


document.addEventListener("click", function (e) {
    if (e.target.id === "register-link") {
      toggleRegister();
      hideLogin();
    }
  });

document.addEventListener("click", function (e) {
    if (e.target.id === "login-link") {
      toggleLogin();
      hideRegister();
      
    }
  });
  

  document.addEventListener("click", function (e) {
    if (e.target.id === "forgot-link") {
      hideLogin();
      hideRegister();
      togglePopup();


      
    }
  });


  document.addEventListener("click", function (e) {
    if (e.target.id === "send-code") {
      const form = document.getElementById("email-container");
      form.classList.add("hide-email-sent");
      console.log("Email sent");

      const show_code = document.getElementById("code-container");
      show_code.classList.add("show-code");
      show_code.classList.remove("hide-code");
    }
  });


  document.addEventListener("click", function (e) {
    if (e.target.id === "continue-reset") {
      const show_code = document.getElementById("code-container");
      show_code.classList.remove("show-code");
      show_code.classList.add("hide-code");

      const reset_password = document.getElementById("resetpass-con");
      reset_password.classList.add("show-resetpass");
    } 

  });