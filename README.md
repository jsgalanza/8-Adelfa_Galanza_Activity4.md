import math

## Hypotenuse Program

## This program is designed to find the hypotenuse of a triangle.

## Open this program in PyCharm and paste the code (Line 1-25)

## Input the value of the two shorter sides

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))

## This is the code that makes it work

side1squared = math.pow(side1,2)
side2squared = math.pow(side2,2)

sumofsides = side1squared + side2squared

math.sqrt(sumofsides)

## Expect your output here

print("The hypotenuse is ", math.sqrt(sumofsides))

## Name: Jairus S. Galanza
## Section: Adelfa
