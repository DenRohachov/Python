### HW 07 Function
# 07.2 Quiz for Topic 7
print("# 07.2 Quiz for Topic 7")


def output_param(x,y,z):
    print(x,y,z)

my_tuple = (1,2,3)
output_param(*my_tuple)


def my_func(first_param = 3, second_param = 1):
    first_param = first_param + second_param
    second_param += 1
    print(first_param, second_param)
my_func(second_param=1, first_param=3)


my_func = lambda: x if x>5 else x**2*my_func(10)
my_func = lambda x: x if x>5 else x**2*my_func(10)
print(my_func)

def my(input_message, num = 1):
    print(input_message * num)
my("Hello")
my("Hi", 5)

my_func = lambda x: x if x >5 else x ** 2 * my_func(10)

print(my_func(2))

list = [lambda x: x ** 2,
        lambda x: x ** 3,
        lambda x: x ** 4]

for item in list:
    print(item(5))


counter = 5
def func():
    counter = 8
    print(counter)

func()
print(counter)


# 07.1 Practical tasks / [GitHub Topic 7]
print()
print("07.1 Practical tasks / [GitHub Topic 7]")


def numbers(a,b):
    if a > b:
        print(a)
        return(a)
    else:
        print(b)
        return(b)
numbers(10,40)