import tkinter as tk
from math import sin, cos, radians

def draw_chakra(canvas, center_x, center_y, radius):
    # Drawing the 24 spokes first

    
    # Drawing the blue circle
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill='#ffffff', outline='#000080')

    for i in range(24):
        angle = radians(i * 15)
        start_x = center_x + (10 * cos(angle))  # Minor adjustment to the starting point
        start_y = center_y - (10 * sin(angle))
        end_x = center_x + (radius * cos(angle))
        end_y = center_y - (radius * sin(angle))
        canvas.create_line(start_x, start_y, end_x, end_y, fill='#000080', width=3)

    # Drawing the small white circle at center
    small_circle_radius = radius / 7
    canvas.create_oval(center_x - small_circle_radius, center_y - small_circle_radius, center_x + small_circle_radius, center_y + small_circle_radius, fill='#000080')


def main():
    root = tk.Tk()
    root.title("Flag of India")

    canvas = tk.Canvas(root, width=600, height=400, bg='white')
    canvas.pack()

    # Saffron color band
    canvas.create_rectangle(0, 0, 600, 133, fill='#FF9933', outline='#FF9933')

    # White color band (with Ashoka Chakra)
    canvas.create_rectangle(0, 133, 600, 266, fill='#FFFFFF', outline='#FFFFFF')
    draw_chakra(canvas, 300, 200, 65)

    # Green color band
    canvas.create_rectangle(0, 266, 600, 400, fill='#138808', outline='#138808')

    root.mainloop()

if __name__ == '__main__':
    main()
