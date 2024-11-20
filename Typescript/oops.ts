// define properties and methods
interface EmployeeDetails {
    employeeId: number;
    department: string;
    getDetails(): string;
}

// Base class
class Person {
    protected name: string;
    protected age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    introduce(): string {
        return `Hello, my name is ${this.name}, and I am ${this.age} years old.`;
    }
}

// Inheritance that derives from person and implements interface
class Employee extends Person implements EmployeeDetails {
    employeeId: number;
    department: string;

    constructor(name: string, age: number, employeeId: number, department: string) {
        super(name, age);
        this.employeeId = employeeId;
        this.department = department;
    }

    getDetails(): string {
        return `Employee ID: ${this.employeeId}, Department: ${this.department}`;
    }

    // Overriding the introduce method from Person
    introduce(): string {
        return `${super.introduce()} I work in the ${this.department} department.`;
    }
}

// Usage
const employee = new Employee("Alice", 30, 12345, "Engineering");

console.log(employee.introduce()); 
console.log(employee.getDetails()); 
