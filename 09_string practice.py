'''Write a program to display a user entered name followed by Good Afternoon 
using input () function'''
# name = input('What is your good name sir?\n')
# print('Good Afternoon, ' + name)



'''write a program to fill in a letter template given with name and date''' 
# letter = '''Dear <|Name|>,
# This is to inform you that you have cleared the interview and are selected for further round. 
# Thanks and regards, 
# Have a nice day.
# Date: <|Date|>'''# We will need to replace name and date so we will use replace function
# name = input("Please enter your name\n")
# date = input("Please enter the date you applied for the interview\n")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)
# print(letter)



'''Write a program to detect double spaces in a string'''
# story = "I love to play football and also fitness is my    passion."
# Doublespaces = story.find("  ")
# print(Doublespaces)
'''replace the double spaces with single spaces'''
# story = story.replace("    "," ")
# print(story)



'''write a pogram to format the following letters using  escape sequence characters'''
# letter = "Dear Shrey, This Python course is nice. Thanks!"
# print(letter)
# editedletter = "Dear Shrey,\n\t This Python course is nice.\n\t\t\t\t Thanks!"
# print(editedletter)