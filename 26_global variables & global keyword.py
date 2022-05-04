
# a = 10 # Global variable
# def function(n):
#     a = 5 # Local variable
#     print(n,'wassup')
#     # print(a)

# function('kya bhai')
# print(a)

'''Global variable cannot be changed''' 
# a = 10 # Global variable
# def function(n):
#     a = a + 20 # this will throw an error if we try to change the global variable
#     print(n,'wassup')
#     print(a)

# function('kya bhai')
# print(a)


'''But if we use global command we can change global variable in function'''
# a = 10 # Global variable
# def function(n):
#     global a
#     a = a + 20
#     print(n,'wassup')
#     print(a)

# function('kya bhai')


'''We can change the local variable'''
# def function(n):
#     a = 5 # Local variable
#     a = a + 25
#     print(n,'wassup')
#     print(a)

# function('kya bhai')



def Shrey():
    x = 10
    def Kamil():
        global x
        x = 40
    print('Before calling Kamil', x) # this will print 10 as value of x
    Kamil()
    print('After calling Kamil',x) # this will also print 10 as value of x because global will only check for the values outside the functions if not then x will remain as it is.

Shrey()
print(x) # Here the value of x will change to 40 because we printed the value outside where global value is changed to 40