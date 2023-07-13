input_text=input()
row_list= input_text.split(",N")

if "" in row_list:  #art arda iki tane "N" olduğunda bu gerekli oluyor"
    row_list.remove("")

row_number=len(row_list)
print(row_list)

row_1= row_list[0].split(",")
if "" in row_1:
    row_1.remove("")
print(row_1)


row_2=row_list[1].split(",")
if "" in row_2:
    row_2.remove("")
print(row_2)


#art arda gelen iki N den dolayı artan , işimi uzattı daha düzgün bir çözüm bulmaya çalışacağım

#bir de kaç tane row olacağını bilmiyorum böyle tek tek yapmadan bi dictionary ye atmanın yolunu bulmalıyım