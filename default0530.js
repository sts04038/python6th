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
//
//typeof - 변수 타입 알려줌
//console.log(typeof 123);            // number
//console.log(123.5, typeof 123.5);   // 123.5, "number"
//console.log(typeof "123");          // string
//console.log(typeof true);           // boolean
//console.log(typeof false);          // boolean

//var car;
//var car = "";
//
//var person
//var person = { firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" };
//console.log(person)
//console.log(typeof person); // object
//person = null;

//// 4교시 시작
//var name = "이승훈"
//var age = 29;
//var cgpa = 3.92;
//var lineBreak = "<br/>"
//
//document.write("이름: " + name + lineBreak);
//document.write("나이: " + age + lineBreak);
//document.write("학점: " + cgpa + lineBreak);
//
//var text = prompt("Enter your name");
//document.write("Your name : " + text + "<br/>");
//
//var len = text.length;         // 전체 글자수 띄어쓰기 포함됨
//document.write("Number of characters : " + len + "<br/>");
//
//document.write(text.charAt(2) + "<br/>");
//document.write(text.toUpperCase() + "<br/>");
//document.write(text.toLowerCase() + "<br/>");
//
//var text1 = "hi ";
//var text2 = "bye";
//// + 기호와 concat은 같은 기능을 한다.
//var text3 = text1.concat(text2);     //hi bye
//var text4 = text1 + text2;           //hi bye
//document.write(text3 + "<br/>");
//document.write(text4 + "<br/>");
//
//var text5 = "hello";
//var result = text5.slice(0,2);      // he 출력됨 - 0,1번째 글짜 출력
//var result = text5.slice(2);      // llo 출력됨 - 0,1번째 글짜 출력
//document.write(result + "<br/>");

//// 5교시 시작
//var num = "20";
//num = num.toString();
//console.log(typeof num);        // string 출력
//
//var number = 20;
//console.log(typeof number);     // number 출력
//number = number.toString();
//console.log(number, typeof number);     // 20 string 출력
//
//var x = 2.56789
//// toFixed(a) 소수점 a번째까지 표시 (반올림해서)
//console.log(x.toFixed(1), typeof x.toFixed(1));     // 2.6 string 출력
//console.log(x.toFixed(2));                          // 2.57 출력
//
//console.log(x.toPrecision(1), typeof x.toFixed(1));     // 3 string 출력
//console.log(x.toPrecision(2));                          // 2.6 출력
//
//// Number(a) : a의 type을 숫자 object로 바꿔줌
//console.log(Number(true));                          // 1 출력
//console.log(Number(false));                         // 0 출력
//console.log(Number(" 10"));                         // 10 출력
//console.log(Number(" 10"));                         // 10 출력
//console.log(Number(" 10.25"));                     // 10.25
//
//// pareInt : parses a string and returns an integer. It attempts to convert the provided string into an integer representation.
//// personal ex
//var str = "42";
//var num = parseInt(str);
//
//console.log(num); // Output: 42
//console.log(typeof num); // Output: number
//
//// class ex 계산기 만들기
//var num1 = parseInt(prompt("Enter first number: "));
//var num2 = parseInt(prompt("Enter second number: "));
//var lineBreak = "<br/>"
//
//var result = num1 + num2;
//document.write("the sum is: " + result + lineBreak);
//
//var result = num1 - num2;
//document.write("the sub is: " + result + lineBreak);
//
//var result = num1 * num2;
//document.write("the multiplication is: " + result + lineBreak);
//
//var result = num1 / num2;
//document.write("the division is: " + result + lineBreak);
//
//var result = num1 % num2;
//document.write("the remainder is: " + result + lineBreak);

var base = parseFloat(prompt("밑변 입력: "));
var height = parseFloat(prompt("높이 입력: "));

var area = base * height * 0.5;
document.write("삼각형의 넓이: " + area);
