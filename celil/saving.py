
#input_text = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


def obj_width_finder(string):  # "DL", "N" veya "B" alırsa -1 dönecek
    starting_letter = string[0]
    if starting_letter == "T":
        size = int(string[1: len(string)])
        width = (size * 2) - 1
        return width # Width
    if starting_letter == "V":
        size = int(string[1: len(string)])
        return size # Width
    if starting_letter == "S":
        size = int(string[1: len(string)])
        return size # Width
    if starting_letter == "E":
        x_index = string.index("x")
        width = int(string[(x_index + 1): len(string)])
        return width
    if starting_letter == "R":
        x_index = string.index("x")
        width = int(string[(x_index + 1): len(string)])
        return width
    else:
        return -1

def obj_height_finder(string):
    starting_letter = string[0]
    if starting_letter == "T":
        size = int(string[1: len(string)])
        return size  # Height
    if starting_letter == "V":
        size = int(string[1: len(string)])
        height = int((size + 1) / 2)
        return height  # Height
    if starting_letter == "S":
        size = int(string[1: len(string)])
        return size  # Height
    if starting_letter == "E":
        x_index = string.index("x")
        height = int(string[1: x_index])
        return height
    if starting_letter == "R":
        x_index = string.index("x")
        height = int(string[1: x_index])
        return height
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

def max_height_finder(string_lst):
    lst = list(string_lst.split(","))
    max_height = 0
    for shapes in lst:
        if shapes[0] == "T" and obj_height_finder(shapes) > max_height:
            max_height = obj_height_finder(shapes)
        if shapes[0] == "V":
            shape_width = obj_width_finder(shapes)
            shape_height = int((shape_width + 1) /2)
            if shape_height > max_height:
                max_height = shape_height
        if shapes[0] == "S" and obj_height_finder(shapes) > max_height:
            max_height = obj_height_finder(shapes)
        if shapes[0] == "E" and obj_height_finder(shapes) > max_height:
            max_height = obj_height_finder(shapes)
        if shapes[0] == "R" and obj_height_finder(shapes)> max_height:
            max_height = obj_height_finder(shapes)
    return max_height

def width_finder(string_lst): # "DL", "N", ve "B" temizlenmiş bir liste gerekli input olarak
    total_width = 0
    lst = list(string_lst.split(","))
    for i in range(len(lst) - 1): # width coming from the space btw any two elements
        total_width += 1
    for shape in lst: # width coming from the elements' widths
        if shape[0] == "E" or shape[0] == "R":
            width = obj_width_finder(shape)
            total_width += width

        if shape[0] == "V" or shape[0] == "S":
            width = obj_width_finder(shape)
            total_width += width

        if shape[0] == "T":
            height = obj_height_finder(shape)
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
        triangle_drawer(obj_height_finder(string))
    if starting_letter == "V":
        inverted_triangle_drawer(obj_width_finder(string))
    if starting_letter == "S":
        square_drawer(obj_height_finder(string))
    if starting_letter == "E":
        empty_rectengular_area(obj_height_finder(string),obj_width_finder(string))
    if starting_letter == "R":
        rectangle_drawer(obj_height_finder(string),obj_width_finder(string))
    if string == "B":
        next_row()

def empty_line_finder(max_height, obj_height):
    empty_line = max_height - obj_height
    return empty_line

input_text = "T4,S4,DL,DL,T5,N,E1x4,R3x5,E1x7,T3,E1x4"
my_list = input_text.split(",N,")

my_diction = {}
for i in range(1, len(my_list) + 1):
    my_diction["element_list_string{}".format(i)] = my_list[i - 1]

print(my_diction)

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

    print("Values lst:", values_lst)

    for value in values_lst:
        empty_line = empty_line_finder(max_height_finder(values_str), obj_height_finder(value))
        for line in range(empty_line):
            print(" " * obj_width_finder(value))
        shape_drawer(value)



print("-" * max_width_finder())


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
