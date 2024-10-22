# HW 5
# 5.3

# numbers = [10, 20]
# items = ["Chair", "Table"]

# for x in numbers:
#   for y in items:
#     print(x, y)


# x = 0
# while (x < 100):
#   x+=2
# print(x)


# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)


# for num in range(2,-5,-1):
#     print(num, end="")



# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     print(x)


# i = 1
# while i < 6:
#    print(i)
#    i += 1


# for num in range(10, 14):
#     for i in range(2, num):
#         if num%i == 1:
#           print(num)
#           break



# 5.2

# def count_vowels(word):
#     s = 0
#     gls = ["a", "e", "i", "o", "u"]
#     for i in word:
#         if i in list(gls):
#             s += 1
#             print(i, s)
#     return

# count_vowels("softserve")


def count_vowels(word):
    x = 0
    gls = ["a", "e", "i", "o", "u"]
    for i in word:
        if i in gls:
            x += 1
    return x
        
print(count_vowels("Celebration"))





# def count_vowels(word):

#     for i in word:
#         if i in list(gls):
#             m += 1
#     print(m)
        


def mean(number):
    a = 0
    b = 0
    for i in number:
        print(i)
        a = i
        b += 1
        c = i + a
        print(c)
    return a, b

print(mean("512"))

# (5+1+2)/3(number of digits) = 8/3=3).