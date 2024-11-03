print("1.Sayıları Topla")
print("2.Sayıları Çıkar")
print("3.Sayıları Çarp")
print("4.Sayıları Böl")

while True:
    sayi1 = int(input("1.Sayıyı girin:"))
    sayi2 = int(input("2.Sayıyı girin:"))
    secenek = int(input("Yapmak istediğiniz işlemin numarasını girin:"))

    if secenek == 1:
        print(sayi1 + sayi2)
        break
        
    elif secenek == 2:
        print(sayi1 - sayi2)
        break
        
    elif secenek == 3:
        print(sayi1 * sayi2)
        break
        
    elif secenek == 4:
        if sayi2 == 0:
            print("0'a bölünemez")
        print(sayi1 / sayi2)
        break
