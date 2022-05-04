# # creating a tuple using ()
# a = (1,3,5,7,8)
# print(a[0])

# # we cannot change the values of tuple like we did in list
# # a[2] = 35 # it will show an error
# print(a)
# # tuple  is an immutable type data

# b = () # it is an empty tuple
# print(b) 

# # b1 = (1) # it is not the correct way to declare a tuple with single element
# b1 = (1,) # always use comma after an element to declare a tuple with single element 
# print(b1) 

# Swapping technique
a = 1
b = 8
a,b=b,a
print(a,b)


# methods of tuple
# a = (1,1,3,3,2,5,5)
# print(a.count(1)) # will count the number of 1
# print(a.index(2)) # will specify the index of number 2 which is 4
# print(a)
