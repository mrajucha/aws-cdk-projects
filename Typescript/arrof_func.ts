// Arrow function to check if a number is prime

// Example usage
let number = Number(prompt("Enter a number to check if it's prime:"));

const isPrime = (num: number): boolean => {
    if (num <= 1) return false; 
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false; 
        }
    }
    return true; 
};




