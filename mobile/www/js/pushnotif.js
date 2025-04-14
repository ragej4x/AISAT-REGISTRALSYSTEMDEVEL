document.addEventListener("click", function (e) {
    if (e.target.id === "login-link") {
        document.addEventListener('deviceready', function () {
            FirebasePlugin.getToken(function (token) {
              console.log("FCM Token:", token);
            }, function (error) {
              console.error("Token error:", error);
            });
          
            FirebasePlugin.onMessageReceived(function (message) {
              console.log("Push received:", message);
              alert(message.body);
            }, function (error) {
              console.error("Push error:", error);
            });
          });
          
    }
  });
  
