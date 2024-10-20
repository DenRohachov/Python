# Lesson 4


a = 1
b = 2

print(a==b)
print(a!=b)
print(a>b)
print(b<a)


# порівняння контейнерів
# ліст
# перевірка по велью, по цінності
# порівнює по першобу обєєкту в лісті

a = [1,2,3]
b = [1,2,3]
print("\n")
print("ліст - перевірка по велью, по цінності")
print(a==b)
print(a!=b)
print(a>b)
print(b<a)


# оператори логіческі =  bool ева аріфметика

# and також множення
# or також додавання
print("\n")
print("and також множення, or також додавання")
print(True and True or True and False)
print(True and (True or True and False))
print(10 and (20 or "True" and []))
# and повертає перший неістенний
print(10 and [] and 0 and "g")
# or повертає останній неістенний
print([] or 10 or 0 or 1)
is_false = [False, None, 0, "", [],(),{}]
print(is_false)
if len([]) > 0: pass

# and or повертають обєекти


# Оператори пренадлежності

a = [1,2,3]
b = [1,2,3]
c = a
print(f"{a==b = }")

# Оператори пренадлежності

print("\n")
print("Оператори пренадлежності")

a1 = 1
b1 = 2
c1 = a1
print(f"{a1==b1 = }")
print(f"{a1 is b1 = }")
print(f"{a1 is c1 = }")
print(f"{a1==b1 = }")
print(f"{a1!=b1 = }")


if a1 != b1:
    print("OK")


    # Оператори пренадлежності

print("\n")
print("Оператори пренадлежності - обєкт ліст")

a1 = [1,2,3]
b1 = [1,2,4]
c1 = a1
print(f"{a1==b1 = }")
print(f"{a1 is b1 = }")
print(f"{a1 is c1 = }")
print(f"{a1==b1 = }")
print(f"{a1!=b1 = }")


if a1 != b1: print("OK")
if c1 is a1: print("OK ID")


# оператор принадлежності in  not in
# значення справа повинно бути ітерабельним (змінною)
print("\n")
print("оператор принадлежності in & not in")
a = [1,2,3,"4",[7,9]]
print(f"{1 in a = }")
print(f"{"4" in a = }")
print(f"{5 in a = }")
print(f"{[7] in a = }")
print(f"{[7,9] in a = }")


# оператор принадлежності  if
print("\n")
print("оператор принадлежності  if")

# d = int(input("Your age:"))
# if d < 20:
#     print("a < 20")
# if d  > 20:
#    print("a > 20")
# if 20 < d < 80:
#    print("<20 >80")


# age = int(input("Tell me your age: "))
# if age > 100:
#    print("більш 100")
#else:
#   if age == 60:
#        print("тобі 60")
#    else:
#        print("меньш 50")



# тернарний оператор 
weather = "raining"
print("Дощь" if weather == "raining" else "сонечко")
# повний код
result = None
if weather == "rain":
    result = "rain"
else:
    result = "no raint"
print(result)



# конструкція match case - аналог IF

print("конструкція match case - аналог IF")

status = int(400)
match status:
    case 400:
        print("400")
    case _:
        print("Error")

''' 
# конструкція match case - аналог IF
print("конструкція match case складніше")
values = str(input("enter values: ")).split()
match values:
    case "load", link: 
        print(f"load ->", link)
    case "save", link, *filenames: 
        print(f"save ->", link)
        for filename in filenames:
            print(f"\t({link}, {filename})")
    case _:
        print(f"default ({values})")

# конструкція match case -якщо IF
print("конструкція match case -якщо IF")

values = str(input("enter values: ")).split()

if len(values) == 2 and values[0] == "load":
   print(" load -> ", values[1])
elif len(values) == 3 and values[0] == "save":
    print(f" save ({values[1]}, {values[2]})")
else:
        print(f"default ({values})")

'''

# завдання в рамках уроку

a = int(input("a ?"))
b = int(input("b ?"))

if a < b:
    print(f"{a} < {b}")
elif b < a:
    print(f"{b} < {a}")
elif a == b:
    print(f"{a} = {b}")
else:
    print("Error", a, b)


c = 15
if c % 2 == 0:
    print(f"{c} парноє")
else:
    print(f"{c} не парноє")


# не використовуємо != а беремо not
not a == b