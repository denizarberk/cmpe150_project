def draw_square_line(square_size):
    for j in range(square_size):
        print("*", end="")

def draw_triangle_line(triangle_size,i):
    for j in range(1,triangle_size - i):
        print(" ", end="")
    for o in range(i * 2 + 1):
        print("*", end="")
    for j in range(1,triangle_size - i):
        print(" ", end="")

def draw_inverted_triangle_line(inverted_triangle_size,i):
    for j in range(i):
        print(" ", end="")
    for o in range((inverted_triangle_size - i) * 2 - 1):
        print("*", end="")
    for j in range(i):
        print(" ", end="")

def draw_rectangle_line(width):
    for j in range(width):
        print("*", end="")

def draw_empty_rectangle_line(width):
    for j in range(width):
        print(" ", end="")

max_height=6

for line in range(max_height):
    draw_square_line(max_height)
    print(" ",end="")
    draw_triangle_line(max_height,line)
    print(" ",end="")
    draw_rectangle_line(10)
    print(" ",end="")
    draw_inverted_triangle_line(max_height,line)
    print(" ",end="")
    draw_square_line(max_height)
    print(" ",end="")
    print()