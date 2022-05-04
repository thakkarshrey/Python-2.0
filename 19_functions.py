# marks1 = [23,45,67,87]
# percentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400)*100


# marks2 = [98,76,54,99]
# percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100
# print(percentage1, percentage2)


'''if there are 10 list given then we will need to do the same thing again and again which will
make the code complicated and time consuming so we will create a function'''


# def func():
    # return 


# def percentage(marks):
#     return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

# marks1 = [23,45,67,87]
# percentage1 = percentage(marks1)


# marks2 = [98,76,54,99]
# percentage2 = percentage(marks2)
# print(percentage1, percentage2)

# a function can be reused in a programe by the programmer

'''write a program to greet a user with good day using functions'''
# method1 
# def greet(user):
#     """This function will greet the user"""   # this is known as doc string
#     print('Good day' , user)
# greet('Shrey')

# print(greet.__doc__) --> this will print the docstring 

# method2
# def greet(user):
#     a = ('Good day ' + user)
#     return a

# b = greet('Shrey')
# print(b)

# if you dont write return then b will show None because the function wont return anything.



'''write a program to add two numbers using function'''
#method1
# def sum(num1, num2):
#     return num1 + num2
# a = sum(3,6)
# print(a)


#method2
# def sum(num):
#     return num[0]  + num[1]
# num1 = [3,7]
# b = sum(num1)
# print(b)


'''default parameter value'''
# def greet(user):
#     print('Good day' , user)
# greet('Shrey') #  lets suppose if if dont specify the name 'shrey' and keep the bracket empty

# def greet(user):
#     print('Good day' , user)
# greet() # it will throw an error as no default name is set

# def greet(user = 'Stranger'): # if if write stranger here then output will say good day stranger when i keep the greet() empty
#     print('Good day' , user)
# greet() 



'''Lambda functions or anonymous functions'''
minus = lambda x,y:x-y
print(minus(10,5))


def minus(x,y):
    return x-y
print(minus(10,5))

# these both works the same

def func(a):
    return a[1]
a = [[1,30],[9,5],[7,28]]
a.sort(key=func)
print(a)

#OR

a = [[1,30],[9,5],[7,28]]
a.sort(key=lambda a:a[1])
print(a)

