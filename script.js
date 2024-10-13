const form = document.querySelector('form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const fromCurrency = document.getElementById('from_currency').value;
    const toCurrency = document.getElementById('to_currency').value;

    try {
        const response = await fetch(`/api/v1/${from_currency}-${to_currency}`);
        const data = await response.json();
        resultDiv.textContent = `Conversion rate: ${data.rate}`;
    } catch (error) {
        console.error('Error fetching rate:', error);
        resultDiv.textContent = 'Error fetching rate';
    }
});
