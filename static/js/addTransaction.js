// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
    // Attach the form submit event handler
    const form = document.getElementById('addTransactionForm');
    if (form) {
        form.addEventListener('submit', handleAddTransaction);
    }
});

/**
 * Handles the form submission to add a transaction
 * @param {Event} event
 */
async function handleAddTransaction(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Retrieve form field values
    const sender = document.getElementById('sender').value.trim();
    const receiver = document.getElementById('receiver').value.trim();
    const amount = document.getElementById('amount').value.trim();

    // Validate the inputs
    if (!sender || !receiver || !amount || isNaN(amount) || amount <= 0) {
        alert('Please fill in all fields correctly.');
        return;
    }

    try {
        // Send the POST request to the backend
        const response = await fetch('/add_transaction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sender, receiver, amount }),
        });

        // Parse the JSON response
        const result = await response.json();

        // Handle success or error response
        if (response.ok) {
            alert(result.message || 'Transaction added successfully!');
            // Optionally, reset the form fields
            document.getElementById('addTransactionForm').reset();
        } else {
            alert(result.error || 'Failed to add transaction.');
        }
    } catch (error) {
        console.error('Error adding transaction:', error);
        alert('An error occurred while adding the transaction. Please try again.');
    }
}
