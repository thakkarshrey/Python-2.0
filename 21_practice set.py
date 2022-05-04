'''Write a program to find the grestest of three number'''

# def greatest(num1, num2, num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3         

# a = greatest(33,9,10)
# print('the greatest number is ' + str(a))



'''write a program t convert celcius to farenheit using function'''
# def temperature(celcius):
#     return ((celcius*(9/5)) + 32)
# farenheit = temperature(0)
# print(f'the value of fareinheit is {farenheit} °F')   



'''how do you prevent a python print() function to print a new line at the end'''
# print('hello', end=' ')
# print('how', end=' ')
# print('are', end=' ')
# print('you?', end=' ')


'''write a recursive funtion to calculate the sum of first n natural numbers'''
# if n! = 1 X 2 X 3 X 4....X n can be written as n! = (n-1)! X n 
# then sum(n) = sum(n-1) + n


# def sum(n):
#     if n==0:
#         return n==1
#     return sum(n-1) + n
# a=sum(3)
# print(a)


'''write a pythn function to print first n lines of following pattern
***
**
*'''
# n = 5
# for a in  range(n):
#     print('*'*(n-a)) # prints * n-a times



'''What is strip function?'''
# this = '     shrey is good       '
# print(this)
# print(this.strip()) # it removes the spaces 



'''write a python function to remove a given word from a string and strip'''

# def remove(string, word):
#     newstring = string.replace(word, '')
#     return newstring
# this = '     shrey is good       '
# a = remove(this, 'shrey')
# print(a)


'''Including strip'''
# def remove(string, word):
#     newstring = string.replace(word, '')
#     return newstring.strip()
# this = '     shrey is good       '
# a = remove(this, 'shrey')
# print(a)



'''write a program to print multiplication of a given number using python function'''
# method1
# num = int(input('enter your number\n'))
# for a in range(1,11):
#     print(f'{num} X {a} = {num*a}')

#method2
# num = int(input('enter your freaking number\n'))
# a = 1
# while a<11:
#     print(f'{num} * {a} = {num*a}')
#     a=a+1


              