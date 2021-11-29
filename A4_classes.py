# class Dog:
    
# #    energy = "high"

#     def __init__(self,inputenergy): #when an object is created, create a variable called energy, set it to input (inputenergy) and set them in each instance.
#         self.energy = inputenergy

#     def speak(self):
#         print("woof")

# havoc = Dog("medium")
# havoc.speak()
# havoc.energy = "Low"
# print(havoc.energy)

# scooby = Dog("high")
# scooby.speak()
# print(scooby.energy)

# clifford = Dog("large")

#######################################
# QA Tutorial
# #######################################
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# John = Student("John", "21")
# Jane = Student("Jane", "22")

# print(getattr(Jane, "age"))

#########################################################################################################
# QA Exercise
# In a new Python file, create a class of students.
# It should contain the following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints the students average test score.
##########################################################################################################

#name of the class
# class Student: 
#     #default value for the name attribute
#     name = "Student"

#     # initialised attributes of the class
#     def __init__(self, name, age, score1, score2, score3): 
#     #attributes    
#         self.name = name
#         self.age = age
#         self.score1 = score1
#         self.score2 = score2
#         self.score3 = score3
#     #defines a function within the class
#     def average(self): 
#     #calculates the average of the 3 scores (assumes 3 scores entered)
#         avg = (self.score1 + self.score2 + self.score3)/3 
#     #returns the result of the function        
#         return avg 

#defines objects in the class and assigns attributes
# StudentA = Student("StudentA",15,20,21,30) 
# StudentB = Student("StudentB",10,15,12,8)

# #creates the variable from the function
# avg_scoreA = StudentA.average()
# avg_scoreB = StudentB.average()

# #prints result
# print(StudentA.name,"|",StudentA.score1,"|", StudentA.score2,"|", StudentA.score3,"|",avg_scoreA) 
# print(StudentB.name,"|", StudentB.score1,"|",StudentB.score2,"|",StudentB.score3,"|",avg_scoreB)
##########################################################################################################
# https://towardsdatascience.com/3-useful-projects-to-learn-python-classes-cf0076c36297
#
# Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, 
# clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each 
# category, as well computing category balances and transferring balance amounts between categories”
# Considerations: this is a very interesting project as it allows not only to comprehend how a class is 
# initialized and used, but also represented and used as input to other functions. You will learn how to add 
# methods to your classes and print them in a way that allows complex representation of your class object at 
# different points in the program. As a bonus, you will define a function that computes how much money you are 
# spending across class categories as a % of your total expenses, something that can be very useful for the 
# money-savvy programmers among you.
# Approach: define the purpose and flexibility of a class object; build its class methods using a modular 
# approach and develop an understanding for how different instances of the same class can interact.



# ## Polygon
# Goal: “Create class and sub-class objects which represent different geometrical shapes, such as Rectangles and Squares”
# ## Lottery Ball
# Goal: “Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each 
# color that are in the hat. Give the object the ability to pick a random number of balls from the hat, which will then be 
# used to compute the probability of picking a certain distribution of balls over a large number of experiments”