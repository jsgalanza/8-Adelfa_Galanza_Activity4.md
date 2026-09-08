import math

## Hypotenuse Program

## Program is designed to find the hypotenuse of a triangle.

## Input the value of the two shorter sides

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))

side1squared = math.pow(side1,2)
side2squared = math.pow(side2,2)

sum = side1squared + side2squared

math.sqrt(sum)

## Expect your output here

print("The hypotenuse is ", math.sqrt(sum))

## Name: Jairus S. Galanza
## Section: Adelfa
