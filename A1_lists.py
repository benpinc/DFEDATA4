#####################################################
#           LISTS, TUPLES, DICTIONARIES             #
#####################################################

List = ["Chips", "Peas", "Gravy", "Pie", "Fish"] #mutable
Tuple = ("Chips", "Peas", "Gravy", "Pie", "Fish") #tuple  - can't append, remove, etc. Can only count - fixed entity
String = "String" #immutable
Dictionary = {"Title":"Going Bananas","Author":"Ape Lincoln","Published":1961}

print(List[0]) #lists the first value
print(List[-1]) #returning the last value
print(List[0:2]) #slicing
# List.append("Sausages") #adds to the list #stores data
# List.remove("Sausage") #removes from list
print(Tuple[2]) # prints out the value of the index in a Tuple

#Lists within lists
List1 = ["A","B","C","D"]
List2 = ["E","F","G","H"]
List3 = ["I","J","K","L"]
ListAll = [List1, List2, List3]

#Find G (of a list within a list)
print(ListAll[1][2])

#printing out " ring" from "string" within the string
print(String[2:6])

#printing out from Dictionary (Key Value Pairs)
print(Dictionary["Title"]) #prints the title from a dictionary
print(Dictionary.get("Title")) #alternative to the above
print(Dictionary.keys()) #print the keys from a dictionary
print(Dictionary.values()) # print the values from a dictionary
print(Dictionary.keys(), Dictionary.values())

#To add to the dictionary, reference a key that doesn't yet exist
Dictionary["Price"] = 5.99

# converts Dictionary to a list via casting (using tuple)
ListFromDictionary = tuple(Dictionary.keys()) 

SetFromDictionary = set(Dictionary.keys()) # creates a set from Dictionary (unique values)

###################################################################################################################################
# QA Exercise
# books = {"The Handmaiden's Tale":"Margaret Atwood","The Hobbit":"J.R.R.Tolkien","Charlie and the Chocolate Factory":"Roald Dahl"}
# print(books["The Handmaiden's Tale"])
#
# You cannot query a key using a value
####################################################################################################################################