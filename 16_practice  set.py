'''write a program to find greatest of 4 numbers entered by the  user'''
# num1 = input('Enter your number1 :')
# num2 = input('Enter your number2 :')
# num3 = input('Enter your number3 :')
# num4 = input('Enter your number4 :')

# if(num1>num2):
#     a1 = num1
# else:
#     a1 = num2


# if(num3>num4):
#     a2 = num3
# else:
#     a2 = num4


# if(a1>a2):
#     print(str(a1) + 'is the greatest')
# else:
#     print(str(a2) + 'is the greatest')




'''write a program to find out if a student is pass or fail if it requires total 40 % and 
at least 33% in each subject to pass. assume 3 subjects and take marks from the user'''
# m1 = int(input('Enter your marks scored in English'))
# m2 = int(input('Enter your marks scored in Science'))
# m3 = int(input('Enter your marks scored in Maths'))
# if(m1<33 or m2<33 or m3<33):
#     print('You are failed because you have less than 33% in one subject')
# elif((m1+m2+m3)/3) <40:
#     print('You have failed due to total percentage less than 40')
# else:
#     print('Congratulations! You have passed the examination')



'''a spam comment is defined as a text containing following key words:
"Make a lot of money","buy now", "subscribe this", "click this". Write a program to detect these spams.'''
comment = input('Enter any text:\n')
if("make a lot of money" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("subscribe this" in comment):
    spam = True
elif("click this" in comment):
    spam = True
else:
    spam = False

if(spam):
    print('This text is spam')
else:
    print('This is not spam')

'''write a program to find wether a given username has less than 10 characters or not'''
# username = input("Enter any name")
# print(len(username))
# if(len(username)<10):
#     print('The length of username has less than 10 characters')
# else:
#     print('the length of username has more than 10 characters')


'''Write a program to find out if a given name is present in a list or not'''
# a=['shrey', 'kamil', 'sagar', 'rishank']
# name=input('Please enter your name: \n')
# if(name in a):
#     print('your name is pressent in the list')
# else:
#     print('your name did not make the list')


'''write a program to calculate the grade of a student frm his marks from following
90 - 100  Ex
80 - 90   A
70 - 80   B
60 - 70   C
50 - 60   D
<50       F'''
# marks=int(input('Enter your marks:\n'))
# if(marks>90 and marks<=100):
#     print('EX')
# elif(marks>80 and marks<=90):
#     print('A')
# elif(marks>70 and marks<=80):
#     print('B')
# elif(marks>60 and marks<=70):
#     print('C')
# elif(marks>50 and marks<=60):
#     print('D')
# elif(marks<50):
#     print('F')

    #OR

# marks=int(input('Enter your marks:\n'))
# if(marks>=90):
#     grade = 'EX'
# elif(marks>=80):
#     grade = 'A'
# elif(marks>=70):
#     grade = 'B'
# elif(marks>=60):
#     grade = 'C'
# elif(marks>=50):
#     grade = 'D'
# else:
#     grade = 'F'
# print('Your grade is: '+ grade)




'''write a program to find out if this post is taking about shrey or not'''
post = input('Write anything:\n')
check = "Shrey"
if(check.upper() in post.upper()):
    print('Yes this post is taking about shrey')
else:
    print('No this post is not taing abut shrey')