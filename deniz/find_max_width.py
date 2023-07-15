input_text=input()
row_list= input_text.split(",N")
for _ in range(row_list.count("")):
    row_list.remove("")

number_of_rows=len(row_list)

row_dictionary={}

for i in range(number_of_rows):
    new_row=row_list[i].split(",")
    print(new_row)
    for _ in range(new_row.count("")):  ##art arda gelen iki N den dolayı artan , işimi uzattı daha düzgün bir çözüm bulmaya çalışacağım
        new_row.remove("")
    print(row_list)
    row_dictionary.update({i+1: new_row})

print("dictionary:",row_dictionary)

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
            width = width + int(row[k][1])
        elif letter=="T":
            width=width+ (int(row[k][1])*2)-1
        elif letter == "R" or letter == "E":
            width = width + int(row[k][3])
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

print(find_max_width())



