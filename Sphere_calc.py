"""
Program: sphere.py
Author: Jcosg336
Date: 1/30/2020

This program is used to calculate the diameter, circumference,
surface area, and volume of a sphere.

Input:  Radius of a sphere as an int or float
Output: Diameter, circumference, surface area, and volume of a sphere
        with supplied radius
"""
import math

radius = float(input("Input a value for the radius of a sphere "))   #get user data for the radius
                                                                     #to be calculated"""

Pi = float(math.pi)                               #assign the value of Pi to a variable

diameter = 2 * radius                             #calculate diameter
circum = diameter * Pi                            #calculate circumference
surfArea = 4 * Pi * radius * radius               #calculate surface area
volume = 4/3 * Pi * radius * radius * radius      #calculate volume

print("\nThe sphere's radius entered: ", radius)  #print user defined radius and previous calculations 
print("Diameter: ", diameter)
print("Circumference: ", circum)
print("Surface Area: ", surfArea)
print("Volume: ", volume)
