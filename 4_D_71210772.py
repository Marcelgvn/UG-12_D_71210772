a = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
sen = ("kelas ke-1 Algorima Graf","kelas ke-3 Sistem Operasi","kelas ke-4 PAK")
sel = ("kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indonesia","kelas ke-6 PKN")
rab = ("kelas ke-2 Sistem Basis Data","kelas ke-4 Praktikum Sistem Basis Data")
kam = ("kelas ke-1 IMK","kelas ke-3 LogMat","kelas ke-4 Praktekkom")

if a == "senin" :
    for i in range(len(sen)):
        print(sen[i])
elif a == "selasa" :
    for i in range(len(sel)):
        print(sel[i])
elif a == "rabu" :
    for i in range(len(rab)):
        print(rab[i])
elif a == "kamis" :
    for i in range(len(kam)):
        print(kam[i])
elif a == "jumat" :
    print("Hari Jumat Anda tidak ada kelas")