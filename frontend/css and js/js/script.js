// This is the function used to submit the question and get the answer from the backend
function submitQuestion() {

    document.querySelector(".loading-message-sql").style.display = "inline-block";
    document.querySelector(".loading-message-answer").style.display = "inline-block";

    // Get the question from the textarea
    const question = document.querySelector(".question").value;

    // Send the question to Flask backend using AJAX
    fetch('/result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "question": question })
    })
    .then(response => response.json())
    .then(data => {
        // Update the page with the result
        document.querySelector('.sql').value = data.sql_query;
        document.querySelector('.answer').value = data.answer;

        document.querySelector(".loading-message-sql").style.display = "none";
        document.querySelector(".loading-message-answer").style.display = "none";
    })
    .catch(error => {
        console.error('Error:', error);
        document.querySelector(".loading-message-sql").style.display = "none";
        document.querySelector(".loading-message-answer").style.display = "none";
    });
}

// Clear the answers from the textarea
function clearButton(){
    document.querySelector(".sql").value = "";
    document.querySelector(".answer").value = "";
}

