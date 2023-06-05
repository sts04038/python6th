# #변수 선언
# a = 10                  # a:  <class 'int'>
# b =3.14                 # b:  <class 'float'>
# c = "Hello, world"      # c:  <class 'str'>
# d = [1, 2, 3]           # d:  <class 'list'> List [] 순서를 가지는 객체의 집합
# e = (4, 5, 6)           # e:  <class 'tuple'> Tuple(튜플) - 속도가 list보다 빠름, 근데 add가 안됨
# f = {7, 8, 9}           # f:  <class 'set'> 집합, 중복 안됨. 순서 없음
# g = {"apple": 1, "banana": 2, "orange": 3} # g:  <class 'dict'> 사전에서는 키에 대한 중복이 허용안됨
#
# # 데이터 타입 출력
# print("a: ", type(a))   # a:  <class 'int'>
# print("b: ", type(b))   # b:  <class 'float'>
# print("c: ", type(c))   # c:  <class 'str'>
# print("d: ", type(d))   # d:  <class 'list'>
# print("e: ", type(e))   # e:  <class 'tuple'>
# print("f: ", type(f))   # f:  <class 'set'>
# print("g: ", type(g))   # g:  <class 'dict'>

# 연산자
a = 4
b = 2
# 덧셈
print("total = a + b :", a + b) # total = a + b : 6
# 뺄셈
print("total = a - b :", a - b) # total = a - b : 2
# 곱셈
print("total = a * b :", a * b) # total = a * b : 8
# 나눗셈
print("total = a / b :", a / b) # total = a / b : 2.0
# 나머지
print("total = a % b :", a % b) # total = a % b : 0
# 거듭제곱
print("total = a ** b :", a ** b) # total = a ** b : 16
# 몫 (양수)
print("total = a // b :", a // b) # total = a // b : 2
# 몫 (음수)
c = -5
print("total = c // b :", c // b) # total = c // b : -3

# 비교 연산자
a = 5
b = 2
print('a < b: ', a < b)   # a < b:  False
print('a <= b: ', a <= b) # a <= b:  False
print('a == b: ', a == b) # a == b:  False
print('a != b: ', a != b) # a != b:  True

# 논리 연산자
a = 5
b = 2
c = 3
d= 200

#AND 연산자
print('a > b and a > c: ', a > b and a > c) # a > b and a > c:  True
#OR 연산자
print('a > b or a > c: ', a > b or a > c)   # a > b or a > c:  True
#NOT 연산자
print('a > b and a > c: ', not(a < b))      # a > b and a > c:  True
