# Bool 
t = True
print(type(t),t)
f = False
print(type(f),f)

# List (mutable)
list = [55,52,55]
print(type(list),list)

# tuple 
tuple = (55,52,55)
print(type(tuple),tuple)

# Set (mutable)
set = {55,52,55}
print(type(set),set)

# Dict (mutable)
dict = {"name":"denis","age":10}
print(type(dict),dict)

# перевірка типу
с = 123
print("перевірка типу")
print(type(с) is int)

# переноси кругли дужки, або /
с = ([1 +
     2 +
     3])
print(с)


# множинне присвоювання переменних
a,b,c = 1,2,3
print(a,b,c)

# множинне присвоювання переменних
a = 1
b = 2
c = b,a
print(c)

# равенста  Bool
print(True == 1)
print(False == 0)



# дефолтна заглушка
value_1 = None
print(value_1)


# будь яки типи в колекціях list
l = [1, "test", 5.6, (1.2), None]
print(type(l),l)


# string символи
text = "Hello, what\"s \n this? \r 123 \t\t  this? \\this? "
print(text)


#  Темплейт старий
template = "My name is %s"
print(template)
print(template % ("Denis"))

#  Темплейт новий з змінними
template = "My name is {name} and age is {age}"
print(template.format(name = "Denis", age = 44))

#  Темплейт новий з змінними самі нові, самі швидки
name = "Denis"
age = 44
print(f"My name is {name} and age is {int(age/2)}")


#  Індексація та отримання данних з текстового типу змінной
s = "Denis need to be happy"
print(s[0])

#  Індексація та отримання данних з по
s = "Denis need to be happy"
print(s[0:10])

#  Індексація та отримання данних кожен другий
#  приклад салйсу - перше друге третье 
s = "Denis need to be happy"
print(s[::-1])


#  Перетворення string
s = "Denis need to be happy"
print(s.count(s))
print(s.lower())



s1 = "hot"
s2 = "dog"
print(s1 + s2)


str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub, 4))

str = "my name is James bond"
print (str.capitalize())

str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())


print("John" > "Jhon")
print("Emma" < "Emm")

first_name = "television"
hobby = "homer"
tmp = first_name
first_name = hobby
hobby = tmp
print(f"T{first_name[1:3]} likes to watch {hobby[4:]}")


str1 = "Welcome"
print(str1*2)


str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())

str = "my name is James bond"
print (str.capitalize())


print("John" > "Jhon")
print("Emma" < "Emm")

str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub, 4))


first_name = "television"
hobby = "homer"
tmp = first_name
first_name = hobby
hobby = tmp
print(f"T{first_name[1:3]} likes to watch {hobby[4:]}")


str1 = "Ault\"Kelly"
print(str1)


print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

v1 = 1
v2 = 2
v3 = "3"
# print(v1 + v2 + v3)

value = 36 / 4 * (3 + 2) * 4 + 2
print(value)

print(type({}) is set)

value_one = 5 ** 2
value_two = 5 ** 3

print(value_one)
print(value_two)


print("hello")

