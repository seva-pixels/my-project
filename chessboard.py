import turtle

def draw_square(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_chessboard():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    square_size = 50

    colors = ["white", "black"]
    start_x = -200
    start_y = 200

    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            x = start_x + col * square_size
            y = start_y - row * square_size
            draw_square(t, x, y, square_size, color)

    t.hideturtle()
    screen.mainloop()

draw_chessboard()
