### lesson 5 - LOOPS
 
a = int(input("a: "))
s = 0
while a > 0:
    s += a
    a = int(input("a: "))

print(f"{s=}")


###


start = 0
finish = 10
while start < finish:
    print(start)
    start += 1
else:
    print("end")


###

l = [1,2,3]
for i in l:
    print(i)

for i in range(len(l)):
    print(l[i])


###

# while True:
#    pass

### SLEEP

# import time
# for datetime import date, datetime, timedelta
#
# while True:
#    print(date.todat())
#    time.sleep(5)

l = [10, None, [1, 2, 6]]
for element in l:
    if type(element) in (list, tuple):
        for e in element:
            print("\t", e)
    else:
        print(element)

# 

s = set("qwert") # - набір унікальних елементів але послідовсніть різна
print(s)
for c in s:
    print(c)

# 

d = { "key1":"value1", 15:"value2"}
print(d)
for i in d:
    print(i, d[i])


a, b = (1, 5)
print(d.items())
print(a,b)
for key, value in d.items():
    print(key,value)


n = 5
l = [i for i in range(n)]
t = (i for i in range(n))
print(l)
print(list(t))
print(t)



print()
print("51 хв")

l = [1,2,3]
for i in l:
    print(i)

for i in range(3,9,2):
    print([i])


print()
print("break")
print("i\t i**2 \t i**i")
for i in range(5):
    print(i, end=" \t ")
    print(i**2, end=" \t ")
    print(i**i)


print()
print("continue")

for i in range (10):
    print(i, end="")
    if i% 2:
        print()
        continue
    print("=>", i**i)


print()
print("break")

for i in range (10):
    print(i, end="")
    if i == 3:
        print()
        break
    print("=>", i**i)


print()
print("else з continue")

l = [1,5,9, [1,8,9]]
s = 0
for i in l:
    if type(i) is not int:
        temp =i
        continue
    s += i
else:
    print(f"{s=}")
print("end")


print()
print("pass")
pass


print()
print("tasks")

for i in range(0,100,2):
    print(i)


i = 0
while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1

for i in range(1,100,2):
    print(i)


i = 1
while i < 100:
    i += 1
    if i % 2 ==0:
        continue
    print(i)

# git commit
# git commit
# git commit

i = 1
while i < 100:
    i += 1
    if i % 2 ==0:
        continue
    print(i)