'''while loop'''

a = 0 
while(a<10): # it will create a loop and evalute it untill the condition is true
    print('Yes' + str(a)) 
    a=a+1 # a will increment 1 untill it reaches 10...... will be executed untill the value reaches 10
print('done')

'''write a program to print 1 to 50 using while loop'''
# a = 1
# while(a<=50): 
#     print(a) 
#     a=a+1 
# print('done')




'''print shrey 5 times'''
# a = 0
# while(a<5): 
#     print('Shrey') 
#     a=a+1 
# print('done')


''' write a prgram to print the contents of list using while loops'''
# fruits = ['banana', 'mango', 'watermelon', 'grapes', 'apple']
# a=0
# while a<len(fruits):
#     print(fruits[a])
#     a=a+1



'''for loop'''
''' write a prgram to print the contents of list using for loops'''
# fruits = ['banana', 'mango', 'watermelon', 'grapes']
# for item in fruits: # easier to execute as compared to while loop
#     print(item)

 #range function
# for a in range(8): # it will print number from 0 to 7
#     print(a)



# for b in range(1,8): # it will print number from 1 to 7
    # print(b)



# for c in range(1,8,2): # it will print number from 1,3,5,7. it is callled step size
#     print(c)


# if you want to print the items of a dictionary then.....
# list1 = [['Shrey', 1], ['Shreya', 3], ['Thakkar', 2]]
# mydict = dict(list1)
# for names, chocolates in mydict.items():   # if you dont write mydict.items() then it wont print 
#     print(names, chocolates)


'''for loop with else'''
# for i in range(10):
#     print(i)
# else:
#     print('this is done') # when loop becomes false then else will be executed 



'''break statement'''
# for i in range(10):
#     print(i)
#     if i==5:
#         break
# else:
#     print('this is done') # when you break the loop then else will not be executed 



'''continue statement'''
# for i in range(10):
#     if i==5:
#         continue # it will skip the value of 5 and print he rest of the values
#     print(i)


'''pass statement'''
# pass is a null statement in python. it means to do nothing

# i=0
# while i>3:
#     pass
# print('this job is done')



# '''Break and continue using for loop'''
# i = 0
# while True:
#     if i<5:
#         i = i+1
#         continue
#     print(i)

#     if i == 10:
#         break
#     i = i+1




# age = 0
# while age<10:
#     age+=1
#     if age==5:
#         continue

#     if age==8:
#         print('It ends here')
#         break
#     print(age)