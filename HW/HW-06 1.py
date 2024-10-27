# HW collections

sum = 0
counter = 0
numbers = [22, 55, 111, 555]

print(numbers[counter])

while numbers[counter] < 100:
  sum = sum + numbers[counter]
  counter = counter + 1
print(sum)



my_list = ["Hello", "Python","Denis"]
print("-".join(my_list))



sum = 0
counter = 0
numbers = [1, 2, 3, 4]
print(len(numbers))
while counter < len(numbers):
  sum = sum + numbers[counter]
  counter = counter + 1
print(sum)


aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])    
print(aList[1][3])


# color_set = {"black", "red", "blue"}
# print(color_set[1])


new_dict = dict()
print(type(new_dict))

new_dict = {}
print(type(new_dict))

dict_1 = {"age":11, "name":"Ivan"}
dict_2 = {"name":"Ivan", "age":11}
print(dict_1 == dict_2)


word = ""
counter = 0
letters = ["c", "a", "r"]
while counter < len(letters):
  word = word + letters[counter]
  counter = counter + 1
print(word)