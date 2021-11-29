###################################################
#                   FOR LOOPS                     #
###################################################

List = ["Chips", "Peas", "Gravy", "Pie", "Fish"]
List2 = ["Sausage", "Scampi"]
ListAll = [List,List2]
# #used when indexed list
# #loops each index in turn
for i in ListAll:
    print(i)
terminates at end of list

String = ("Chips")
#prints each character in a string one-by-one
for a in String:
    print(a)

#prints the List five times
for i in range(5):
    print(List)

for b in range(5,10,2): #index 5 times, up to value of 10 in steps of 2, i.e. 2,4,6,8)
    print(List)

######################################################
#                     WHILE LOOPS                    #
######################################################
Score = 500
while Score > 100:
    Score = int(input("Enter a score: "))
if Score >=85:
    print("Dist")
elif Score >=65:
    print("Merit")
elif Score >=45:
    print("Pass")
elif Score >=0:
    print("Fail")
else:
    print("Invalid Score")

#######################################################
#             BREAK AND CONTINUE                      #
#######################################################
List = ["Chips", "Peas", "Gravy", "Pie", "Fish"]
for i in List:
    if i == "Peas":
        break #stops the loop and prints up to this point in the index
    print(i)

List = ["Chips", "Peas", "Gravy", "Pie", "Fish"]
for a in List:
    if a == "Peas":
        continue #passes over the data in the conditional and continues to loop
    print(a)
#
#
#######################################################
#                NESTED LOOP                          
# List = ["Chips", "Peas", "Gravy", "Pie", "Fish"]
# List2 = ["Sausage", "Scampi"]
# ListAll = [List,List2] #as this var is based on two lists, the nested loop will populate one list of individual items.  Without it, it will print List and List2 on one row each.
# for a in ListAll:
#     for aSub in a:
#         print(aSub)
########################################################
count = 0
newname = []
while count<5:
    name = input("Enter you name: ")
    newname.append(name)
    count = count + 1

for a in newname:
    print(a, "is awesome")