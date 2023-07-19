


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

def find_row_width(row):
    total_width = 0
    offset_count = 0
    for k in range(len(row)):
        letter = str(row[k][0])
        if letter == "T":
            width = (int(row[k][1: len(row[k])]) * 2) - 1
            total_width = width + total_width
        elif letter == "V":
            width = int(row[k][1: len(row[k])])
            total_width = width + total_width
        elif letter == "S":
            size = int(row[k][1: len(row[k])])
            total_width = size + total_width
        elif letter == "R":
            x_index = row[k].index("x")
            width = int(row[k][x_index + 1: len(row[k])])
            total_width = width + total_width
        elif letter == "E":
            x_index = row[k].index("x")
            width = int(row[k][x_index + 1: len(row[k])])
            total_width = width + total_width
        elif letter == "B":
            continue
        elif letter == "O":
            offset_count += 1
    total_width = total_width + len(row) - 1
    return total_width

def find_max_width():
    for j in range(len(row_list)):
        max_width=0
        width=find_row_width(row_list[j]) #find_row_with tuple göndermişti
        if width>max_width:
            max_width=width+max_width
    return max_width

def find_max_height(row):
    max_height = 0
    offset_count = 0
    for k in range(len(row)):
        letter = str(row[k][0])
        if letter == "T":
            height = int(row[k][1: len(row[k])])  # triangle fonksiyonu ilk elemanı width, ikincisi height olan bir tuple gönderdi
            if height > max_height:
                max_height = height
        elif letter == "V":
            height = int((int(row[k][1: len(row[k])]) + 1) / 2)
            if height > max_height:
                max_height = height
        elif letter == "S":
            height = int(row[k][1: len(row[k])])
            if height > max_height:
                max_height = height
        elif letter == "R":
            x_index = row[k].index("x")
            height = int(row[k][1: x_index])
            if height > max_height:
                max_height = height
        elif letter == "E":
            x_index = row[k].index("x")
            height = int(row[k][1: x_index])
            if height > max_height:
                max_height = height
        elif letter == "B":
            max_height=-1
        elif letter == "O":
            offset_count += 1
    return max_height


def draw_dashed_line(max_height):
    print("-"*max_height)

def draw_blank_line():
    print()

def draw_square_line(row,k,max_height,i):
    size = int(row[k][1: len(row[k])])
    offset=max_height-size
    if i<offset:
        print(" "*(size+1),end="")
    else:
        print("*" *size+" ",end="")

def draw_triangle_line(row,k,max_height, i):
    height = int(row[k][1: len(row[k])])
    width = (int(row[k][1: len(row[k])]) * 2) - 1
    offset = max_height - height
    if i < offset:
        print(" " * (width+1), end="")
    else:
        print(" " * (height - (i-offset) - 1) + "*" * (2 * (i-offset) + 1) + " " * (height - (i-offset)), end="")

def draw_inverted_triangle_line(row,k,max_height, i):
    height = int((int(row[k][1: len(row[k])]) + 1) / 2)
    width = int(row[k][1: len(row[k])])
    if i<height:
        print(" " * i + "*" * (width-2*i) + " " * (i+1), end="")
    else:
        print(" "*(width+1),end="")

def draw_rectangle_line(row,k,max_height,i):
    x_index = row[k].index("x")
    height = int(row[k][1: x_index])
    width = int(row[k][x_index + 1: len(row[k])])
    offset=max_height-height
    if i<offset:
        print(" "*(width+1),end="")
    else:
        print("*" * width+" ",end="")

def draw_empty_rectangle_line(row,k,max_height,i):
    x_index = row[k].index("x")
    height = int(row[k][1: x_index])
    width = int(row[k][x_index + 1: len(row[k])])
    offset = max_height - height
    if i < offset:
        print(" " * (width+1), end="")
    else:
        print(" " * (width+1), end="")

for j in range(len(row_list)):
    row=row_list[j]
    dashed_line_count=count_then_erase_dashed_line(row)
    max_width=find_max_width()
    max_height=find_max_height(row)
    row_width=find_row_width(row)
    offset=int((max_width-row_width)/2)
    if dashed_line_count >= 1:
        print("-" * max_width)
        dashed_line_count = 0
    if max_height==-1:
        print()
    for i in range(max_height):
        print(" " * offset, end="")
        for k in range(len(row)):
            letter = str(row[k][0])
            if letter == "T":
                draw_triangle_line(row,k,max_height,i)
            elif letter == "V":
                draw_inverted_triangle_line(row,k,max_height,i)
            elif letter == "S":
                draw_square_line(row,k,max_height,i)
            elif letter == "R":
                draw_rectangle_line(row,k,max_height,i)
            elif letter == "E":
                draw_empty_rectangle_line(row,k,max_height,i)
            elif letter == "O":
                print("offset")


        print()

print("-" * max_width)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
