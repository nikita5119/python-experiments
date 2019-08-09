# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

position=[0,0]
while True:
    a= input("enter the direction and steps :")
    if not a:
        break
    direction, steps= a.split(' ')
    steps=int(steps)
    
    if (direction== "up"):
        position[0]= position[0]+steps
    elif (direction=="down"):
        position[0]=position[0]-steps
    if (direction=="right"):
        position[1]=position[1]+steps
    elif (direction=="left"):
        position[1]=position[1]-steps
print(position)
distance=(position[0]**2+position[1]**2)**(1/2)
print(distance)