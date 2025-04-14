document.addEventListener("click", function (e) {
    if (e.target.id === "login-link") {
        document.addEventListener('deviceready', function () {
            // Get FCM token
            FirebasePlugin.getToken(function (token) {
              console.log("FCM Token:", token);
              // Send this to your server if needed
            }, function (error) {
              console.error("Token error:", error);
            });
          
            // Listen for push messages
            FirebasePlugin.onMessageReceived(function (message) {
              console.log("Push received:", message);
              alert(message.body); // or show your own notification
            }, function (error) {
              console.error("Push error:", error);
            });
          });
          
    }
  });
  