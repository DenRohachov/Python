### Lesson 7 - Definition (оголошення)

def print_text(a):
    ''' doc string documentation '''
    print("my_rext >>", a, "<< and my_text")

print_text("Anna")
print_text(579)
print(print_text)

print(print_text.__doc__)


### return - службове слово, яке є тільки в функціях всередені
### ждя повернення значення

def max_number(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    return f"{a} == {b}"
    
print(max_number(1,2))
c = max_number(3,5)
print(c)


# Function - required - обовьязкові
# name age = обовьязкові аргументи
print()
print("Function - required")
print()

def print_info(name, age):
    print(f"my name is {name}, my age is {age}")

print_info("Denis", 34)

# Function - default - не обовязкові
# age=34 = не обовязковий
print()
print("Function - default")
print()

def print_info(name, age=34):
    print(f"my name is {name}, my age is {age}")

print_info("Denis")
print_info("Denis", 44)

# Function - keyword
print()
print("Function - keyword")
print()
print_info(age=45 , name="Denis")


# Function - keyword
print()
print("Function - keyword")
print()

# def print_in():
#     a = input("a:")
#     b = input("b:")
#     c = input("c:")
#     print(a,b,c)
#     return(a,b,c)

# print_in()



# Function - var
print()
print("Function - var (args and wargs)")
print()

def f(*args, **qwargs):
    print(f"{args} {qwargs}")

f(1,2,3,4,5,6,7, l=1,b="test")


def numbers(a,b,c):
    x = a + b + c
    return(x)

print(numbers(1,2,3))


def f(*args):
    return sum(args) / len(args)
print(f(10,20,30,25))


### zip * or **

def f(*number, **values):
    print(f"{number} {values}")

l = {"a":1, "b":2}
f(*l)
f(**l)

### global **

a = 1

def f():
    global a
    print(a)
    a = "new"
    print(a)
f()
print(a)


### non local

g = "global - 1"
l = "global - 1"

def out():
    l = "local - 2"
    def inner():
        ll = "local_inner"
        nonlocal l
        print("inner:", g,l,ll)
    inner()
    print("out:", g,l)
out()
print(g, l)


### Рекрусівна функція - функція котра
### викликає сама себе

print()
def fuc(n):
    f = 1
    for i in range(n+1):
        f *= i
    return f
print(fuc(5))
print(fuc(10))

def r_fuc(n):
    if n >= 0:
        print(n)
        return n*r_fuc(n-1)
    return("STOP")
print(r_fuc(10))



### Lambda - Однастрічкова
### Lambda - єсную поки є функція 

print()
print("Lambda")

s = lambda a,b: a*b
print(s(5,25))

def lam(a,b):
    print(a*b)
lam(5,25)


l = [1,3,2,4,"0"]
l.sort(key= lambda e: str(e))
print(l)