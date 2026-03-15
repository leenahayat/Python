#sets are unordered in python but dictionary is ordered in python


manager1 = {1: 'Shubh', 2: 'Ali', 3: 'Raza', 4: 'Zani'}
manager2 = {5: 'Hina', 6: 'Rana'}

manager1.update(manager2)
print(manager1)

manager1.pop(2)
print(manager1)

manager1.popitem()
print(manager1)

manager1.clear()
print(manager1)

empt = {}
print(empt)