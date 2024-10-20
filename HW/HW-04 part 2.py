x = 5
if x > 0:
    x += 1
    if x < 10:
     x += 1
else:
    x -= 1
print(x)




num1 = 10
num2 = 20
print(num1 if num1 < num2 else num2)

x = 5
if x < 10:
    x += 1
    if x < 5:
       x += 2
x -= 1
print(x)


num = 7
print("Even" if num % 2 == 0 else "Odd")



x = 10
y = 5

if x > y:
   result = x + y
else:
   result = x - y
print(result)


x = 42

if x > 40 and x < 50:
    if x % 2 == 0:
       print("A")
    elif x % 3 == 0:
       print("B")
else:
   print("C")


x = 20
y = 10

if x >= y and x != 10 and (y % 2 ==0 or x % 4 == 0):
      print("A")
else:
   print("B")



x = 10


match x:
        case int(value):
            if value < 0:
                print("Negative")
            else:
                print("Non")
        case str(value):
            print("String")
        case _:
            print("Other")



x = 10
if x > 5:
    if x > 8:
        print("A")
    else:
        print("B")
else:
    print("C")