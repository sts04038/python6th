//document.write("Hello, world")
//document.write("<h1> Welcome to JS Program</h1>")
//document.write("<h2> Welcome to JS Program</h2>")
//
//console.log('Welcome JS Program');
//console.info('Welcome JS Program');
//console.warn('Welcome JS Program');
//console.error('Welcome JS Program');
//
//alert('Welcome JS Program') // 팝업창 뜸 - 웬만하면 사용하지 않음 - 제일 먼저 실행되고 사용자 당황함
//var a = prompt('Welcome to JS Program');
//console.log(a)

//typeof - 변수 타입 알려줌
//console.log(typeof 123);            // number
//console.log(123.5, typeof 123.5);   // 123.5, "number"
//console.log(typeof "123");          // string
//console.log(typeof true);           // boolean
//console.log(typeof false);          // boolean
//
//var car;
//var car = "";
//
//var person
//var person = { firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" };
//console.log(person)
//console.log(typeof person); // object
//person = null;

// 4교시 시작
var name = "이승훈"
var age = 29;
var cgpa = 3.92;
var lineBreak = "<br/>"

document.write("이름: " + name + lineBreak);
document.write("나이: " + age + lineBreak);
document.write("학점: " + cgpa + lineBreak);

var text = prompt("Enter your name");
document.write("Your name : " + text + "<br/>");

var len = text.length;         // 전체 글자수 띄어쓰기 포함됨
document.write("Number of characters : " + len + "<br/>");

document.write(text.charAt(2) + "<br/>");
document.write(text.toUpperCase() + "<br/>");
document.write(text.toLowerCase() + "<br/>");

var text1 = "hi ";
var text2 = "bye";
// + 기호와 concat은 같은 기능을 한다.
var text3 = text1.concat(text2);     //hi bye
var text4 = text1 + text2;           //hi bye
document.write(text3 + "<br/>");
document.write(text4 + "<br/>");

var text5 = "hello";
var result = text5.slice(0,2);      // he 출력됨 - 0,1번째 글짜 출력
var result = text5.slice(2);      // llo 출력됨 - 0,1번째 글짜 출력
document.write(result + "<br/>");

