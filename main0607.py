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

# dictionary
stu = {101: 'Kim', 102: 'Bae', 103: 'Park'}
fees = {'Kim': 2000, 'Bae': 3000, 'Park': 8000}

print(stu[101])     # output: Kim
print(fees['Park']) # output: 8000

# 수정 하는 법
stu[102] = 'Python'
print(stu)          # output: {101: 'Kim', 102: 'Python', 103: 'Park'}

# 추가 하는 법
stu[104] = 'John'
print(stu)          # output: {101: 'Kim', 102: 'Python', 103: 'Park', 104: 'John'}

# 삭제 하는 법
del stu[102]
print(stu)          # output: {101: 'Kim', 103: 'Park', 104: 'John'}

# 있니 없니 멤버 in 이용해서 찾기
print(102 in stu)     # output: False
print(102 not in stu) # output: True

# 복사하기
new_stu = stu.copy()

#
key = (101, 102, 103)
value = 'Lion'
new1_stu = dict.fromkeys(key, value)

print(new1_stu) # output: {101: 'Lion', 102: 'Lion', 103: 'Lion'}

# 접근하는 방법들
print(new_stu)      # output: {101: 'Kim', 103: 'Park', 104: 'John'}
print(stu[101])     # output: Kim
print(stu.get(101)) # output: Kim (함수로 호출하는 법)
print(stu.items())  # output: dict_items([(101, 'Kim'), (103, 'Park'), (104, 'John')])
print(stu.keys())   # output: dict_keys([101, 103, 104])

# update
stu.update({103: 'Lion 2'})
print(stu)          # output: {101: 'Kim', 103: 'Lion 2', 104: 'John'}

# pop
print(stu.pop(104)) # John - 삭제된 value
print(stu)          # {101: 'Kim', 103: 'Lion 2'}

# setdefault
name = stu.setdefault(104, 'Pep')
print(stu)          # {101: 'Kim', 103: 'Lion 2', 104: 'Pep'}
print(name)         # pep