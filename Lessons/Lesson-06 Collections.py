### Lesson 6 - Collection
# List
# Tuple 
# Set
# Dictionary

# Створення  List
print()
print("Start")
print("List")

l = list()
print(type(l), l)

l = list("12345")
print(type(l), l)

l = []
print(type(l), l)

l = [0,1,2,"test", [1,2,3]]
print(type(l), l)

# Звіна елементів в list

l[1] = "123"
l[-1][0] = "123"
print(type(l), l)

# методи в List
print([method for method in dir(list) if not method.startswith("_")])

# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

l.append("append")
print(l)

l.extend("10")
l.extend([20])
l.extend([[20]])
print(l)

l.insert(-1, "denis")
print(l)

print(l.count("123"))

l.remove(0)
print(l)
l.remove("denis")
print(l)

element = l.pop()
print(element, l)


i = l.index(20)
print(i)

l.append(20)
i = l.index(20, i+1)
print(i)
print(l)


l.reverse()
print(l)
rl = list(reversed(l))
print(l)
print(rl)
print(list(rl[::-1]))

b = [1,2,6,3,2,10]
b.sort()
print(b)


l.clear()
print(l)

l = [1,2,3]
k = []

print(l,k)

k = l.copy()
print(type(k))
print(k)


print()
print("Build list")
l = [i+1 for i in range(20)]
print(l)

b = []
for a in range(3):
    a = a + 1
    b.append(a)
print(b)

# Створення  Tuple
print("Tuple")


t = tuple((1,2,3))
print(type(t),t)

l = list(t)
print(type(l),l)

# методи в Tuple
print([method for method in dir(tuple) if not method.startswith("_")])


# Створення  Set
print()
print("Set")
print([method for method in dir(set) if not method.startswith("_")])

s = set()
s = {1,2,3}
print(type(s),s)

s = set("denis")
print(type(s),"denis = >", s)

s.add("D")
print(s)

r = s.remove("d" and "e")
print(r,s)

s.update([1,2,3])
print(s)


A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A,B)

print ( A | B)
print(A.union(B)) # унікальні  
print(A.intersection(B)) #  gthtnsy
print(A.difference(B)) # різні
print(B.difference(A))
print(B ^ A) # сіметрічні  


C = {1,2,3,4,1,2,3,4}
print(C)


# Створення  Dict
print()
print("Dict")
print([method for method in dir(dict) if not method.startswith("_")])


d = dict()
print(type(d),d)

d = dict([("key.1","1")])
print(d)

d["key.1"] = 1
print(d)
d["key.2"] = 2
print(d)

print("get")
print(d.get("key.2")) # достати значення по ключу
print(d.keys()) # ключи
print(d.values()) # значення
print(d.items()) # 


for i in d:
    print(i)

#  як достати ключи
print("як достати ключи")
for key, values in d.items():
    print(key,values)