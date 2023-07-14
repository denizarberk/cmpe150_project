input_text=input()
row_list= input_text.split(",N")

if "" in row_list:  #art arda iki tane "N" olduğunda bu gerekli oluyor"
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