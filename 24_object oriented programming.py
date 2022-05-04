# a = 12
# b = 24
# print(f'the sum of a and b is {a+b}')
#--> This method is called procedural oriented programming


'''example:1'''
# class Number:
#     def sum(self):
#         return self.a + self.b
# num = Number()
# num.a = 12
# num.b = 34
# s=num.sum()
# print(s)
#--> This method is called object oriented programming


'''example:2'''
# class RailwayForm:
#     formType = 'Railway'
#     def printData(self):
#         print(f'the name of the applicant is{self.name}')
#         print(f'the name of applicants train is {self.train}')

# shreysapplication = RailwayForm()
# shreysapplication.name = 'Shrey'
# shreysapplication.train = 'Rajdhani express'
# shreysapplication.printData()

# RailwayForm is the class. It can be compared to template of a railway form.
# Suppose i want to fill the railway form so shreysapplication will be the object.
# There will be variables in the form as shreysapplication.name and .train which will contain details of the object.


'''example:3'''
# lets suppose if we are making gta vice city
class Remote:
    pass
class Player:
    def moveRight(self):     # pass is written because we are not making a game. this is just an example.
        pass
    def moveLeft(self):  
        pass
    def moveTop(self):     
        pass
    def moveDown(self):     
        pass
remote1 = Remote()
player1 = Player()
if(remote1.isLeftPressed()):
    player1.moveLeft()

# if we would have written this in function then it would have been difficult to identify which function works for which command.
# it is easy to understand and close to the language we use in daily life.

'''CLASS ATTRIBUTES EXAMPLE'''
# Class attribute will be something which is common between the employees which can be the company.
# class Employee:
#     company = 'Google' # this is called an attribute 
# Shrey = Employee()
# Kamil = Employee()
# print(Shrey.company)

# Now if i want to change the company of class then....
# Employee.company = 'Youtube' # This is known as class attributes
# print(Kamil.company)




'''INSTANCE ATTRIBUTES'''
# the attributes which belong to that particular object. suppose phone number, name, address, salary of the employee.
# considering the same example as previous one

# class Employee:
#     company = 'Google'
#     salary = 5000 # class attribute

# Shrey = Employee()
# Kamil = Employee()
# Shrey.salary = 7000 # instance attribute
# Kamil.salary = 10000 # instance attribute
# print(Shrey.salary)
# print(Kamil.salary)

# lets suppose there is a class attribute called salary and at the same time there is instance attribute for salary
# what will be printed first instance attribute or class attribute?
# It will check for the instance attribute first. If it is present then it will display the data of that.
# If not then it will check for the class attribute.


'''SELF PARAMETER USED IN ATTRIBUTE'''
# class Employee:
#     company = 'Google'
#     def getSalary(self):
#         print('Your salary is 100k')

# Shrey = Employee()
# Shrey.getSalary()
# # OR
# Employee.getSalary(Shrey)

# If we remove self it says Employee.getSalary() takes 0 positional arguments but 1 was given
# Shrey.getSalary() is also written as Employee.getSalary(Shrey)
# The Shrey in Employee.getSalary(Shrey) goes to the self of getSalary(self) function and calls it
# But as self is removed it throws an error
# So the error says 1 argument was given which was Shrey but self was not given



# class Employee:
#     company = 'Google'
#     def getSalary(self):
#         print(f'Your salary is{self.salary}') # It will print the salary attribute of the object we are running this function on.
# # The object will be passed on to the function and we will be able to print all the instance and class attributes of the object
# Shrey = Employee()
# Shrey.salary = '100k'
# Shrey.getSalary()



'''STATIC METHOD'''
# class Employee:
#     company = 'Google'
#     def getSalary(self, signature):
#         print(f'Your salary is {self.salary}\n{signature}')

#     @staticmethod
#     def greet():
#         print('Hello sir hope you have a good day') 

# Shrey = Employee()
# Shrey.salary = '100k'
# Shrey.getSalary('Thanks!:D')
# Shrey.greet()

# What is the need of self in function when you ust want to greet someone like hello sir have a good day
# What if we can use Employee.greet() instead of Employee.greet(Shrey) 
# We can do this by using Static method 
# Just write @staticmethod before greet function
# but if you write @staticmethod and self both at same time then it will throw an error 
# we can also pass signature function along with self





'''CONSTRUCTOR'''
# example1
class Employee:
    def __init__(self, name, salary, work):
        self.name = name
        self.salary = salary
        self.work = work
        print('Employee is created')
        print(f'The name of employee is {self.name}')
        print(f'The salary of employee is {self.salary}')
        print(f'The work of employee is {self.work}')

Shrey = Employee('Shrey', '100k', 'Youtuber')
Shrey = Employee() #--> This throws an error


# This init function will print the data even if we did not run it. 
# Even if we run it by writing Shrey.__init__() then it will print the data 2 times. one is by default and the other which we ran it
# init can be used to add more functions at the same time as shown above.
