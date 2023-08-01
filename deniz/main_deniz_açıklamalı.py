input_text = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    #bu kısımda verilen inputu N gördüğüm yerden ayırıp temporary_list adında listeye atıyorum
temporary_list=input_text.split(",N,")
number_of_rows=len(temporary_list) #kaç tane row olduğunun sayısı olmuş oluyor N gördüğüm yerden ayırdığım için
row_list=[]
    #burada her row u , görüğüm yerden ayrıp new_row listesine atıyorum
for i in range(number_of_rows):
    new_row=temporary_list[i].split(",")
    for _ in range (new_row.count("N")): #art arda N geldiği zaman sorun oluyordu, bir tane N gelmesi yeni satıra geçmek için yeterli,fazlalıkları sildim
        new_row.remove("N")
    if new_row != []: #burada da her new_row u genel row_list adındaki listede topladım
        row_list.append(new_row)
    #yani genelde inputu row_list adında içerisinde row listelerinin bulunduğu bir listede topladım
    # her row da içinde komutların(ileride kullanacağım üzere elementlerin) listesi

    #bu fonksiyon almış olduğu row da eğer DL varsa o row için dashed_line_count ı 1 yapıyor ardıından da o satırdaki bütün DL elementlerini siliyor
    #en son çalıştırdığım for döngüsünde bir row geldiğinde ilk önce bunu çalıştırdım ki row çizilmeye başlamadan DL çizip çizmeyeceğimi bileyim
def count_then_erase_dashed_line(row):
    for element in row:
        letter= str(element[0])
        dashed_line_count=0
        if letter == "D":
            dashed_line_count=1
            for _ in range(row.count("DL")):
                row.remove("DL")
            break
    return dashed_line_count

#bu fonksiyon eleman alıp onların genişliğini veriyor
def find_element_width(element):
    width=0
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
        width=int(element[1: len(element)])
    return width

#bu fonksiyon row alıp row içindeki her eleman için bir üstteki fonksiyonu çağırıyor sonra da row un toplan genişliğini hesaplıyor
def find_row_width(row):
    total_width = len(row)-1
    for element in row:
        total_width = find_element_width(element) + total_width
    return total_width
#bu fonksiyon girdideki bütün row lardan en büyük genişliğe sahip olanın genişliğini hesapluyor ki DL komutlarını bu uzunluğa göre çizeyim
def find_max_width():
    max_width = 0
    for row in row_list:
        width=find_row_width(row)
        if width>max_width:
            max_width=width
    return max_width
#bu fonksiyon eleman alıp onların yüklsekliğini veriyor
def find_element_height(element):
    letter=str(element[0])
    if letter == "T":
        height = int(element[1: len(element)])
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
        height=0
    return height
#bu fonksiyon row içerisindeki en yüksek elemanı bulup onun yüksekliğini döndürüyor(şekilleri aşağı yukarı hizzalamak için gerekli)
def find_max_height(row):
    max_height = 0
    for element in row:
        if find_element_height(element)>max_height:
            max_height=find_element_height(element)
    return max_height

#bundan sonraki 8 fonksiyon her bir şeklin tek tek satırlarını yazdırıyor
def draw_dashed_line():
    print("-"*max_height)

def draw_blank_line():
    print()

def draw_square_line(element,line):
    size=find_element_width(element)
    offset=max_height-size #bu offset komutu şekli max_height a göre row içinde aşağıya dayamak için
    if line<offset:
        print(" "*size,end="")
    else:
        print("*" *size,end="")

def draw_triangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    offset = max_height - height
    if line < offset:
        print(" " * width, end="")
    else:
        print(" " * (height - (line-offset) - 1) + "*" * (2 * (line-offset) + 1) + " " * (height - (line-offset)-1), end="")

def draw_inverted_triangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    if line<height:
        print(" " * line + "*" * (width-2*line) + " " * line, end="")
    else:
        print(" "*width, end="")

def draw_rectangle_line(element,line):
    height = find_element_height(element)
    width = find_element_width(element)
    offset=max_height-height
    if line<offset:
        print(" "* width, end="")
    else:
        print("*" * width, end="")

def draw_empty_rectangle_line(element,line):
    width = find_element_width(element)
    print(" " * width, end="")

def draw_offset(element,line):
    width=find_element_width(element)
    print(" "*width,end="")


#programı asıl çalıştıran kısım burası

for row in row_list: #her rowda sırayla geziniyor
    dashed_line_count=count_then_erase_dashed_line(row)
    max_width=find_max_width()
    max_height=find_max_height(row)
    row_width=find_row_width(row)
    row_offset=int((max_width-row_width)/2)
    if dashed_line_count >= 1:
        print("-" * max_width)
    if row_width==-1: #Blank line geldiğince row_width -1 olarak dönüyor o yüzden print() ile blank line bıraktırdım
        print()
    for line in range(max_height):
        print(" " * row_offset, end="")
        for element in row:
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
            print(" ",end="")

        print()

print("-" * max_width)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE