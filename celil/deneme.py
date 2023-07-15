

def triangle_line_drawer(height, max_height):
    width = 2 * height + 1
    blank_counter = int((width - 1)/ 2)
    star_counter = 1
    if max_height > height:
        for i in range(max_height - height):
            print(" " * height)
    for i in range(height):
        print(" " * blank_counter + "*" * star_counter + " " * blank_counter, end = " ")
        blank_counter -= 1
        star_counter += 2

def square_line_drawer(size, max_height):
    if max_height > size:
        for i in range(max_height - size):
            print(" " * size)
    for i in range(size):
        print("*" * size, end = " ")


max_height = 4
for i in range(max_height):
    triangle_line_drawer(4, i)
    square_line_drawer(3, i)
    print()


"""
###*### ###
##***## ***
#*****# ***
******* ***
"""

def size_finder(string):  # "DL", "N" veya "B" alırsa -1 dönecek
    starting_letter = string[0]
    if starting_letter == "T":
        size = int(string[1: len(string)])
        return size # Height
    if starting_letter == "V":
        size = int(string[1: len(string)])
        return size # Width
    if starting_letter == "S":
        size = int(string[1: len(string)])
        return size # Both height and width, they are equal
    if starting_letter == "E":
        x_index = string.index("x")
        height = int(string[1: x_index])
        width = int(string[(x_index + 1): len(string)])
        return height, width
    if starting_letter == "R":
        x_index = string.index("x")
        height = int(string[1: x_index])
        width = int(string[(x_index + 1): len(string)])
        return height, width
    else:
        return -1

def square_drawer(size):
    for i in range(size):
        for j in range(size):
            print("*", end = "")
        print()

def triangle_drawer(height):
    star_counter = 1
    blank_counter = height - 1
    for i in range(height):
        print(" " * blank_counter + "*" * star_counter + " " * blank_counter)
        star_counter += 2
        blank_counter -= 1

def inverted_triangle_drawer(width):
    height = int((width + 1) / 2)
    star_counter = (height * 2) - 1
    blank_counter = 0
    for i in range(height):
        print(" " * blank_counter + "*" * star_counter + " " * blank_counter)
        star_counter -= 2
        blank_counter += 1

def rectangle_drawer(height, width):
    for i in range(height):
        print("*" * width)

def empty_rectengular_area(height, width):
    for i in range(height):
        print(" " * width)

def next_row():
    print()

def dashed_line_drawer(max_width):
    print("-" * max_width)

def height_finder(string_lst):
    lst = list(string_lst.split(","))
    height = 0
    for shapes in lst:
        if shapes[0] == "T" and size_finder(shapes) > height:
            height = size_finder(shapes)
        if shapes[0] == "V":
            shape_width = size_finder(shapes)
            shape_height = int((shape_width + 1) /2)
            if shape_height > height:
                height = shape_height
        if shapes[0] == "S" and size_finder(shapes) > height:
            height = size_finder(shapes)
        if shapes[0] == "E" and size_finder(shapes)[0] > height:
            height = size_finder(shapes)[0]
        if shapes[0] == "R" and size_finder(shapes)[0] > height:
            height = size_finder(shapes)[0]
    print(height)

def width_finder(string_lst): # "DL", "N", ve "B" temizlenmiş bir liste gerekli input olarak
    total_width = 0
    lst = list(string_lst.split(","))
    for i in range(len(lst) - 1): # width coming from the space btw any two elements
        total_width += 1
    for i in lst: # width coming from the elements' widths
        if i[0] == "E" or i[0] == "R":
            width = size_finder(i)[1]
            total_width += width

        if i[0] == "V" or i[0] == "S":
            width = size_finder(i)
            total_width += width

        if i[0] == "T":
            height = size_finder(i)
            width = int((2 * height) - 1)
            total_width += width
    return total_width

def max_width_finder():
    max_width = 0
    for i in my_diction.values():
        if width_finder(i) > max_width:
            max_width = width_finder(i)
    return max_width

def shape_drawer(string):
    starting_letter = string[0]
    if starting_letter == "T":
        triangle_drawer(size_finder(string))
    if starting_letter == "V":
        inverted_triangle_drawer(size_finder(string))
    if starting_letter == "S":
        square_drawer(size_finder(string))
    if starting_letter == "E":
        empty_rectengular_area(size_finder(string)[0],size_finder(string)[1])
    if starting_letter == "R":
        rectangle_drawer(size_finder(string)[0],size_finder(string)[1])
    if string == "B":
        next_row()

input_text = "T4,S3"
my_list = input_text.split(",N,")

my_diction = {}
for i in range(1, len(my_list) + 1):
    my_diction["element_list_string{}".format(i)] = my_list[i - 1]

#print(my_diction)

for values_str in my_diction.values():
    values_lst = values_str.split(",")

    if "DL" in values_lst:
        dashed_line_drawer(max_width_finder())
        dl_counter = values_lst.count("DL")
        for i in range(dl_counter):
            values_lst.remove("DL")
    if "N" in values_lst:
        n_counter = values_lst.count("N")
        for i in range(n_counter):
            values_lst.remove("N")
"""
    for value in values_lst:
        shape_drawer(value)"""


#print("-" * max_width_finder())


