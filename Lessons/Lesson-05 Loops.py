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