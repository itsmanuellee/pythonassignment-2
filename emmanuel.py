
#NAME:                     AJAYI EMMANUEL OLAMILEKAN
#MATRIC NO:         CSC / 15 / 4045
#DEPARTMENT:     COMPUTER SCIENCE
#USING Python 2 . 7 . 13
#GROUP 1, NO 1A


#A python program to compute a mathematical expression

import math
#input the value for radius
radius = int(input("please enter value for radius:  "))

#input the value for angle
angle = int(input("please enter value for angle in degree:  "))

r = radius
a = angle

#To solve for trigonometry functions, use math function
s1 = float (r * ( ( math.cos (math.radians ( a ) ) ) ** 2) )
s2 = float (r * ( ( math.sin ( math.radians ( a ) ) ) ** 2) )

#add s1 and s2 together and store in my_sum
my_sum = float ( s1 + s2 )

#To find the sqaure root of the sum of s1 and s2, use math function, then,
#store value in result
result = float (math.sqrt(my_sum) )

#print the result
print ("the result is ", result )
