#변수 선언
a = 10                  # a:  <class 'int'>
b =3.14                 # b:  <class 'float'>
c = "Hello, world"      # c:  <class 'str'>
d = [1, 2, 3]           # d:  <class 'list'> List [] 순서를 가지는 객체의 집합
e = (4, 5, 6)           # e:  <class 'tuple'> Tuple(튜플) - 속도가 list보다 빠름, 근데 add가 안됨
f = {7, 8, 9}           # f:  <class 'set'> 집합, 중복 안됨. 순서 없음
g = {"apple": 1, "banana": 2, "orange": 3} # g:  <class 'dict'> 사전에서는 키에 대한 중복이 허용안됨

# 데이터 타입 출력
print("a: ", type(a))   # a:  <class 'int'>
print("b: ", type(b))   # b:  <class 'float'>
print("c: ", type(c))   # c:  <class 'str'>
print("d: ", type(d))   # d:  <class 'list'>
print("e: ", type(e))   # e:  <class 'tuple'>
print("f: ", type(f))   # f:  <class 'set'>
print("g: ", type(g))   # g:  <class 'dict'>
