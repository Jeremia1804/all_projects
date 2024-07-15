document.getElementById('codeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let codeInput = document.getElementById('codeInput').value;

    fetch('/sardinas-patterson', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: codeInput })
    })
    .then(response => response.json())
    .then(data => {
        let a = document.querySelector('#resultSardinas span');
        let b = document.querySelector('#resultOther span');

        a.textContent = data.sardinas;
        if(data.learning == "Not a code"){
            b.style.color = "red";
        }else{
            b.style.color = "green";
        }
        document.querySelector('#resultOther span').textContent = data.learning;
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('learn').addEventListener('click', function() {

    fetch('/learn', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
    })
    .catch(error => console.error('Error:', error));
});
