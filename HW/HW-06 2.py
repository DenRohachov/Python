def filter_list(lst):
    print(lst)
    l_new = []
    for i in lst:
        if type(i) == int:
            l_new.append(i)
    print(l_new) 
    return(l_new) 

filter_list([1, 2, 3, "a", 4, "b"])


def probability(lst, num):
    print()
    a = 0
    b = 0
    l = lst
    print(lst)
    for i in l:
        if int(i) >= int(num):
            a += 1
        b += 1
        print(i)
    print(a)
    print(b)
    print(round((100*a/b),1))
    return(100*a/b)

probability([5, 1, 8, 9], 6)
probability([7, 4, 17, 14, 12, 3], 16)
probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6)

# 50 = 100 * 2 / 4
# 16.7
# 70.0 = 100 * 5 / 10



def find_odd(lst):
    print()
    s = set(lst)
    s = list(s)
    print(s)
    l = []
    for i in s:
            if int(lst.count(i)) % 2 != 0:
                    print(i, "count => ", int(lst.count(i)))
                    l.append(i)
    print(l)            
    return(l)

find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
print(find_odd([20, 1, 1, 2, 1, 2, 3, 3, 5, 5, 4, 20, 4, 5]))



print()
def nth_smallest(lst, n):
    l = []
    x = 0
    for i in lst:
        l.append(i)
        print((i))
    l.sort()
    print(l)
    for i in l:
         if i / n >= n:
            x = i
            break
         
    print()
    print(x)
    print()
    
    return(lst, n)



nth_smallest([5, 1, 8, 9], 2)
nth_smallest([1, 3, 5, 7], 3)
nth_smallest([1, 3, 5, 7], 5)
nth_smallest([1, 3, 5, 7], 4)

# print(nth_smallest([5, 1, 8, 9], 2)) 5
# print(nth_smallest([1, 3, 5, 7], 3)) 5
# print(nth_smallest([1, 3, 5, 7], 5)) None
# print(nth_smallest([1, 3, 5, 7], 4)) 7



print()
print()
print("5 step")
def add_indexes(lst):
    x = []
    c = 0
    for i in lst:
     x.append(i+c)
     c += 1
    print(x)
    return(x)


add_indexes([0, 0, 0, 0, 0]) 
add_indexes([1, 2, 3, 4, 5]) 
add_indexes([5, 4, 3, 2, 1]) 
add_indexes([0, -1, -2, -3, -4]) 


# add_indexes([0, 0, 0, 0, 0]) [0, 1, 2, 3, 4]
# add_indexes([1, 2, 3, 4, 5]) [1, 3, 5, 7, 9]
# add_indexes([5, 4, 3, 2, 1]) [5, 5, 5, 5, 5]
# add_indexes([0, -1, -2, -3, -4]) [0, 0, 0, 0, 0]