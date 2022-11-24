print ("===================Pilihan Menu=====================")
print ("Tambah")
print ("Kurang")
print ("Kali")
print ("Bagi")

#variabel
a = int(input("Bilangan 1 : "))
b = int(input("Bilangan 2 : "))
pilihan = int(input("Pilihan : "))

#formula
if pilihan == 1 :
    nilai = a+b
elif  pilihan == 2 :
    nilai = a-b
elif pilihan == 3 :
    nilai = a*b
elif pilihan == 4 :
     nilai = float(a/b)
    
print("Hasil : ", nilai)