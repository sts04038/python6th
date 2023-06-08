# set
a = {10, 20, 30}
a = {10, 20, 30, "Like Lion", "Park", 40}
a = {10, 20, 30, "Like Lion", "Park", 40, 10, 20}

b = set()
print(type(b))          # output: <class 'set'>
a.add(50)
a.update([10, 20, 60, 70])
print(a)                # output: {70, 10, 'Park', 20, 'Like Lion', 30, 40, 50, 60}
a.remove('Like Lion')
a.discard('Like Lion')
a.discard(70)
print(a)                # output: {10, 'Park', 20, 30, 40, 50, 60}

new_set = a.copy()
print(new_set)          # output: {'Park', 50, 20, 40, 10, 60, 30}

new_set.clear()
print(new_set)          # output: set()

intersection_a_new = a.intersection(new_set, a, b)
print(intersection_a_new)               # output: set()

union_a = a.union(new_set)
print('union_a: ', union_a)             # output: union_a:  {'Park', 50, 20, 40, 10, 60, 30}

difference_a = a.difference(new_set)
print('difference_a: ', difference_a)   # output: difference_a:  {50, 20, 40, 10, 60, 'Park', 30}

print(b.issubset(a))    # output: True
print(a.issuperset(b))  # output: True