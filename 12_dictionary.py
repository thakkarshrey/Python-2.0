# Dictionary is a collection of key value pairs
mydictionary = {
    'Shrey': 'An electrical engineer',
    'Marks': [10,8,8,9],
    'One more dictionary' : {'Shrey' : 'Not a player'},
    1 : 1999
}
print(mydictionary['Shrey'])
print(mydictionary['Marks'])
print(mydictionary['One more dictionary'])
print(mydictionary['One more dictionary']['Shrey'])
del mydictionary['Shrey'] # it will delete the key value pair associated with Shrey


mydictionarynew = mydictionary.copy() # it will copy mydictionary into mydictionarynew


'''Dictionary methods'''
print(mydictionary.keys()) # it will show the first word of dictionary
print(type(mydictionary.keys())) # its type is not a list but it is a diffferent type called dict_values
print(mydictionary.values()) # it will show you the second line or the meaning of the word
print(list(mydictionary.values())) # we can also indicate the dict_values intoo list
print(mydictionary.items()) # it will print the contents of dictionary as (keys, values)

updated_dictionary ={
    'Kamil' : 'Friend',
    'Shrey': 'A Coder',
}
mydictionary.update(updated_dictionary) 
# updates the dictionary by adding key value pairs from updated_dictionary
# it will also update a key's value if its already present in the dictionary
print(mydictionary)

print(mydictionary.get('Shrey')) # Prints the value associated with Shrey
print(mydictionary['Shrey'])# Prints the value associated with Shrey

'''The difference between .get and [] syntax'''

print(mydictionary.get('Shrey1')) # Prints as none as Shrey1 is not present in the dictionary
print(mydictionary['Shrey1']) # Throws an error as Shrey1 is not present in the dictionary





# Dictionary is unordered 
# Dictionary is mutable 