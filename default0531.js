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

// 함수 자체를 변수로 담는 법 - react에서 자주 쓰임
// Example 1: IIFE (Immediately-Invoked Function Expression)
(function display(message) {
    console.log(message);
})("hi");

// Example 2: Function expression assigned to a variable
var display2 = function displayMessage(msg) {
    console.log(msg);
};
display2("I am message");

// Example 3: IIFE with arguments
(function addNumbers(a, b) {
    console.log(a + b);
})(3, 4);
