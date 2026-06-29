
import turtle
import math

def draw_digital_bmw():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#050505")
    screen.title("BMW")
    screen.tracer(1)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    COLORS = {
        "blue": "#0066AD",
        "white": "#FFFFFF",
        "chrome": "#E0E0E0",
        "grey": "#A0A0A0",
        "black": "#111111"
    }

    def draw_circle_filled(x, y, radius, color):
        t.penup()
        t.goto(x, y - radius)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    def draw_ring(x, y, outer_r, inner_r, color):
        # Outer circle
        t.penup()
        t.goto(x, y - outer_r)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(outer_r)
        t.end_fill()
        
        draw_circle_filled(x, y, inner_r, COLORS["black"])

    def draw_arc_filled(cx, cy, radius, start_angle, end_angle, color):
        t.penup()
        t.fillcolor(color)
        t.begin_fill()
        # Move to center
        t.goto(cx, cy)
        t.pendown()
        # Draw arc
        steps = 60
        for i in range(steps + 1):
            angle = math.radians(start_angle + (end_angle - start_angle) * i / steps)
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            t.goto(x, y)
        t.goto(cx, cy)
        t.end_fill()

    cx, cy = 0, 0
    outer_ring = 180
    inner_ring = 155
    emblem_r = 150

    draw_ring(cx, cy, outer_ring, inner_ring, COLORS["chrome"])

    
    
    draw_arc_filled(cx, cy, emblem_r, 90, 180, COLORS["blue"])
    draw_arc_filled(cx, cy, emblem_r, 270, 360, COLORS["blue"])
    
    draw_arc_filled(cx, cy, emblem_r, 0, 90, COLORS["white"])
    
    draw_arc_filled(cx, cy, emblem_r, 180, 270, COLORS["white"])

    
    t.pensize(6)
    t.pencolor(COLORS["chrome"])

    
    t.penup()
    t.goto(-emblem_r, cy)
    t.pendown()
    t.goto(emblem_r, cy)

    
    t.penup()
    t.goto(cx, -emblem_r)
    t.pendown()
    t.goto(cx, emblem_r)

    
    t.penup()
    t.goto(cx, cy - emblem_r)
    t.pendown()
    t.pencolor(COLORS["chrome"])
    t.pensize(5)
    t.fillcolor("")
    t.circle(emblem_r)


    t.penup()
    t.goto(0, -outer_ring - 50)
    t.pencolor(COLORS["white"])
    t.write("BMW", align="center", font=("Arial", 28, "bold"))

    screen.mainloop()

draw_digital_bmw()


