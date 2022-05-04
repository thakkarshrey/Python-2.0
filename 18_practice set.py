'''write a prgram to print a multiplication table using for loop of a given number'''
# done by me
# for a in range(1,11):
    # print(int(5)*a)

# done by harry
# num=int(input('enter your number:\n'))
# for a in range(1,11):
    # print(str(num) + 'X' + str(a) + '=' + str(num*a)) 
    # print(f"{num}X{a}={num*a}") # this is called f string.we can use this instead of individually writing str


'''write a program to greet all the person names stored in a list l1 and which starts with S'''
# l1=['Harry', 'Shrey', 'Soham', 'Sachin', 'Rahul']
# for name in l1:
#     if name.startswith('S'):
#         print('Greetings ' + name)



'''Write a program for multiplication of table using while loop'''
# num = int(input('enter your number:\n'))
# a = 1
# while a<11:
#     print(str(num) + 'X' + str(a) + '=' + str(num*a))
#     a=a+1
    



'''Write a program to find wether a given number is prime or not'''
# num = int(input('Enter your number:\n'))
# prime = True
# for a in range(2,num):
#     if num%a == 0:
#         prime = False
#         break
# if prime:
#     print('this number is a prime number')
# else:
#     print('this is not a prime number')



'''Write a program to find the sum of first n natural numbers using while loop'''
# num=int(input('Enter your number\n'))
# sum = 0
# for a in range(1,num+1):
#     sum = sum + a
# print(f'the summation of n natural numbers is {sum}')


# method2
# num = int(input('Enter your number\n'))
# a = 1
# sum = 0
# while a<(num+1):
#     sum = sum+a
#     a = a+1
# print(f'The sum of {num} natural number is {sum}')




'''write  a program to find the factorial of a given number using for loop'''
# n! = 1 X 2 X 3 X .... X ...n 
# 5! = 1 X 2 X 3 X 4 X 5


#method1
# num = int(input('Enter your number \n'))
# factorial = 1
# for a in range(1, num+1):
#     factorial = factorial*a
# print(f'The factorial of {num} is {factorial}')


#method2
# num = int(input('Enter your number \n'))
# factorial = 1
# for a in range(num):
#     factorial = factorial*(a+1)
# print(f'The factorial of {num} is {factorial}')



'''wriite a program to print following star pattern'''
'''*
   **
   ***''' 

# for i in range(3):
#     print('*' * (i+1))



'''wriite a program to print following star pattern'''
''' *
   ***
  ***** ''' 
n = 3
for i in range(3):
    print(' ' * (n-i-1), end='')
    print('*' * (2*i+1))


''' print multiplication table using for loop using reverse order'''
# num = int(input('Enter your number\n'))
# for i in range(-10,0):
#     print(f'{num} * {-i} = {-num*i}')



'''If you want to write continuous tables then use folllowing program'''

# for i in range(2,4):
#     for j in range(1,11):
#         print(f'{i}*{j}={i*j}')




'''Make a list and print only those things which are numbers and are greater than 6 using for loop'''
list = ['Shrey', 77, 2, 'Rishank', 3, 'Kamil']
for items in list:
    if (items).isnumeric() and items>6:
        print(f'{items} is greater than 6')    




'''Take input from user untill user does not give input greater than 100. 
Do this using break continue and while loop'''




# while True:
#     num = int(input('Enter any number\n'))
#     if num>100:
#         print('Congratulations you have entered number greater than 100')
#         break
#     else:
#         print('Try again')
#         continue



'''Write a program using for loop; A list contains numbers in form of strings
Write a program to convert them to integer'''

list = ['23','45','67','12']

# for i in range(len(list)):
#     list[i]=int(list[i])
#     print(list[i])











'''Example'''
# a = [2,5,7]
# str = ""
# index = 0
# for i in a:
#     str += (f'{i} a{index} +')
#     index = index +1
# print(str)

