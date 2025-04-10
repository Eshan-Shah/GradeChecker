function toInputsPage() {
    window.location.href = 'http://127.0.0.1:3000/userinputs.html'

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
    const examLevel = document.querySelector('#examLevel input[name="examLevel"]:checked')
    const examBoard = document.querySelector('#examBoard input[name="examBoard"]:checked')
    const subject = document.querySelector('input[name="whichSubject"]')
    const urlParams = `?percentage=${percentage}&board=${examBoard.value}&level=${examLevel.value}&subject=${subject.value}`
    window.location.href = `http://127.0.0.1:3000/gradeoutput.html` + urlParams;
    
}

