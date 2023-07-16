
input_text = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def square_line_drawer(size, line, height_offset):
    if line <= height_offset:
        print(" " * size, end= " ")
    else:
        print("*" * size, end= " ")

def triange_line_drawer(height, line, height_offset):
    width = height * 2 - 1
    if line <= height_offset:
        print(" " * width, end= " ")
    else:
        line = line - height_offset
        print(" " * (height - line) + "*" * ((line * 2) - 1) + " " * (height - line), end= " ")

def inverted_triangle_line_drawer(width, line, height_offset, max_height): # Cracked, fix it
    height = int((width + 1) / 2) # for V9, height = 5
    if line > max_height - height_offset: # line 1,2,3,4,5,6,7 diyelim height offset = 2
        print(" " * width, end = " ")
    else:
        print(" " * (line - 1) + "*" * ((width + 2) - (2 * line)) + " " * (line - 1), end = " ")

def rectangle_line_drawer(height, width, line, height_offset):
    if line <= height_offset:
        print(" " * width, end = " ")
    else:
        line = line - height_offset
        print("*" * width, end = " ")

def empty_rec_line_drawer(height, width, line, height_offset):
    if line <= height_offset:
        print(" " * width, end = " ")
    else:
        line = line - height_offset
        print(" " * width, end = " ")

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
    if starting_letter == "O":
        size = int(string[1: len(string)])
        return size  # Width
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

def width_finder(string_lst): # Hatalı
    total_width = 0
    lst = list(string_lst.split(","))
    for i in range(len(lst) - 1): # width coming from the space btw any two elements
        total_width += 1
    for i in range(lst.count("DL")): # Overcountingi engellemek için yazdım ama çalışmıyor
        total_width -= 1
    for i in range(lst.count("N")):
        total_width -= 1
    for i in range(lst.count("B")):
        total_width -= 1
    for shape in lst: # width coming from the elements' own widths
        if shape[0] == "E" or shape[0] == "R":
            width = obj_width_finder(shape)
            total_width += width

        if shape[0] == "V" or shape[0] == "S" or shape[0] == "O":
            width = obj_width_finder(shape)
            total_width += width

        if shape[0] == "T":
            height = obj_height_finder(shape)
            width = int((2 * height) - 1)
            total_width += width
    return total_width

def max_width_finder():
    max_width = 0
    for i in my_diction.values(): # my_dict.. liste gibi bir şey ama tam değil onun elemanları string, widthlerini bul ekle
        if width_finder(i) > max_width:
            max_width = width_finder(i)
    return max_width

def shape_drawer(string):
    starting_letter = string[0]
    if starting_letter == "T":
        triange_line_drawer(obj_height_finder(string), line, height_offset)
    if starting_letter == "V":
        inverted_triangle_line_drawer(obj_width_finder(string), line, height_offset, max_height)
    if starting_letter == "S":
        square_line_drawer(obj_height_finder(string), line, height_offset)
    if starting_letter == "E":
        empty_rec_line_drawer(obj_height_finder(string),obj_width_finder(string), line, height_offset)
    if starting_letter == "R":
        rectangle_line_drawer(obj_height_finder(string),obj_width_finder(string), line, height_offset)
    if starting_letter == "O":
        empty_rec_line_drawer(obj_height_finder(string), obj_width_finder(string), line, height_offset)
    if string == "B":
        print()

def empty_line_finder(max_height, obj_height):
    empty_line = max_height - obj_height
    return empty_line

#input_text = "T4,DL,R2x3,DL,O2,N,N,O1,V5,O2,T3"
my_list = input_text.split(",N,")

my_diction = {}
for i in range(1, len(my_list) + 1):
    my_diction["element_list_string{}".format(i)] = my_list[i - 1]

rows_max_height_list = []
for values_str in my_diction.values():
    rows_max_height_list.append(max_height_finder(values_str))

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
    max_height = max_height_finder(values_str)
    if max_height == 0: # Max_height = 0 demek sadece "B" var demek kaç taneyse print() bas
        b_counter = values_lst.count("B") # Burada bir sıkıntı seziyorum sanki dönmek lazım dkdkkd
        for i in range(b_counter):
            print()
    max_width = max_width_finder()
    row_s_width = width_finder(values_str)
    width_offset = int((max_width - row_s_width) / 2)
    row_s_height = max_height_finder(values_str)

    for line in range(1, max_height + 1):
        print(" " * width_offset, end= "")
        for value in values_lst:
            height_offset = row_s_height - obj_height_finder(value)
            shape_drawer(value)
        print()


print("-" * max_width_finder())


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
