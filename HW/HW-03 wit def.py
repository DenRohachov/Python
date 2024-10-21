# HW 3
print("HW03")

def tri_area(base, height):
    result = 0.5 * base * height
    print(round(result,2)) 

base = 2
height = 3



def addition(number):
    result = number + 1
    print(result)

addition(1)


def convert(minutes):
    result = minutes * 60
    print(result)

convert(1)


def remainder(num1, num2):
    result = num1 % num2 
    print(result)

remainder(5,2)
remainder(25,5)
remainder(101,7)

# remainder(5, 2) 1
# remainder(25, 5) 0 
# remainder(101, 7) 3



def vol_shell(r1, r2):
    PI = 3.14
    result = round(4/3 * PI* (r1**3 - r2**3),2)
    print(result)

vol_shell(3, 2)
vol_shell(0, 0) 
vol_shell(100, 99) 


# vol_shell(3, 2) 79.55
# vol_shell(0, 0) 0.0
# vol_shell(100, 99) 124348.19