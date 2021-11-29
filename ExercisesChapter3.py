# The Python Workbook by Ben Stephenson
# Chapter 3 - Loop Exercises
#################################################################
# Exercise 61
# 
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
# #
# numbers = 0
# count = 0
#
# zero_exit = False
# while not zero_exit:
# 	entry = int(input("Enter a value: "))
# 	if entry != 0:
# 		numbers = numbers + entry
# 		count = count + 1
# 	else:
# 		zero_exit = True 
#		
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
# original_price = [4.95, 9.95, 14.95, 19.95, 24.95]
# discount = 0.6
# for i in original_price:
#     discount_amount = float(i * discount)
#     print("${:.2f}".format(i), "{:.0%}".format(discount), "${:.2f}".format(discount_amount))
#####################################################################
# Exercise 63: Temperature Conversion Table
# 
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.

# for celsius in range(0,101,10):
# 	fahrenheit = celsius * (9/5) + 32
# 	print("Celsius:","{:.1f}".format(celsius),"Fahrenheit:","{:.1f}".format(fahrenheit))
#####################################################################
# Exercise 64: No More Pennies
#
# February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
# Mint. Now that pennies have been phased out retailers must adjust totals so that they
# are multiples of 5 cents when they are paid for with cash (credit card and debit card
# transactions continue to be charged to the penny). While retailers have some freedom
# in how they do this, most choose to round to the closest nickel.
# Write a program that reads prices from the user until a blank line is entered.
# Display the total cost of all the entered items on one line, followed by the amount
# due if the customer pays with cash on a second line. The amount due for a cash
# payment should be rounded to the nearest nickel. One way to compute the cash
# payment amount is to begin by determining how many pennies would be needed to
# pay the total. Then compute the remainder when this number of pennies is divided
# by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
# the total up.
#
