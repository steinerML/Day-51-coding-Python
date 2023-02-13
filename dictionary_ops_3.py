#Dictionary Operations

dictionary = {'ABBA': 'Associate Basket', 'MNN': 'Chinese News', 'FOX' : 'Fake Oligarchs', 'XNBC': 'Shake New BS', 'JDR': 'Democratic Deek'}

#Add MAVO to the dictionary
dictionary['MAVO'] = 'Music Allround'
print(dictionary)

#Create a list where all the values are in alphabetical order
voluit = sorted(dictionary.values())
print(voluit)
print(type(voluit))

#Acces JDR and XNBC elements
print(dictionary['JDR'])
print(dictionary['XNBC'])

#Access KEYS
print(dictionary.keys())

#Access VALUES
print(dictionary.values())

#DELETE ELEMENTS

#Delete dictionary DEL
dictionary2 = {'AB': 'Associate', 'N': 'Chinese', 'F' : 'Fake', 'BC': 'Shake New', 'DR': 'Democratic'}

# del dictionary2
# print(dictionary2)

#Clear, clears dictionary of all content but keeps the object.
dictionary2.clear()
print(dictionary2)

#Pop, deletes selected element
dictionary.pop('ABBA')
print(dictionary)

#Popitem, deletes last added element
dictionary.popitem() #Deletes MAVO
print(dictionary)

#DICTIONARY COMPREHENSION
new = {i:i**4 for i in (1,2,3,4,5)}
print(new)

#MERGE 2 DICTIONARIES
dict1 = {'H': 'High', 'L': 'Low'}
dict2 = {'1': 'Super', '2': 'Xtra'}

dict3 = dict1 | dict2
print(dict3)

#With Item Unpacking
dict3 = {**dict1, **dict2}
print(dict3)

#Append a Dictionary to a List
dictionary = ['Dataplan', 'Internet']
list1 = {'1': 0.5, '2': 0.33}

dictionary.append(list1.copy())
print(dictionary)
