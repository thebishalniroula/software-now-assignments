

# Question 3
# Create a program that uses a recursive function to generate a geometric pattern using Python's turtle graphics. The pattern starts with a regular polygon and recursively modifies each edge to create intricate designs.
# Pattern Generation Rules:
# For each edge of the shape:
# 1.
# Divide the edge into three equal segments
# 2.
# Replace the middle segment with two sides of an equilateral triangle pointing inward (creating an indentation)
# 3.
# This transforms one straight edge into four smaller edges, each 1/3 the length of the original edge
# 4.
# Apply this same process recursively to each of the four new edges based on the specified depth

print("Recursive Function to generate a geometric pattern using Python's turtle graphics")
print("**************************************************************************************")

import turtle


#drawing a koch-style edge based on recursion depth

def make_edge(length , depth):
    if depth == 0:
        turtle.forward(length)
    
    else:
        length /= 3


        make_edge(length , depth-1)
        turtle.right(60)


        make_edge(length , depth-1)
        turtle.left(120)


        make_edge(length , depth-1)
        turtle.right(60)


        make_edge(length , depth-1)



turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()
        

def make_polygon( sides, length , depth):
    angle = 360 / sides
    for n in range(sides):
        make_edge(length , depth)
        turtle.left(angle)


sides = int(input("Enter the number of sides : "))
length = int(input("Enter the  desired length of the side:"))
depth = int(input("Enter the desired recursion depth:"))

turtle.speed(0)
turtle.hideturtle()


make_polygon(sides, length , depth)

turtle.done()


print("**************************************************************************************")
print("***********************************END***********************************************")
