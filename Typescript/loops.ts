// Function to print numbers up to the given limit using a for loop
function printUsingForLoop(limit: number): void {
    console.log("Using for loop:");
    for (let i = 1; i <= limit; i++) {
        if (i % 5 === 0) {
            continue; // Skip multiples of 5
        }
        console.log(i);
    }
}

// Prompt the user for input
const input = prompt("Enter a number:");
const limit = Number(input);

// Validate the input
if (isNaN(limit) || limit <= 0) {
    alert("Please enter a valid positive number.");
} else {
    // Call both functions
    printUsingForLoop(limit);
}
