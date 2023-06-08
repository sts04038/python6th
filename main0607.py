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

# # while 문
# a = 2
# while a <= 20:
#     print(a)
#     a += 6
# else:
#     print("While 조건이 거짓이므로 else 부분 실행: 코드 종료")
# # 무한 루프
# i = 0
# while True:
#     i += 1
#     print(i)
#     if i >= 5:
#         break
# print("code end")
#
# # range
# for i in range(2,7):
#     print(i)
#
# print("reverse Range with start, stop, step")
# r = range(5, 0, -1)
# print(r[0]) # output: 5
# print(r[1]) # output: 4
# print(r[2]) # output: 3
# print(r[3]) # output: 2
# print(r[4]) # output: 1
#
# # for in
# st = "멋쟁이 사자"
# for ch in st:
#     print(ch)
# else:
#     print("Else")
#
# # pass
# a = 5
# if a < 6:
#     pass
# else:
#     print("bigger than 6")

# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105])
# print(stu_roll)                 # output: array('i', [101, 102, 103, 104, 105])
#
# # insert
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# print(stu_roll)                 # output: array('i', [101, 106, 102, 107, 103, 104, 105])
# # pop
# stu_roll.pop() # 맨 마지막 요소 제거
# print(stu_roll)                 # output: array('i', [101, 106, 102, 107, 103, 104])
# # index 메소드
# print(stu_roll.index(103))      # output: 4
# # extend : 배열을 뒤에 붙히는 것
# arr = array('i', [201, 208, 289])
# stu_roll.extend(arr)
# print(stu_roll) # output: array('i', [101, 106, 102, 107, 103, 104, 201, 208, 289])
# # reverse - 뒤에서 부터 역순 (최신 자료를 가져오려고 할 때 자주 사용함)
# stu_roll.reverse()
# print(stu_roll) # output: array('i', [289, 208, 201, 104, 103, 107, 102, 106, 101])
#
# # 슬라이싱 [start:stop:stepsize]
# print(stu_roll[1:3])    # output: array('i', [208, 201])
# print(stu_roll[-4:])    # 마지막 요소 4개 출력 output: array('i', [107, 102, 106, 101])
#
# a = stu_roll[0:7:2]     # 0부터 6번째까지 2개씩 건너뛰어 출력
# print(a)                # output: array('i', [289, 201, 103, 102])
#
# str = '''
# 동해물과 백두산이마르고 닮도록
# 하느님이 보우하사
# '''
# print(str)

# # 문자열 함수
# s = "Hello From The Other Side"
# print(s.upper())    # HELLO FROM THE OTHER SIDE
# print(s.lower())    # hello from the other side
# print(s.swapcase()) # hELLO fROM tHE oTHER sIDE
# print(s.title())    # Hello From The Other Side
# print(s.isupper())  # False
# print(s.islower())  # False
# print(s.istitle())  # True
# print(s.isdigit())  # True
# print(s.isalpha())  # False
#
# # strip 문자열 메소드: 문자열의 시작과 끝에 있는 공백(스페이스, 탭, 개행)을 제거하는 데 사용됩니다.
# b = "  Hello From The Other Side   "
# print(b.lstrip())  # "Hello From The Other Side    "
# print(b.rstrip())  #"   Hello From The Other Side"
# print(b.strip())  # "Hello From The Other Side"
#
# text = "***Hello, World!***"
# print(text.strip("*"))  # Output: "Hello, World!"
#
# # replace, split
# a = "Hello, friend"
# print(a.replace("friend", "there"))  # Hello, there
# split_str = a.split(",")
# print(split_str)                     # ['Hello', ' friend']
# print(" ".join(split_str))           # Hello  friend
# print(a.startswith("Hello"))         # True

# def disp(sh):
#     print(type(sh))
#     print("Disp Function " + sh())
#
# def show():
#     return "Show Function"
#
# disp(show)

# output
# <class 'function'>
# Disp Function Show Function

# def disp():
#     def show():
#         return "Show Function"
#     print("Disp Function")
#     return show()
# r_sh = disp()
# print(r_sh)

# output:
# Disp Function
# Show Function