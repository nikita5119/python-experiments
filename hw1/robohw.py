position=[0,0]
while True:
    a= input("enter the direction and steps :")
    if not a:
        break

    try:
        direction, steps= a.split(' ')
        steps=int(steps)
        if(direction== "up"):
            position[0]= position[0]+steps
        elif (direction=="down"):
            position[0]=position[0]-steps
        if (direction=="right"):
            position[1]=position[1]+steps
        elif(direction=="left"):
            position[1]=position[1]-steps


    except:
        print("you're suppose to enter a number u dumboo!, except block!")
        #break
    
print(position)
distance=(position[0]**2+position[1]**2)**(1/2)
print(distance)