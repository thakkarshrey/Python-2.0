"r" - 'open file for reading'
"w" - 'open file for writing'
"x" - 'creates file if it does not exists'
"a" - 'add more content to a file'
"t" - 'text mode'
"b" - 'binary mode'
"+" - 'read and write' 

'''Reading a file'''

# Use open function to read the function of a file
# r can be used to read the data 

# f = open('sample.txt', 'r') # by default the mode is in read mode so we can also write it as open('sample.txt')
# f = open('sample.txt') # --> this works fine 
# data = f.read()
# print(data)
# f.close()




# f = open('sample.txt')
# data = f.read(7) # will read first seven characters from the .txt file
# print(data)
# f.close()



# f = open('sample.txt')
# # It will read first line
# data = f.readline()
# print(data)

# # It will read second line
# data = f.readline()
# print(data)

# # It will read third line
# data = f.readline()
# print(data)
# f.close()


# f = open ('sample.txt')
# print(f.readlines())
# This will read lines of the txt file and print them in form of list



# This is how you can print lines using iteration
# f = open ('sample.txt')
# for line in f:
#     print(line)


'''Writing a file'''

# a = open('another.txt', 'w') # 'w' will only overwrite the file and not add any additional data again and again 
# a.write('idhar jo bhi likha hai vo iss file mei aa jaye')
# a.close()


# if i want to add another file in the data then i will use 'a'
# a = open('another.txt', 'a') 
# a.write(' kya haal hai bhai \n')
# a.close()



'''Handle read and write both'''
# f = open('sample2.txt','r+')
# data = f.read()
# print(data)
# f.write('ha malum hai tere baap ko mat sikha')





'''with statement'''
# with open('another.txt','r') as f:
#     a = f.read()
# print(a)                         # the advantage here is that there is no need to use close function

# with open('another.txt', 'w') as f:
#     a = f.write('abe jaa na bc')
# print(a)                          # the advantage here is that there is no need to use close function




'''Tell function'''

