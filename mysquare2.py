import turtle


def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


ruby = turtle.Turtle()

square(ruby,200)

ella = turtle.Turtle()

square(ella,100)



turtle.mainloop()