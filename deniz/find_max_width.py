input_text = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
temporary_list=input_text.split(",N,")
number_of_rows=len(temporary_list)
row_list=[]

for i in range(number_of_rows):
    new_row=temporary_list[i].split(",")
    for _ in range (new_row.count("N")):
        new_row.remove("N")
    if new_row!= []:
        row_list.append(new_row)

def count_then_erase_dashed_line(row):
    for k in range(len(row)):
        letter = str(row[k][0])
        dashed_line_count=0
        if letter == "D":
            dashed_line_count=1
            for _ in range(row.count("DL")):
                row.remove("DL")
            break
    return dashed_line_count


def find_element_width(element):
    width=0
    offset_count=0
    letter = str(element[0])
    if letter == "T":
        width = (int(element[1: len(element)]) * 2) - 1
    elif letter == "V":
        width = int(element[1: len(element)])
    elif letter == "S":
        width = int(element[1: len(element)])
    elif letter == "R":
        x_index = element.index("x")
        width = int(element[x_index + 1: len(element)])
    elif letter == "E":
        x_index = element.index("x")
        width = int(element[x_index + 1: len(element)])
    elif letter == "B":
        width=0
    elif letter == "O":
        offset_count += 1
        width=int(element[1: len(element)])
    return width

def find_row_width(row):
    total_width = len(row)-1
    for k in range(len(row)):
        element=row[k]
        total_width = find_element_width(element) + total_width
    return total_width

def find_max_width():
    max_width = 0
    for j in range(len(row_list)):
        width=find_row_width(row_list[j]) #find_row_with tuple göndermişti
        if width>max_width:
            max_width=width
    return max_width
def find_element_height(element):
    offset_count=0
    letter=str(element[0])
    if letter == "T":
        height = int(element[1: len(element)])  # triangle fonksiyonu ilk elemanı width, ikincisi height olan bir tuple gönderdi
    elif letter == "V":
        height = int((int(element[1: len(element)]) + 1) / 2)
    elif letter == "S":
        height = int(element[1: len(element)])
    elif letter == "R":
        x_index = element.index("x")
        height = int(element[1: x_index])
    elif letter == "E":
        x_index = element.index("x")
        height = int(element[1: x_index])
    elif letter == "B":
        height=0
    elif letter == "O":
        offset_count += 1
        height=0
    return height

def find_max_height(row):
    max_height = 0
    for k in range(len(row)):
        element=row[k]
        if find_element_height(element)>max_height:
            max_height=find_element_height(element)
    return max_height


def draw_dashed_line():
    print("-"*max_height)

def draw_blank_line():
    print()

def draw_square_line(element,line):
    size=find_element_width(element)
    offset=max_height-size
    if line<offset:
        print(" "*(size+1),end="")
    else:
        print("*" *size+" ",end="")

def draw_triangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    offset = max_height - height
    if line < offset:
        print(" " * (width+1), end="")
    else:
        print(" " * (height - (line-offset) - 1) + "*" * (2 * (line-offset) + 1) + " " * (height - (line-offset)), end="")

def draw_inverted_triangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    if line<height:
        print(" " * line + "*" * (width-2*line) + " " * (line+1), end="")
    else:
        print(" "*(width+1),end="")

def draw_rectangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    offset=max_height-height
    if line<offset:
        print(" "*(width+1),end="")
    else:
        print("*" * width+" ",end="")

def draw_empty_rectangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    offset = max_height - height
    if line < offset:
        print(" " * (width+1), end="")
    else:
        print(" " * (width+1), end="")
def draw_offset(element,line):
    width=find_element_width(element)
    print(" "*width,end="")

for j in range(len(row_list)):
    row=row_list[j]
    dashed_line_count=count_then_erase_dashed_line(row)
    max_width=find_max_width()
    max_height=find_max_height(row)
    row_width=find_row_width(row)
    offset=int((max_width-row_width)/2)
    if dashed_line_count >= 1:
        print("-" * max_width)
    if row_width==-1: #Blank line geldiğince row_width -1 olarak dönüyor
        print()
    for line in range(max_height):
        print(" " * offset, end="")
        for k in range(len(row)):
            element=row[k]
            letter = str(element[0])
            if letter == "T":
                draw_triangle_line(element,line)
            elif letter == "V":
                draw_inverted_triangle_line(element,line)
            elif letter == "S":
                draw_square_line(element,line)
            elif letter == "R":
                draw_rectangle_line(element,line)
            elif letter == "E":
                draw_empty_rectangle_line(element,line)
            elif letter == "O":
                draw_offset(element,line)


        print()

print("-" * max_width)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
