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

// Function to calculate percentage

const mark = document.getElementById('mark');
const maxMark = document.getElementById('maxMark');


function calculatePercentage() {
    const markValue = parseFloat(mark.value);
    const maxMarkValue = parseFloat(maxMark.value);

    if (!isNaN(markValue) && !isNaN(maxMarkValue) && maxMarkValue !== 0) {
        const percentage = (markValue / maxMarkValue) * 100;
        localStorage.setItem('percentage', percentage.toFixed(2));
        return percentage.toFixed(2);
    } else {
        alert("Please enter valid numbers for both marks.");
        return null;
    }
}

function submitInfo() {
    const percentage = calculatePercentage();
    window.location.href = `http://localhost:8000/gradeoutput.html?percentage=${percentage}`;
    
}

