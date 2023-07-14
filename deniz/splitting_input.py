#bu sayfa girilen texti alıp rowlara ayırıp bu rowları row_dictonary dictionarysine atıyor

input_text=input()
row_list= input_text.split(",N")

for _ in range(row_list.count("")):
    row_list.remove("")

number_of_rows=len(row_list)
print(row_list)

row_dictionary={}

for i in range(number_of_rows):
    new_row=row_list[i].split(",")
    if "" in new_row:    ##art arda gelen iki N den dolayı artan , işimi uzattı daha düzgün bir çözüm bulmaya çalışacağım
        new_row.remove("")
    row_dictionary.update({i+1: new_row})

print("dictionary:",row_dictionary)