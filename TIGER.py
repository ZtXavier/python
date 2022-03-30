import turtle as tl 

def set_start(x,y,w,c=COLOR):
    tl.penup()
    tl.setx(x)
    tl.sety(y)
    tl.setheading(tl.towards(0,0))
    tl.width(w)
    tl.pencolor(c)
    tl.pendown()
    tl.speed(0)
    
def left_rotate(time,angle,length):
    for i in range(time):
        tl.left(time)
        tl.forward(length)

def fill_color(color):
    def decorator_all(func):
        def wrapper(*args, **kwargs):
            
        



