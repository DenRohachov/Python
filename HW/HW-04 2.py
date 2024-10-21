def k_to_k(num1, num2):
    k = num2
    n = num1
    if k**k == n:
        print(True)
    else:
        print(False)
	
# k_to_k(4, 2) True
# k_to_k(8, 2) False
# k_to_k(387420489, 9)True

k_to_k(4, 2)
k_to_k(8, 2)
k_to_k(387420489, 9)


def string_int(str1):
    x = str1.isdigit()
    if x == True: 
        print(str1)
        print(x)
    else:
        print("Not a number")
        print(x)

string_int("1000")



print("Task 1")

def divisible_by_five(number):
    if number % 5 == 0:
        print(True)
    else:
        print(False)

divisible_by_five(25)
divisible_by_five(4)



print("Task 2")

def makes10(num1, num2):
    if num1 == 10 or num2 == 10:
        print(True)
    elif num1 + num2 == 10:
        print(True)
    else:
        print(False)

makes10(10,5)
makes10(5,5)
makes10(1,5)

print("Task 3")

def return_negative(number):
    if int(number) <= -1:
        print(number)
    elif int(number) >=1:
        print(number - number *2)
    else:
        print(number)

return_negative(1)
return_negative(-11)



print("Task 4")

def less_than_100(num1, num2):

    if num1 + num2 < 100:
        print(True)
    else:
        print(False)


less_than_100(1,20)
less_than_100(20,91)
