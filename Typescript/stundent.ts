class Student {
    id: number;
    name: string;
    age: number;

    constructor(id: number, name: string, age: number) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
}

// Create an array of student objects
const students: Student[] = [
    new Student(1, "Alice", 20),
    new Student(2, "Bob", 22),
    new Student(3, "Charlie", 21),
];

// Print the student details using destructuring in a for loop
for (const { id, name, age } of students) {
    console.log(`ID: ${id}, Name: ${name}, Age: ${age}`);
}
