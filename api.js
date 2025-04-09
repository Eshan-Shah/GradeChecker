function toInputsPage() {
    const url = 'http://localhost:8000/userinputs.html'
    window.location.href = url

}
// Functionality for slider max values.

const maxMarkInput = document.getElementById('maxMark');
const markInput = document.getElementById('mark');
const maxMarkDisplay = document.getElementById('maxMarkDisplay');
const markDisplay = document.getElementById('markDisplay');

function updateMax() {
    const maxValue = parseInt(maxMarkInput.value);
    maxMarkDisplay.textContent = maxValue;
    markInput.max = maxValue;

    if (parseInt(markInput.value) > maxValue) {
        markInput.value = maxValue;
        markDisplay.textContent = maxValue;
    }
}

maxMarkInput.addEventListener('input', updateMax);

markInput.addEventListener('input', () => {
    markDisplay.textContent = markInput.value;
});

updateMax();
