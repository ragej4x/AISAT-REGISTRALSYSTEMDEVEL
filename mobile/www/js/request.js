//192.0.0.1
//sa port 5000 or 55000 conf
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const username = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;


    const data = { username, email, password };

    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert('Login successful!');
        } else {
            alert('Login failed: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});

