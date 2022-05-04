#recursion is a function which calls itself
# n! = 1 X 2 X 3 X 4....n
num = 5
factorial = 1
for a in range(num):
    factorial = factorial*(a+1)
print(factorial)


'write the program to find factorial using function'
# def factorial_iter(num):
#     factorial = 1
#     for a in range(num):
#         factorial = factorial*(a+1)
#     return factorial

# d = factorial_iter(12)
# print(d)



# Now, n! = 1 X 2 X 3 X 4....X n
# n! = 1 X 2 X 3 X 4....[n-1] X n 
# n! can also be written as n! = [1 X 2 X 3 X 4....n-1] X n
# Therefore, n! = (n-1)! X n

# def factorial_recursive(num):
#     return num*factorial_recursive(num-1)
# f = factorial_recursive(5)
# print(f)

# it will throw an error beacuse when num becomes 0 then the answer will go negative like -1, -2
# therefore,


# def factorial_recursive(num):
#     if num==1 or num ==0:
#         return 1
#     return num*factorial_recursive(num-1)
# f = factorial_recursive(3)
# print(f)




'''Fibonacci function'''
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num2 = int(input("Enter the number\n"))
print(fibonacci(num2))
