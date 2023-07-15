input_text=input()
row_list= input_text.split(",N")

for _ in range(row_list.count("")):
    row_list.remove("")

row_number=len(row_list)
print(row_list)

row_dictionary={}

for i in range(row_number):
    new_row=row_list[i].split(",")
    if "" in new_row:    ##art arda gelen iki N den dolayı artan , işimi uzattı daha düzgün bir çözüm bulmaya çalışacağım
        new_row.remove("")
    row_dictionary.update({i+1: new_row})

print("dictionary:",row_dictionary)

def draw_triangle_line(height,i):
    print(" " * (height - i - 1) + "*" * (2 * i + 1)+ " " * (height - i - 1),end="")

def draw_inverted_triangle_line(width, i):
    print(" " * i + "*" * (width-(2*i)) + " " * i, end="")

def draw_square_line(square_size):
    print("*" * square_size, end="")
def startswith(k,i):
    if letter=="T":
        #size=row[k][1]
       # print("Triangle")
        draw_triangle_line(size,i)
    elif letter=="V":
        #size=row[k][1]
        draw_inverted_triangle_line(size,i)
       # print("Inverted Triangle")
    elif letter=="S":
        #size=row[k][1]
        draw_square_line(size)
        #print("Square")
    elif letter=="R":
        height=row[k][1]
        width=row[k][3]
        print("Rectangle")
    elif letter=="E":
        height=row[k][1]
        width=row[k][3]
        print("Empty Rectangular Area")
    elif letter=="D":
        print("Dashed Line")
    elif letter=="B":
        print("Blank Line")
    elif letter=="O":
        print("Offset")

#şu anda başarısız bir kısım

for _ in range(row_number):
    row= row_dictionary[_+1]
   #print(row)
    for k in range(len(row)):
        i=0
        letter=row[k][0]
        size=int(row[k][1])
        for i in range(size):
            for b in range(len((row))):
                startswith(k,i)
                print(" ", end="")
            print()
    print()
