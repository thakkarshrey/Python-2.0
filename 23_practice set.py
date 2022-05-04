'''write a program to read the text from a given file'poem.txt', and find out whether it contains the word 'twinkle' '''


# a = open('poem.txt', 'r')
# data = a.read()
# if 'twinkle' in data:
#     print('Twinkle is present')
# else:
#     print('Twinkle is not present')
# a.close()


'''the game function in a program lets the user play a game andd return
the score as an integer. you need too read a file 'Hiscore.txt' which is ether blank or contains the 
previous Hi-score. you need to write a program to update the Hi-score whenever game() breaks the Hi-score'''


# def game():
#     return 56

# score = game()

# with open('hiscore.txt','r') as f:
#     hiscore =int(f.read())
# if hiscore<score:
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))


# this program will not work when the hiscore.txt file is blank. so for that...


# def game():
#     return 321

# score = game()

# with open('hiscore.txt','r') as f:
#     hiscore =(f.read())
# if hiscore =='':
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))

# elif int(hiscore)<score:
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))



'''a file contains a word donkey multiple times. you need to write a program which replaces this word 
with ###### by updating the same file'''

# with open('poem.txt',) as f:
#     content = f.read()

# content = content.replace('donkey', '$$$$$$')

# with open('poem.txt', 'w') as f:
#     f.write(content)


'''repeat the above program for a list of such words to be cencored'''
# a = ['twinkle', 'donkey', 'pagal', 'bekar admi']
# with open('poem.txt',) as f:
#     content = f.read()
# for words in a:
#     content = content.replace('twinkle', '!!!!!!!')
#     content = content.replace('donkey', '@@@@@@')
#     content = content.replace('pagal', '$$$$$')
#     content = content.replace('bekar admi', '????? ????')
# with open('poem.txt', 'w') as f:
#     f.write(content)
# this is how we can replace individual words with different texts 



# a = ['twinkle', 'donkey', 'pagal', 'bekar admi']
# with open('poem.txt',) as f:
#     content = f.read()
# for words in a:
#     content = content.replace(words, '!!!!!!!')
# with open('poem.txt', 'w') as f:
#     f.write(content)
# this is how we can replace all the words with same text





'''write a program to mine a log file and find wether it contains 'python'.'''
# method1
# with open('log.txt') as f:
#     content = f.read().lower()

# if 'python' in content:
#     print('yes python is present')
# else:
#     print('no python is not present')


# method2
# with open('log.txt') as f:
#     content = f.read()

# if 'python' in content.lower():
#     print('yes python is present')
# else:
#     print('no python is not present')



'''write a program to find out the line number where python is present from the above question'''
content = True
i = 1 # this indicates the line number
with open('log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content, end='')
            print(f'yes python is present in line number {i}')
        i+=1       



'''write a program to make a copy of text file this.txt'''
# with open('poem.txt') as f:
#     content = f.read()

# with open('C:\\Users\\KRUTIKA\\Desktop\\poem1.txt', 'w') as f:
#     f.write(content)




'''write a program to find wether a file is identical and matches the content of another file'''
# with open('poem.txt') as f:
#     content = f.read()
# with open('poem1.txt') as f:
#     content1 = f.read()

# if content==content1:
#     print('files are identical')
# else:
#     print('files are not identical')



'''write a program to wipe out the contents of a file using python'''
# method1
# with open('poem.txt') as f:
#     content = f.read()
#     content = content.replace(content, ' ')
# with open('poem.txt', 'w') as f:    
#     f.write(content)

# easiest method2
# with open('poem.txt', 'w') as f:    
#     f.write(' ')



'''Write a python program to rename a file to renamed_by_python.txt'''
# import os
# oldname = 'poem.txt'
# newname = 'renamed_by_python.txt'

# with open(oldname) as f:
#     content = f.read()

# with open(newname, 'w') as f:
#     f.write(content)
# os.remove(oldname)

# this wont replace the name of file but if i delete the oldname file then it will replace it
# for that i will have to download a module which removes the old file
