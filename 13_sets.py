a = {1,4,6,3,8,6,5}
print(a)
print(type(a)) # it is of class set type
# A set is a collection of non repetitive items

b = {} # this syntax will make an empty dictionary and not empty set
print(type(b))

c = set() # correct method to make an empty set, it will show as class empty set
print(type(c))

'''methods of sets'''
# Adding values to an empty set 
c.add(4)
c.add(54)
c.add(54) # it wont add any repetitive items


# Lets try adding list in a set
# c.add([3,5,7,8]) # throws an error because a list can be changed and it is not hashable

# Lets try adding dictinary in a set
# c.add({3:8}) # throws an error because a dictionary can be changed and it is not hashable

# Cannot add list or dictinary in sets

c.add((3,5,8))
print(c)
print(len(c)) # will print the length of this set
c.remove(54) #  will remove 54 from set 
print(c)
c.pop() # will remove a random element from  the set
print(c)
c.clear() # will clear all the elements from the set
print(c)

