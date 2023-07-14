
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

#DL ve B yi sildikten sonra yapmalıyım bu hesabı yoksa eleman sayısının bir eksiğini ekle dediğimde onları da ekliyorum
def find_row_width(k, row):
    width = len(row) - 1  # her iki şekil arasındaki boşluk sayısı
    for k in range(len(row)):
        letter = str(row[k][0])
        if letter == "T" or letter == "V" or letter == "S" or letter == "O":
            width = width + int(row[k][1])
        elif letter == "R" or letter == "E":
            width = width + int(row[k][3])
        else:
            continue
    print("row length of", k, "is", width)

for _ in range(row_number):
    row= row_dictionary[_+1]
   #print(row)
    for k in range(len(row)):
        print(find_row_width(k,row))

    # Hello comment line deneme
    print("deneme")

    #deniz push deneme




