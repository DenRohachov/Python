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


# def count_vowels(word):
#     x = 0
#     gls = ["a", "e", "i", "o", "u"]
#     for i in word:
#         if i in gls:
#             x += 1
#     return x
        
# print(count_vowels("Celebration"))





# def count_vowels(word):

#     for i in word:
#         if i in list(gls):
#             m += 1
#     print(m)
        


# def mean(number):
#     b = 0
#     for i in str(number):
#         a = i
#         b += 1
#         c = a
#     print()  
#     return a, b

# print(mean(42))


# def integer_boolean(binary_number):
#       for i in str(binary_number):
#         print(i)
#         if int(i) % 2 == 0:
#             num = False
#             print(num)
#         else:
#             print(num)
#             num = True
        
#       return num

# integer_boolean("123456")


# def is_isogram(word):
#     low_word = word.lower
#     for i in low_word:
#         if i in low_word:
#             print(i)
#             return True
#         else:
#             return False

# is_isogram("Denis")




# def mean(number):
#     a = str(number)
#     b = 0
#     c = []
#     for i in str(number):
#         b += 1
#     print(a,b,c)
#     return a, b, c

# mean(512)
