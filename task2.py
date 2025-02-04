import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)
    t.left(45)

    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    
    t.right(90)

    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    
    t.left(45)
    t.backward(length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.pencolor("purple")

    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
    
    length = 100
    
    draw_pythagoras_tree(t, length, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
