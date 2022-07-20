#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sandesh
#
# Created:     18/03/2022
# Copyright:   (c) Sandesh 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#let's use our knowledge of number equality to write code that tracks sales data
# for an online jeans retailer.
stock=600
jeans_sold=500
target=500

#to see if sales target was achieved
#jeans_sold == target

#now create the variable target_hit to store the result of the comparsion
target_hit = jeans_sold == target
print("Hit jeans sales target:")
print(target_hit)

#now current_stock to keep track of the remaining stock
current_stock = stock-jeans_sold

#to check if jeans are still in stock make sure current-stock not equal to 0
in_stock = current_stock != 0
print("Jeans are in stock: ")
print(in_stock)