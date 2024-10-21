def count_digits(number):
    if type(number) is int:
        result = len(str(abs(number)))
        print(result)
    else:
        print("Wrong data type")

count_digits(123)
count_digits(-23)
count_digits(3)


def gradeCalculator(grade):
    print(grade)
    if grade < 100 and grade > 90:
        print("A")
    elif grade < 90 and grade > 80:
        print("B")
    elif grade < 80 and grade > 70:
        print("C")
    elif grade < 70 and grade > 60:
        print("D")
    elif grade < 60 and grade > 50:
        print("E")
    elif grade < 50 and grade > 0:
        print("F")
    elif grade < 0:
        print("Wrong number")
    else:
        print("Please, input number from 1 to 100")
        

gradeCalculator(int(input("Please, add number from 1 to 100: ")))



def sortNumbers(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        if num2 < num3:
            result = str(num1) + " " + str(num2) + " " + str(num3)
        if num2 > num3:
            result = str(num1) + " " + str(num3) + " " + str(num2)
    elif num1 > num2 and num1 < num3:
        result = str(num2) + " " + str(num1) + " " +  str(num3)
    elif num1 > num2 and num1 < num3:
        result = str(num2) + " " + str(num1) + " " +  str(num3)
    elif num1 > num3 and num1 > num2:
        if num2 < num3:
            result = str(num2) + " " + str(num3) + " " + str(num1)
        if num2 > num3:
            result = str(num3) + " " + str(num2) + " " + str(num1)


    print(result)
	
sortNumbers(4,10,6)
sortNumbers(4,6,10)
sortNumbers(10,6,4)



def calculator(number1, number2, operator):
    if str(operator) == "/":   
        print(int(number1) / int(number2))
    elif str(operator) == "*":
        print(int(number1) * int(number2))
    elif str(operator) == "+":
        print(int(number1) + int(number2))
    elif str(operator) == "-":
        print(int(number1) - int(number2))
    elif str(operator) != "/" or "+" or "-" or "*":
        print("Wrong operator")
    else:
        print("Wrong")


calculator(1,2,"/")