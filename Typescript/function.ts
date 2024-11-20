// Function to calculate grade based on marks
function gradeCalculator(math: number, english: number, history: number): void {
    // Calculate the average
    const average = (math + english + history) / 3;

    let grade: string;
    if (average >= 90) {
        grade = "A";
    } else if (average >= 80) {
        grade = "B";
    } else if (average >= 70) {
        grade = "C";
    } else {
        grade = "below average";
    }

    // Print the results
    console.log(`Marks: Maths = ${math}, English = ${english}, History = ${history}`);
    console.log(`Average: ${average.toFixed(2)}`);
    console.log(`Grade: ${grade}`);
}

const mathMarks: number = Number(prompt("Enter marks for Maths:"));
const englishMarks: number = Number(prompt("Enter marks for English:"));
const historyMarks: number = Number(prompt("Enter marks for History:"));
