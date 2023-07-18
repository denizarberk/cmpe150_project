


input_text = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    #BU KISIMDA INPUTU ALIP ÖNCE ELEMANLARI ROWLAR OLAN BİR LİSTEYE ATADIM
row_list= input_text.split(",N")
for _ in range(row_list.count("")):
    row_list.remove("")

    #BU KISIMDA O LİSTEYİ DEĞİŞTİRİP ELEMANLARI ROWLARIN LİSTESİ OLAN VE LİSTELERİN EMANLARI DA ÇİZMEMİZ GEREKEN KOMUTLAR OLAN "row_dictionary" YE ATADIM
number_of_rows=len(row_list)
row_dictionary={}

for i in range(number_of_rows):
    new_row=row_list[i].split(",")
    for _ in range(new_row.count("")):  ##art arda gelen iki N den dolayı artan , işimi uzattı daha düzgün bir çözüm bulmaya çalışacağım
        new_row.remove("")
    row_dictionary.update({i+1: new_row})

print("dictionary:",row_dictionary)

    #BU KISIMDA find_row_width ve find_max_width FONKSİYONLARINI TANIMLADIM
#offset(O1,02..) girdisini tam anlamadığım için hata olabilir, onun dışında hata yok fonksiyonda
def find_row_width(row):
    width = len(row) - 1
    if "Dl" or "B" in row:  #DL ve B genişliğe ekleyor ama üstte onları da şekiller arasındaki boğluk olarak saydığımdan burada o fazladan saymayı çıkartıyorum
        dashed_line_count= row.count("DL")
        blank_count= row.count("B")
        width=width-dashed_line_count-blank_count
    for k in range(len(row)):
        letter = str(row[k][0])
        if letter == "V" or letter == "S" or letter == "O":
            width = width + int(row[k][1: len(row[k])])
        elif letter=="T":
            width=width+ (int(row[k][1: len(row[k])])*2)-1
        elif letter == "R" or letter == "E":
            x_index = row[k].index("x")
            width = width + int(row[k][x_index+1: len(row[k])])
        else:
            continue
    return width

def find_max_width():
    row_number = len(row_list)
    max_width=0
    for j in range(row_number):
        row = row_dictionary[j + 1]
        row_width= find_row_width(row)
        if row_width>max_width:
            max_width=row_width
    return max_width

def find_object_height(row,k):
    letter = str(row[k][0])
    if letter == "V" :
        height = int((int(row[k][1: len(row[k])])+1)/2)
    elif letter=="T" or letter == "S":
        height=int(row[k][1: len(row[k])])
    elif letter == "R" or letter == "E":
        x_index = row[k].index("x")
        height=int(row[k][1: x_index])
    else:
        height=0
    return height


def find_max_height_in_a_row(row):
    max_height=0
    for k in range(len(row)):
        height= find_object_height(row,k)
        if height>max_height:
            max_height=height
    return max_height
print(find_max_height_in_a_row(row_dictionary[2]))
#print(find_max_height_in_a_row(row_dictionary[1]))


print(find_max_width())

    #BU KISIMDA ŞEKİL LİNE ÇİZME FONKSİYONLARINI TANIMLIYORUM
def draw_triangle_line(height,i):
    print(" " * (height - i - 1) + "*" * (2 * i + 1)+ " " * (height - i - 1),end="")

def draw_inverted_triangle_line(width, i):
    print(" " * i + "*" * (width-(2*i)) + " " * i, end="")

def draw_square_line(square_size):
    print("*" * square_size, end="")

def draw_rectangle_line(height,width):
    print("*"*width,end="")
def draw_empty_rectangle_line(height,width):
    print("*"*width,end="")

def draw_dashed_line():
    max_widh=find_max_width()
    print("-"*max_widh)

def blank_line():
    print()


def startswith(row):
    for k in range(len(row)):
        letter = str(row[k][0])
        if letter=="T":
            height=int(row[k][1: len(row[k])])
            draw_triangle_line(height,i)
        elif letter=="V":
            width=int(row[k][1: len(row[k])])
            draw_inverted_triangle_line(width,i)
        elif letter=="S":
            size=int(row[k][1: len(row[k])])
            draw_square_line(size)
        elif letter=="R":
            x_index= row[k].index("x")
            height=int(row[k][1: x_index])
            width=int(row[k][x_index+1: len(row)])
            draw_rectangle_line(height,width)
        elif letter=="E":
            x_index= row[k].index("x")
            height=int(row[k][1: x_index])
            width=int(row[k][x_index+1: len(row)])
            draw_empty_rectangle_line(height,width)
        elif letter=="D":
            draw_dashed_line()
        elif letter=="B":
            blank_line()
        elif letter=="O":
            print("Offset")

#şekilleri çizmeye daha başlamadım

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
