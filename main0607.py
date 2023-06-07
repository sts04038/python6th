# # if문
# age = 18
# if age >= 18:
#     print("adult")
# else:
#     print("under age")
#
# # 중첩된 if else
# score = 50
# if score >= 90:
#     print("A 학점")
# else:
#     if score >= 70:
#         print("C학점")
#     else:
#         print("fail")
#
# # if else
# marks = 75
# if marks >= 90:
#     print("rankA")
# elif marks >= 80:
#     print("rankB")
# elif marks >= 70:
#     print("rankC")
# else:
#     print("rankD")
#
# # 입력을 이용한 if 문
# a = int(input("Enter Number Greater then 2: "))
# if a > 2:
#     print("You have Entered: ", a)
# else:
#     print("Wrong! You have entered: ", a)
#
# day = input("요일을 입력하세요: ")
# day = day.lower()  # Convert the input to lowercase
#
# if day == "mon" or day == "monday":
#     print("오늘은 월요일")
# else:
#     print("월요일이 아니네요")

# while 문
a = 2
while a <= 20:
    print(a)
    a += 6
else:
    print("While 조건이 거짓이므로 else 부분 실행: 코드 종료")
# 무한 루프
i = 0
while True:
    i += 1
    print(i)
    if i >= 5:
        break
print("code end")

# range
for i in range(2,7):
    print(i)

print("reverse Range with start, stop, step")
r = range(5, 0, -1)
print(r[0]) # output: 5
print(r[1]) # output: 4
print(r[2]) # output: 3
print(r[3]) # output: 2
print(r[4]) # output: 1

# for in
st = "멋쟁이 사자"
for ch in st:
    print(ch)
else:
    print("Else")

# pass
a = 5
if a < 6:
    pass
else:
    print("bigger than 6")