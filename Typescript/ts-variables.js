// Basic variable types in TS
var my_name = "Manoj Chaudhary";
var total = 100;
var marks;
(function (marks) {
    marks[marks["maths"] = 35.5] = "maths";
    marks[marks["English"] = 35.5] = "English";
    marks[marks["science"] = 35.5] = "science";
    marks[marks["social"] = 35.5] = "social";
})(marks || (marks = {}));
var marks_average = 35.5;
console.log("Hello Guys " + "My name is" + my_name + " total marks " + total + " And I have received " + marks_average + " " + marks);
