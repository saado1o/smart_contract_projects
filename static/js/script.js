// Ensure the DOM is fully loaded before executing scripts
document.addEventListener('DOMContentLoaded', () => {
    // Get the form and attach a submit event listener
    const form = document.getElementById('addTransactionForm');
    if (form) {
        form.addEventListener('submit', handleAddTransaction);
    }
});

/**
 * Handles the submission of the "Add Transaction" form.
 * Sends the transaction data to the backend via a POST request.
 * @param {Event} event - The form submission event.
 */
async function handleAddTransaction(event) {
    // Prevent default form submission behavior
    event.preventDefault();

    // Get form input values
    const sender = document.getElementById('sender').value.trim();
    const receiver = document.getElementById('receiver').value.trim();
    const amount = document.getElementById('amount').value.trim();

    // Input validation
    if (!sender || !receiver || !amount) {
        alert('All fields are required.');
        return;
    }

    // Check if the amount is a valid number
    if (isNaN(amount) || amount <= 0) {
        alert('Amount must be a valid number greater than zero.');
        return;
    }

    try {
        // Create a POST request to send data to the backend
        const response = await fetch('/add_transaction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                sender,
                receiver,
                amount,
            }),
        });

        // Parse the JSON response
        const result = await response.json();

        // Handle the response from the backend
        if (response.ok) {
            alert(result.message || 'Transaction added successfully!');
            document.getElementById('addTransactionForm').reset(); // Reset form
        } else if (response.status === 400) {
            alert(result.error || 'Invalid request. Please check the form fields.');
        } else {
            alert(result.error || 'An error occurred while adding the transaction.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to connect to the server. Please try again later.');
    }
}
