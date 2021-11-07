from copy import copy, deepcopy

l1 = [1,2,3]
l2 = l1
l2[0] = 100
print(l1)

print("shallow copy")
l1 = [1,2,3]
l2 = l1[:]
l2[0] = 100
print(l1)

# echivalent
l1 = [1,2,3]
l2 = l1.copy()
l2[0] = 100
print(l1)

# echivalent
l1 = [1,2,3]
l2 = copy(l1)
l2[0] = 100
print(l1)

print("deep copy")
l1 = [1,2,3]
l2 = deepcopy(l1)
l2[0] = 100
print(l1)

print("shallow copy cu lista de liste")
l1 = [[1],[2,3],[4]]
l2 = l1[:]
l2[0][0] = 100
print(l1)
print(id(l1), id(l2))
print(id(l1[0]), id(l2[0]))

print("deep copy cu lista de liste")
l1 = [[1],[2,3],[4]]
l2 = deepcopy(l1)
l2[0][0] = 100
print(l1)
print(id(l1), id(l2))
print(id(l1[0]), id(l2[0]))
