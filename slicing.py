l = [5,6,7,8,9]

# 6
print(l[1])
# 9
print(l[len(l) - 1])
# 9
print(l[-1])

print("slicing")
# [6,7]
print(l[1:3])
# [5,6,7]
# echivalent cu l[0:3]
print(l[:3])
# [7,8,9]
# echivalent cu l[2:len(l)-1]
print(l[2:])
# [5,6,7,8,9]
print(l[:])

print("slicing cu pasi")
#[6,8]
print(l[1:4:2])
# []
print(l[4:1])
# [9,8,7]
print(l[4:1:-1])
# [6, 7, 8]
print(l[1:-1])