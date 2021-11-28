# The Python Workbook by Ben Stephenson
# Chapter 2 - If Statement Exercises
#################################################################
# Exercise 34: Even or odd?
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.
#
# entry = int(input("Please enter a number: "))
# if entry%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd") 
##################################################################   
# # Exercise 35 - Dog Years
#
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number
#
# entry = int(input("Enter your age: "))
# if entry <0:
#     print("error")
# elif entry <=2:
#     dog_years = entry*10.5
# else:
#     dog_years = (2*10.5)+((entry-2)*4)
# print(dog_years)
#########################################################################################
# Exercise 36 - Vowel or Consonant
#
# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.
#
# letter_entry = str(input("Enter a letter: "))
# if(letter_entry)==('a'):
#         print("vowel")
# elif(letter_entry)==('e'):
#         print("vowel")
# elif(letter_entry)=='i':
#         print("vowel")
# elif(letter_entry)=="o":
#         print("vowel")
# elif(letter_entry)=="u":
#         print("vowel")
# elif(letter_entry)=="y":
#         print("sometimes a vowel, sometimes a consonant")
# else: 
#         print("consonant")
#########################################################################################
# Exercise 37 - Name That Shape
#
# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.
# 
# entry = int(input("Enter the sides of the shape: "))
# if entry <3 or entry >10:
#     print("this is outside of the range")
# elif entry == 3:
#     print("Triangle")
# elif entry ==4:
#     print("Square")
# elif entry==5:
#     print("Pentagon")
# elif entry == 6:
#     print("Hexagon")
# elif entry == 7:
#     print("Heptagon")
# elif entry == 8:
#     print("Octagon")
# elif entry == 9:
#     print("Nonagon")
# elif entry == 10:
#     print("Decagon")

#########################################################################################
# 
# Exercise 38 - Month Name to Number of Days
#
# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed.

# entry = str.lower(input("Enter the month: "))
# if entry == "january" or entry == "march" or entry == "may" or entry == "july" or entry == "august" or entry == "october" or entry == "december":
#     print(31)
# elif entry == "february":
#     print("28 or 29")
# elif entry == "april" or entry == "june" or entry == "september" or entry == "november":
#     print(30)
# else:
#     print("Not a valid month")
#########################################################################################
# Exercise 39 - Sound Levels
#
# The following table lists the sound level in decibels for several common noises.
#Noise | Decibel level (dB)
#Jackhammer | 130
#Gas lawnmower | 106
#Alarm clock | 70
#Quiet room | 40
#
# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the level is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table

# entry = int(input("Enter the sound level in dBs: "))
# if entry == 130:
#     print("jackhammer")
# elif entry == 106:
#     print("Gas lawnmower")    
# elif entry == 70:
#     print("Alarm clock")
# elif entry == 40:
#     print("Quiet room")
# elif entry >130:
#     print("louder than a jackhammer")
# elif entry >106:
#     print("Between Gas lawnmower and jackhammer")
# elif entry >70:
#     print("Between Alarm clock and Gas lawnmower")
# elif entry >40:
#     print("Between quiet room and Alarm clock")
# else:
#     print("Quieter than a quiet room!")
#########################################################################################
# Exercise 40: Name that Triangle
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.
# side1 = int(input("Enter the length of side 1: "))
# side2 = int(input("Enter the length of side 2: "))
# side3 = int(input("Enter the length of side 3: "))
# if side1 == side2 == side3:
#     print("Equilateral")
# elif side1 != side2 and side2 != side3 and side1 != side3:
#     print("Scalene")
# else: 
#     print("Isosceles")
#
#########################################################################################
# Exercise 41 - Note to Frequency
# 
# The following table lists an octave of music notes, beginning with middle C, along
# with their frequencies
#Note Frequency (Hz)
#C4 261.63
#D4 293.66
#E4 329.63
#F4 349.23
#G4 392.00
#A4 440.00
#B4 493.88

# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed
# previously.
# Once you have your program working correctly for the notes listed previously you
# should add support for all of the notes from C0 to C8. While this could be done by
# adding many additional cases to your if statement, such a solution is cumbersome,
# inelegant and unacceptable for the purposes of this exercise. Instead, you should
# exploit the relationship between notes in adjacent octaves. In particular, the frequency
# of any note in octave n is half the frequency of the corresponding note in octave n+1.
# By using this relationship, you should be able to add support for the additional notes
# without adding additional cases to your if statement

# entry = str.upper(input("Enter the note/octave: "))
# entry_note = entry[0]
# entry_octave = int(entry[1])
# print(entry_note)

# if entry_note == "C":
#     base_result = 261.63
# elif entry_note == "D":
#     base_result = 293.66
# elif entry_note =="E":
#     base_result = 329.63
# elif entry_note =="F":
#     base_result = 349.23
# elif entry_note =="G":
#     base_result = 392.00
# elif entry_note == "A":
#     base_result = 440.00
# elif entry_note =="B":
#     base_result = 493.88

# entry_frequency = base_result/2**(4-entry_octave)
# print(entry_frequency)
#########################################################################################
