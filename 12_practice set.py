'''write a program to store seven fruits in a list entered by the user'''
# this question is done by me myself
# l1 = []
# fruit1 = input("What is your  favourite fruit?\n")
# l1.insert(0, fruit1)
# fruit2 = input("What is your second most favourite fruit?\n")
# l1.insert(1, fruit2)
# print(l1)

# question  done by harry
# f1 = input("Enter the name of fruit1: ")
# f2 = input("Enter the name of fruit2: ")
# f3 = input("Enter the name of fruit3: ")
# f4 = input("Enter the name of fruit4: ")
# f5 = input("Enter the name of fruit5: ")
# f6 = input("Enter the name of fruit6: ")
# f7 = input("Enter the name of fruit7: ")
# l1 = [f1, f2, f3, f4, f5, f6, f7]
# print(l1)

'''write a program to accept the marks of 6 students and display them in a sorted manner'''
# this question is done by me myself
# s1 = int(input("Please enter your marks out of 100: ")) 
# s2 = int(input("Please enter your marks out of 100: "))
# s3 = int(input("Please enter your marks out of 100: "))
# s4 = int(input("Please enter your marks out of 100: "))
# s5 = int(input("Please enter your marks out of 100: "))
# s6 = int(input("Please enter your marks out of 100: "))
# # harry kept an int before all of variables because the out will be in the form of string and we want an integer.
# l1 = [s1, s2, s3, s4, s5, s6]
# l1.sort()
# print(l1)

'''check that a tuple cannot be changed'''
# t=(2,5,6,7,9)
# t[2]=35 # it will show an error
# print(t)

'''write a program to count the number of zeros in a tuple given below'''
# f= (7,0,8,0,0,9)
# print(f.count(0))


'''write a program to sum a list with 4 numbers'''
# a=[3,5,2,6,7]
# print(a[0]+a[1]+a[2]+a[3]+a[4])
# print(sum(a))






user = {
    'Name':'Shrey',
    'email':'thakkarshrey10.st@gmail.com',
    'age':'23'
}

for key,value in user.items():
    print(key,value)

# Both works fine
# first one just shows key and value
# second one shows key value in form of tuple 

for things in user.items():
    print(things)




