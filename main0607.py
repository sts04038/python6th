# # set
# a = {10, 20, 30}
# a = {10, 20, 30, "Like Lion", "Park", 40}
# a = {10, 20, 30, "Like Lion", "Park", 40, 10, 20}
#
# b = set()
# print(type(b))          # output: <class 'set'>
# a.add(50)
# a.update([10, 20, 60, 70])
# print(a)                # output: {70, 10, 'Park', 20, 'Like Lion', 30, 40, 50, 60}
# a.remove('Like Lion')
# a.discard('Like Lion')
# a.discard(70)
# print(a)                # output: {10, 'Park', 20, 30, 40, 50, 60}
#
# new_set = a.copy()
# print(new_set)          # output: {'Park', 50, 20, 40, 10, 60, 30}
#
# new_set.clear()
# print(new_set)          # output: set()
#
# intersection_a_new = a.intersection(new_set, a, b)
# print(intersection_a_new)               # output: set()
#
# union_a = a.union(new_set)
# print('union_a: ', union_a)             # output: union_a:  {'Park', 50, 20, 40, 10, 60, 30}
#
# difference_a = a.difference(new_set)
# print('difference_a: ', difference_a)   # output: difference_a:  {50, 20, 40, 10, 60, 'Park', 30}
#
# print(b.issubset(a))    # output: True
# print(a.issuperset(b))  # output: True

# # dictionary
# stu = {101: 'Kim', 102: 'Bae', 103: 'Park'}
# fees = {'Kim': 2000, 'Bae': 3000, 'Park': 8000}
#
# print(stu[101])     # output: Kim
# print(fees['Park']) # output: 8000
#
# # 수정 하는 법
# stu[102] = 'Python'
# print(stu)          # output: {101: 'Kim', 102: 'Python', 103: 'Park'}
#
# # 추가 하는 법
# stu[104] = 'John'
# print(stu)          # output: {101: 'Kim', 102: 'Python', 103: 'Park', 104: 'John'}
#
# # 삭제 하는 법
# del stu[102]
# print(stu)          # output: {101: 'Kim', 103: 'Park', 104: 'John'}
#
# # 있니 없니 멤버 in 이용해서 찾기
# print(102 in stu)     # output: False
# print(102 not in stu) # output: True
#
# # 복사하기
# new_stu = stu.copy()
#
# #
# key = (101, 102, 103)
# value = 'Lion'
# new1_stu = dict.fromkeys(key, value)
#
# print(new1_stu) # output: {101: 'Lion', 102: 'Lion', 103: 'Lion'}
#
# # 접근하는 방법들
# print(new_stu)      # output: {101: 'Kim', 103: 'Park', 104: 'John'}
# print(stu[101])     # output: Kim
# print(stu.get(101)) # output: Kim (함수로 호출하는 법)
# print(stu.items())  # output: dict_items([(101, 'Kim'), (103, 'Park'), (104, 'John')])
# print(stu.keys())   # output: dict_keys([101, 103, 104])
#
# # update
# stu.update({103: 'Lion 2'})
# print(stu)          # output: {101: 'Kim', 103: 'Lion 2', 104: 'John'}
#
# # pop
# print(stu.pop(104)) # John - 삭제된 value
# print(stu)          # {101: 'Kim', 103: 'Lion 2'}
#
# # setdefault
# name = stu.setdefault(104, 'Pep')
# print(stu)          # {101: 'Kim', 103: 'Lion 2', 104: 'Pep'}
# print(name)         # pep

# def val(lst):
#     print("Inside Function Before Append: ", lst, id(lst))
#     lst.append(4)
#     print("Inside Function Before Append: ", lst, id(lst))
#
# list = [1, 2, 3]
# print("Before Calling Function: ", list, id(list))

# def val(x):
#     print("Inside : ", x, id(x))
#     x += 1
#     print("Inside After: ", x, id(x))
#
# x = 10
# print("Before Calling: ", x, id(x))     # output: Before Calling:  10 4498734456
# val(x)
# # output:
# # Inside :  10 4498734456
# # Inside After:  11 4498734488
# print("After Calling: ", x, id(x))      # output: After Calling:  10 4498734456
#

# show = lambda x: print(x)
# show(5)
# add = lambda x, y: (x+y, x-y)
# a, s = add(5, 2)
#
# add_sub = lambda x, y: (x+y, x-y)
# a, s = add(5, 2)
#
# print(a)
# print(s)

# decorate
def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add
    return inner

def num():
    return 10

result_fun = decor(num)
print(result_fun())  # output: 15

# 파이썬의 장점중 하나
@decor
def num():
    return 10

print(num())

from array import *
def show(ar):
    print("Passed Array ar: ", ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar
print()

a = array('i', [101, 102, 103, 104])
y = show(a)
print("Return Array Y: ", y)  # output: Return Array Y:  array('i', [101, 102, 103, 104])
print(type(y))                # output: <class 'array.array'>