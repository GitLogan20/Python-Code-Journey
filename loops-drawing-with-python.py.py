#Grab a python code package or module named turtle.
import turtle

#Assign the activation application to the letter "t". "t" allows us to control
#or point to turtle.
t = turtle.Pen()

#Utilizing 2 of turtles functions (color & begin_fill) with the turtle package.
t.color('yellow','purple')
t.begin_fill()

#Conducting variable initialization to keep track of how many loops are being
#conducted in the code. Basically, you created a "count" outside of our "for loop"
count = 0

#Drawing a star while utilizing a for loop with a range.
for x in range(1,15):
    t.forward(300)
    t.left(225)
    '''This count variable increases the count value by "1".
       This would'nt be possible if we did not first, assign "0" to count variable value
       prior to adding a "1" (count = count + 1) to the count variable.
    '''
    count = count + 1
    print('Count is: ' + str(count))


    #Stop drawing after 8 loops
    #if count > 7 and count < 12:

    #This conditional if statement will print after the 8th loop because 8 is greater
    #than 7.
    if count > 7:
        print('The star pattern is complete!')
        break


#This turtle function fills our start with color.
t.end_fill()
print('A star is born!')







'''
#Bringing in the Python programming drawing package called turtle
import turtle

#Activate the turtle import package
tut = turtle.Pen()
# Draw a Cross
for x in range(1):
    tut.left(200)
    tut.forward(100)
    tut.right(90)
    tut.forward(100)
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.forward(50)
    tut.right(90)
    tut.forward(40)
    tut.forward(50)
    tut.right(90)
    tut.forward(100)
    tut.forward(50)
    tut.left(90)
    tut.forward(100)
    tut.right(90)
    tut.forward(80)
    tut.forward(20)
    tut.right(90)
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.forward(50)
    tut.right(90)
    tut.forward(90)
    tut.right(90)
    tut.forward(100)
    tut.forward(50)
    tut.right(90)
    tut.right(90)
    tut.right(90)
    tut.forward(150)
    tut.forward(40)
    tut.forward(10)
print('This cross is finished')
print('Lets draw another cross, this is fun!!!')

for x in range(1,9):
    tut.left(200)
    tut.forward(100)
    tut.right(90)
    tut.forward(100)
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.forward(50)
    tut.right(90)
    tut.forward(40)
    tut.forward(50)
    tut.right(90)
    tut.forward(100)
    tut.forward(50)
    tut.left(90)
    tut.forward(100)
    tut.right(90)
    tut.forward(80)
    tut.forward(20)
    tut.right(90)
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.forward(50)
    tut.right(90)
    tut.forward(90)
    tut.right(90)
    tut.forward(100)
    tut.forward(50)
    tut.right(90)
    tut.right(90)
    tut.right(90)
    tut.forward(150)
    tut.forward(40)
    tut.forward(10)
print('IT IS FINISHED!!')
'''



