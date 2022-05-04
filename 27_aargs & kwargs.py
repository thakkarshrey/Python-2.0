'aargs and kwargs'

def function(a,b,c,d):
    print(a,b,c,d)

function('Shrey','Kamil','Kishan','Sagar')


'''If i want to add a name 'Rishank' here then i will have to add e in function and print value.
This cannot be done individually if there are a lot of names we are dealing with'''

'''For this reason we use aargs. We can directly add names to the list without defining variables'''



# def funcargs(*args):
#     print(type(args))
#     print(args)

# a = ['Shrey','Kamil','Sagar','Rishank','Utsav']
# funcargs(*a)

# '*' will mean that it will print the values of a in form of tuple



# def funcargs(*args):
#     for items in args:
#         print(items)
# a = ['Shrey','Kamil','Sagar','Rishank','Utsav','Pranav']
# funcargs(*a)



# '''We can also add normal with this'''
# def funcargs(normal,*args):
#     print(normal)
#     for items in args:
#         print(items)
# a = ['Shrey','Kamil','Sagar','Rishank','Utsav','Pranav']
# normal = 'The names of students are as follows:'
# funcargs(normal,*a) # Always use normal argument first then *aargs argument and then **kwaargs.It is a convention




def funcargs(normal,*args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    print('\nLet me introduce you to some of my friends')
    for key,value in kwargs.items():
        print(f'{key} is {value}')
a = ['Shrey','Kamil','Sagar','Rishank','Utsav','Pranav']
b = {'Shrey':'Fitness Instructor','Kamil':'NGO wala banda','Sagar':'The NAVY man','Pranav':'My brother'}
normal = 'The names of students are as follows:'
funcargs(normal,*a,**b)

# This way you can add data in a and b variable using *args and **kwargs without making any changes in function

