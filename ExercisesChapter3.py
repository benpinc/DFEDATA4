# The Python Workbook by Ben Stephenson
# Chapter 3 - Loop Exercises
#################################################################
# Exercise 61
# 
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
#
# numbers = 0
# count = 0

# zero_exit = False
# while not zero_exit:
# 	entry = int(input("Enter a value: "))
# 	if entry != 0:
# 		numbers = numbers + entry
# 		count = count + 1
# 	else:
# 		zero_exit = True 
		
# avg = numbers / count 
# print("The average is ", avg)
#####################################################################
# Exercise 62: Discount Table
# (18 Lines)
# A particular retailer is having a 60 percent off sale on a variety of discontinued
# products. The retailer would like to help its customers determine the reduced price
# of the merchandise by having a printed discount table on the shelf that shows the
# original prices and the prices after the discount has been applied. Write a program that
# uses a loop to generate this table, showing the original price, the discount amount,
# and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
# that the discount amounts and the new prices are rounded to 2 decimal places when
# they are displayed.
#
# import math
# original_price = [4.95, 9.95, 14.95, 19.95, 24.95]
# discount = 0.6
# for i in original_price:
#     discount_amount = float(i * discount)
#     print("${:.2f}".format(i), "{:.0%}".format(discount), "${:.2f}".format(discount_amount))
# #sale_price = float(original_price - discount_amount)

