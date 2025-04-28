import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    arc(t, r, 360)


bob = turtle.Turtle()
radius = 100

bob.pu()
bob.fd(radius)
bob.lt(90)
bob.pd()

circle(bob,radius)
turtle.mainloop()


'''
__main__ :
    bob    ---> turtle.Turtle()
    radius ---> 100
polyline:
    t      ---> bob
    n      ---> 158
    length ---> 3.9766995615060674
    angle  ---> 2.278481012658228
arc :
    t           ---> bob
    r           ---> 100
    angle       ---> 360
    arc_length  ---> 628.3185307179587
    n           ---> 158
    step_length ---> 3.9766995615060674
    step_angle  ---> 2.278481012658228
    
circle :
      t ---> bob
      r ---> 100

'''
      