import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()
polygon(bob, 7, 70)

ruby=turtle.Turtle()
polygon(ruby, 10, 70)

turtle.mainloop()
