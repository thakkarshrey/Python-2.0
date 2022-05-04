'''write a program to create a dictionary of hindi words with values as their english translation.
 provide user with an option to look it up'''

# mydict = {
#     'kohinoor' : 'diamond',
#     'kharab' : 'bad',
# }
# print('Your options are', mydict.keys())
# a = input('Enter your hindi word :')
# # print(mydict[a]) # if the user writes a word not resent in the dictionary then it will throw an error
# print(mydict.get(a)) # this will show none if word is not present and not throw an error




'''write a program to input 8 numbers from the user and display all the unique numbers once'''
# num1 = int(input('Enter number 1 :\n'))
# num2 = int(input('Enter number 2 :\n'))
# num3 = int(input('Enter number 3 :\n'))
# num4 = int(input('Enter number 4 :\n'))
# num5 = int(input('Enter number 5 :\n'))
# num6 = int(input('Enter number 6 :\n'))
# num7 = int(input('Enter number 7 :\n'))
# num8 = int(input('Enter number 8 :\n'))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)



'''can we have a set with 18(int) and 18(str) as a value in it?'''
# b = {16,'16'} # yes both are different 
# print(b)


'''what will be the length of following set s'''
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)
# print(len(s))



'''what is the type of c = {}'''
# it is a class dictionary type 
# c = set() is a class set type

'''create an empty dictionary. allw 4 friends t enter their favourite language as values 
and use keys as their names. assume that names are unique'''

mydic = {}
a = input('Enter your fav lang Kamil:\n')
b = input('Enter your fav lang Sagar:\n')
c = input('Enter your fav lang Rishank:\n')
d = input('Enter your fav lang Neha:\n')

mydic['Kamil'] = a
mydic['Sagar'] = b
mydic['Rishank'] = c
mydic['Neha'] = d
print(mydic) 

# keys should be unique


'''can you change the value inside a list which is contained in the given set'''
s= {7, 8, 12, 'shrey', [1,2]}
# A list cannot be stored in a set. it will throw an error.
'''If we change the list into tuple the also we cannot change the value inside it 
because a tuple value cannot be changed.'''