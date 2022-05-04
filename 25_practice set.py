'''Create a class proogrammer for storing information of few programmers working at microsoft'''
# class Programmer:
#     company = 'Microsoft'
#     def __init__(self, name, address, product):
#         self.name = name
#         self.address = address
#         self.product = product

#     def getDetails(self):
#         print(f'The name of the employee is {self.name}. He lives in {self.address} and he is working on the product {self.product}')

# Shrey = Programmer('Shrey', 'Bhayli', 'Microsoft Games')
# Kamil = Programmer('Kamil', 'Panchvati', 'Skype')
# rishank = Programmer('rishank', 'undera', 'Github')

# Shrey.getDetails()
# Kamil.getDetails()
# rishank.getDetails()



'''Write a class calculator capable of finding square, squareroot and cube of a number.'''
# method1
# class Calculator:
#     def __init__(self,num):
#         self.num = num

#     def square(self):
#         return self.num*self.num
    
#     def squareroot(self):
#         return self.num **0.5
    
#     def cube(self):
#         return self.num * self.num * self.num

# object = Calculator(4)
# a = object.square()
# b = object.squareroot()
# c = object.cube()
# print(a)
# print(b)
# print(c)



    
# method2
# class Calculator:
#     def __init__(self,num):
#         self.num = num

#     @staticmethod                    '''Add static method to greet the user with hello'''
#     def greet():
#         print('Hello there welcome to the best  calculator in the world')

#     def square(self):
#         print(self.num*self.num)
    
#     def squareroot(self):
#         print(self.num **0.5)
    
#     def cube(self):
#         print(self.num * self.num * self.num)


# object = Calculator(4)
# object.greet()
# object.square()
# object.squareroot()
# object.cube()



'''Create a class with class attribute a. Create an object from it and set a directly using object a=0.
does this change the class attribute?'''


# class Numbers:
#     a = 'Shrey'   #--> this is class attribute

# object = Numbers()
# object.a = 'Kamil'   #--> this is an instance attribute

# print(Numbers.a)
# print(object.a)

# both are different attributes so both will be printed



'''Write a class Train which has methods to book a ticket, get status(no of seats)and get fare information
of trains running under Indian Railways'''

class Train:
    def __init__(self, train, seats, fare):
        self.train = train
        self.seats = seats
        self.fare = fare
    
    def getStatus(self):
        print(f'The name of the train is {self.train}')
        print(f'The number of seats available is {self.seats}')

    def getfare(self):
        print(f'The price of the ticket is {self.fare}')

    def bookTickets(self):
        if (self.seats>0):
            print(f'Your ticket has been booked! Your seat number is {self.seats}')
            self.seats = self.seats - 1
        else:
            print(f'Sorry no seats available! kindly try in tatkal')
               
intercity = Train('Intercity', 0, 90)

intercity.bookTickets()
# intercity.cancelTicket()
intercity.getStatus()
intercity.getfare()




'''Can you change the self parameter inside a class to  something else(say 'Shrey').
Try changing self to slf or Shrey and see the effects'''

# class Sample:
#     def __init__(Shrey, name):
#         Shrey.name = name

# object = Sample('Shrey')
# print(object.name)

# Yes we can change the parameter self to Shrey or slf and the answer will be the same 