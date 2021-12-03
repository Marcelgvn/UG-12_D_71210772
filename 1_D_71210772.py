a = int(input("Masukan awal deret: "))
b = int(input("Masukan akhir deret: "))

if (a + 1) % 2 == 0:
    for i in range(a + 1, b, 2):
        if i % 3 == 0 or i % 7 == 0: continue
        print(i, end=" ")
else:
    for i in range(a, b, 2):
        if i % 3 == 0 or i % 7 == 0: continue
        print(i, end=" ")