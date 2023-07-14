input_text=input()
row_list= input_text.split(",N")

if "" in row_list:  #art arda iki tane "N" olduğunda bu gerekli oluyor"
    row_list.remove("") #eğer art arda üç tane "N" gelirse diğerini silmiyor

row_number=len(row_list)
print(row_list)

row_dictionary={}

for i in range(row_number):
    new_row=row_list[i].split(",")
    if "" in new_row:    ##art arda gelen iki N den dolayı artan , işimi uzattı daha düzgün bir çözüm bulmaya çalışacağım
        new_row.remove("")
    row_dictionary.update({i+1: new_row})

print("dictionary:",row_dictionary)

def draw_triangle_line(triangle_size,i):
    print(" " * (triangle_size - i - 1) + "*" * (2 * i + 1)+ " " * (triangle_size - i - 1),end="")

def draw_inverted_triangle_line(inverted_triangle_size, i):
    print(" " * i + "*" * (2 * (inverted_triangle_size - i) - 1) + " " * i, end="")

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
