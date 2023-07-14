def draw_square_line(square_size):
        print("*"*square_size, end="")

def draw_triangle_line(triangle_size,i):
    print(" " * (triangle_size - i - 1) + "*" * (2 * i + 1)+ " " * (triangle_size - i - 1),end="")


def draw_inverted_triangle_line(inverted_triangle_size,i):
    print(" " * i + "*" * (2 * (inverted_triangle_size - i ) - 1)+" " * i ,end="")

def draw_rectangle_line(width):
    print("*"*width, end="")

def draw_empty_rectangle_line(width):
    print(" "*width, end="")


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
#pull deneme

#yorumum