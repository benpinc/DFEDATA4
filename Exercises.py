# The Python Workbook by Ben Stephenson
# Introduction to Programming Exercises Chapter 1
##########################################################################################################
# # Exercise 2: Hello
# # (9 Lines)
# # Write a program that asks the user to enter his or her name. The program should
# # respond with a message that says hello to the user, using his or her name.

# name = input("Enter you name: ")
# print("Hello"+" "+name)
##########################################################################################################
# # Exercise 3: Area of a Room
# # (Solved—13 Lines)
# # Write a program that asks the user to enter the width and length of a room. Once
# # the values have been read, your program should compute and display the area of the
# # room. The length and the width will be entered as floating point numbers. Include
# # units in your prompt and output message; either feet or meters, depending on which
# # unit you are more comfortable working with.

# width = float(input("Enter the room width (in metres): "))
# length = float(input("Enter the room length (in metres): "))
# area = round(width * length,2)
# print(area,"m")
##########################################################################################################
# # Exercise 4: Area of a Field
# # (Solved—15 Lines)
# # Create a program that reads the length and width of a farmer’s field from the user in
# # feet. Display the area of the field in acres.

# width = float(input("Enter the field width (in feet): "))
# length = float(input("Enter the field length (in feet): "))
# area = round((width * length)/43560,2)
# print(area,"acres")
##########################################################################################################
# Exercise 5: Bottle Deposits
# (Solved—15 Lines)
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

# small = int(input("Enter the number of small containers 1 litre or less: "))
# large = int(input("Enter the number of containers greater than 1 litre: "))
# small_refund = small * 0.1
# large_refund = large * 0.25
# total_refund = small_refund + large_refund
# print("$",round(float(total_refund),2))
##########################################################################################################
# Exercise 6: Tax and Tip
# (Solved—17 Lines)
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

# cost = float(input("Total cost of meal: "))
# tax = 0.2
# tip = 0.18
# tax_value = cost*tax
# tip_value = cost*tip
# total = cost + tax_value + tip_value

# print("-------------------------------")
# print("Meal Cost: $","%.2f" % cost)
# print("Tip: $","%.2f" % tip_value)
# print("Tax: $","%.2f" % tax_value)
# print("Total: $","%.2f" % total)
# print("-------------------------------")
##########################################################################################################
# Exercise 7: Sum of the First n Positive Integers
# (Solved—12 Lines)
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n.

# n = float(input("Enter a number: "))
# sum_of_integers = (n*(n+1))/2
# print("The sum of the integers from 1 to",n,"is: ",sum_of_integers)
##########################################################################################################
# Exercise 8: Widgets and Gizmos
# (15 Lines)
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

# widgets = int(input("Enter the number of widgets: "))
# gizmos = int(input("Enter the number of gizmos: "))
# total_weight_kg = ((widgets*75)+(gizmos*112))/1000
# print("The total weight is: ", total_weight_kg, "kg")

############################################################################################################################################### NOT STARTED
# Exercise 9: Compound Interest
# (19 Lines)
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.
############################################################################################################################################### NOT STARTED

# Exercise 10: Arithmetic
# (Solved—20 Lines)
# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# This copy belongs to 'acha04'
# 6 1 Introduction to Programming Exercises
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a
# b

# import math

# a = int(input("Enter the first integer here: "))
# b = int(input("Enter the second integer here: "))

# sum = a+b
# difference = b-a
# product = a*b
# quotient_a_div_b = a/b
# quotient_b_div_a = b/a
# remainder_a_div_b = a % b 
# log10a = math.log10(a)
# a_to_the_power_of_b = a**b

# print("Sum: ", sum)
# print("Diff: ", difference)
# print("Product: ", product)
# print("Quotient A/B: ", quotient_a_div_b)
# print("Quotient B/A: ", quotient_b_div_a)
# print("Remainder A/B: ", remainder_a_div_b)
# print("Log10a: ", log10a)
# print("a to the power of b: ", a_to_the_power_of_b)
##########################################################################################################
# Exercise 11: Fuel Efficiency
# In the United States, fuel efficiency for vehicles is normally expressed in miles-per gallon (MPG). 
# In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). Use 
# your research skills to determine how to convert from MPG to L/100 km. Then create a program that 
# reads a value from the user in American units and displays the equivalent fuel efficiency in Canadian 
# units.

# x = float(input("Enter fuel in US units: "))

# # miles to kilometre conversion
# km_per_mile = 1.609344
# gallon_per_liter = 3.78541178

# a = 100 * gallon_per_liter # 100 gallons into liters
# b = x * km_per_mile # input MPG into km
# c = a / b

# print(x," MPG (US) is the same as", round(c,3), "L/100km")

# Exercise 12: Distance Between Two Points on Earth
# (27 Lines)
# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.
# import math
# import numpy

# t1 = math.radians(float(input("Enter latitude point 1")))
# g1 = math.radians(float(input("Enter longitude point 1")))
# t2 = math.radians(float(input("Enter latitude point 2")))
# g2 = math.radians(float(input("Enter longitude point 2")))

# distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))

# km_to_miles = 0.621371 * distance
# print(t1,g1,t2,g2)
# print("Distance: ", round(distance,2),"km")
# print("Distance: ", round(km_to_miles,2), "miles")
