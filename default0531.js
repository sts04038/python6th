//// 4교시 code 함수 연습
//function message() {
//    document.write("Hello, I am a function without parameters" + "<br/>");
//}
//
//function welcomeMessage(name) {
//    document.write("Welcome, " + name + "<br/>");
//}
//
//function additional(num1, num2) {
//    var sum = num1 + num2;
//    document.write("The addition is " + sum + "<br/>");
//}
//
//function square(num) {
//    return num * num;
//}
//
//message();
//welcomeMessage("John");
//additional(2, 3);
//document.write("The square of 5 is " + square(5) + "<br/>");

//// 함수 자체를 변수로 담는 법 - react에서 자주 쓰임
//// Example 1: IIFE (Immediately-Invoked Function Expression)
//(function display(message) {
//    console.log(message);
//})("hi");
//
//// Example 2: Function expression assigned to a variable
//var display2 = function displayMessage(msg) {
//    console.log(msg);
//};
//display2("I am message");
//
//// Example 3: IIFE with arguments
//(function addNumbers(a, b) {
//    console.log(a + b);
//})(3, 4);


var names = new Array(20);
names[0] = "John";
names[1] = "Dean";

console.log(names[1]);

// Create an array with values
var students = ["John", "Dean", "Diane", "Anna"];
console.log("Students = " + students);
console.log("Student at index 2 = " + students[2]);

// Find the length of the array
console.log("Length of the students array: " + students.length);

// Add elements to the array
students.push("Luna");
console.log("Array after push operation: " + students);

// Remove elements from the array
students.pop();
console.log("Array after pop operation: " + students);

// Concatenate arrays
var numArray1 = [10, 20];
var numArray2 = [10, 40, 50, 60];
var numArray = numArray1.concat(numArray2);

console.log("Array concatenation: " + numArray);
console.log(numArray1.concat(numArray2));
