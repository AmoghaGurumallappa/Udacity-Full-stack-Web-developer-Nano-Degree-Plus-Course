import turtle

#def draw_square(some_turtle):
 #   for i in range(1,5):
  #      some_turtle.forward(100)
   #     some_turtle.right(90)
        
def draw_art():
    
    window = turtle.Screen()
    window.bgcolor("white")
    a= turtle.Turtle()
    a.shape("turtle")
    a.color("yellow")
    a.speed(2)
    #for i in range(1,37):
     #   draw_square(a)
      #  a.right(10)
    c= turtle.Turtle()
    c.shape("turtle")
    c.color("blue")
    c.speed(2)
    for k in range(1,37):
        draw_Triangle(c)
        c.right(10)
    
    r= turtle.Turtle()
    r.shape("turtle")
    r.color("blue")
    r.speed(2)
    for x in range(1,37):
        draw_rombus(r)
        r.right(10)
    c.right(90)
    c.forward(300)
    window.exitonclick()
#def circle():
    #b= turtle.Turtle()
    #b.circle(100)
    #b.color("black")
    #b.shape("arrow")

def draw_Triangle(s_turtle):
    
    for i in range(1,4):
        s_turtle.forward(100)
        s_turtle.right(120)
def draw_rombus(r_turtle):
    
    for i in range(1,3):
        
        r_turtle.forward(100)
        r_turtle.left(45)
        r_turtle.forward(100)
        r_turtle.left(135)
       
        


draw_art()
#circle()



