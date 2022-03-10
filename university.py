import turtle

window_1 = turtle.Screen()
cursor_1 = turtle.Turtle()

def ellipse_shape(user_ellipse_big_radius_f,user_ellipse_small_radius_f):
    cursor_1.shape("circle")
    cursor_1.shapesize(user_ellipse_big_radius_f,user_ellipse_small_radius_f,1)
    cursor_1.fillcolor("white")
    window_1.mainloop()

user_ellipse_big_radius = int(input())
user_ellipse_small_radius = int(input())

ellipse_shape(user_ellipse_big_radius,user_ellipse_small_radius)

