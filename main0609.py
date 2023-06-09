# # 상속
# class Mobile:
#     fp = 'yes'
#
# realme = Mobile()
# redme = Mobile()
# geek = Mobile()
#
# print(Mobile.fp)    # yes
# print(realme.fp)    # yes
# print(redme.fp)     # yes
# print(geek.fp)      # yes
#
# Mobile.fp = 'no'
# print(Mobile.fp)    # no
# print(realme.fp)    # no
# print(redme.fp)     # no
# print(geek.fp)      # no
#
# realme.fp = 'Not Working'
# print(Mobile.fp)    # no
# print(realme.fp)    # no
# print(redme.fp)     # Not working
# print(geek.fp)      # no
import time
# class Vector:
#     #  __init__ 메소드는 객체 초기화를 담당합니다. 클래스로부터 새 객체를 만들 때마다 호출됩니다.
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     # __add__ 메소드는 + 연산자를 오버로드합니다. 이 메소드를 재정의하면, 두 Vector 객체를 + 연산자로 더할 수 있게 됩니다.
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#     # __str__ 메소드는 객체를 문자열로 나타내는 방법을 정의합니다. 이 메소드를 재정의하면, print() 함수로 객체를 출력할 때 사용자가 정의한 형식대로 출력됩니다.
#     def __str__ (self):
#         return  f'Vector({self.x}, {self.y})'
#
# a = Vector(1,2) # output: <__main__.Vector object at 0x109574bd0>
# b = Vector(3,4) # # output: <__main__.Vector object at 0x109574bd0>
#
# print(a)    # output: Vector(1, 2)      __str__ 없다면: <__main__.Vector object at 0x109574bd0>
# print(b)    # output: Vector(3, 4)      __str__ 없다면: <__main__.Vector object at 0x109574bd0>
# c = a + b
# print(c)    # output: Vector(4, 6)

# import time
# from datetime import datetime
# from datetime import date
#
# dt = datetime(year=2023, month=5, day=5, hour=10, minute=30)
# print(dt)       # 2023-05-05 10:30:00
# print(type(dt)) # <class 'datetime.datetime'>
#
# current_time = time.ctime()
# current_datetime = datetime.now()
# print(current_datetime, current_time) # 2023-06-09 10:47:13.013777 Fri Jun  9 10:47:13 2023
#
# d = date(year=2023, month=6, day=25)
# print(d)    # 2023-06-25
#
# current_date = date.today()
# print(current_date) # 2023-06-09

class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self):
        return f'ParentClass name : {self.name}, number : {self.number}'
    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.number = self.number + new_number

class ChildClass (ParentClass):
    def __init__(self):
        super().__init__()
        self.name = 'child'
    def add_num(self, new_number):
        print('말 안듣는 자식 : 고정적으로 5 더할건데? ')
        self.number = self.number + 5

parent = ParentClass()
child =ChildClass()
print(parent)   # ParentClass name : parent, number : 10
print(child)    # ParentClass name : child, number : 10

print('7일 더하세요') # 7일 더하세요
parent.add_num(7) # 부모 :  7 만큼 더해야지
child.add_num(7) # 말 안듣는 자식 : 고정적으로 5 더할건데?
print(parent)   # ParentClass name : parent, number : 10
print(child)    # ParentClass name : child, number : 15

from datetime import timedelta, datetime
from datetime import date

td = timedelta(days=10)
print(td) # 10 days, 0:00:00

d1 = date(year=2023, month=5, day=5)
d2 = date(year=2023, month=6, day=9)

print(d1 == d2) # False
print(d1 < d2)  # True
print(d1 > d2)  # False

dt = datetime.today()
formatted_datetime = dt.strftime('%B, %d, %Y')
print(formatted_datetime) # June, 09, 2023