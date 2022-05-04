# a="Shrey's" # use this if you have single quotes in your strings
# print(a)

# b='Shrey"s' 
# # it is valid
# print(b)

# c='Shrey's'
# # invalid 
# print(c)

greetings="Good morning, "
name= "Shrey"
# concatenating two strings
print(greetings+name)
print(greetings[6])
# but we cant change the name of letter
# for eg name[6]="d" -->does not work
print(greetings[0:3]) # this is called string slicing
print(greetings[:3]) # is  same as name[0:3]
print(name[-5:-1]) # --> is same as print(name[0:4])
# slicing with skip value
f="shreyisagenius"
print(f[0::3]) #  it will skip to every third alphabete and give seseu
print(f[1::3]) #  it will skip to every third alphabete and give hyans

