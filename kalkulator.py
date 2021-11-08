def Penjumlahan ():
    print ("Penjumlahan")
    a = float(input("Masukkan bilangan pertama:"))
    b = float(input("Masukkan bilangan kedua:"))
    penjumlahan = a + b
    print("Hasil",a, "+", b, "=", penjumlahan)
    print (" ")
    
def Pengurangan():
    print ("Pengurangan")
    a = float(input("Masukkan bilangan pertama:"))
    b = float(input("Masukkan bilangan kedua:"))
    pengurangan = a - b
    print("Hasil",a, "-", b, "=", pengurangan)
    print (" ")
    
def Perkalian():
    print ("Perkalian")
    a = float(input("Masukkan bilangan pertama:"))
    b = float(input("Masukkan bilangan kedua:"))
    perkalian = a * b
    print("Hasil",a, "x", b, "=", perkalian)
    print (" ")
    
def Pembagian():
    print ("Pembagian")
    a = float(input("Masukkan bilangan pertama:"))
    b = float(input("Masukkan bilangan kedua:"))
    pembagian = a / b
    print("Hasil",a, "/", b, "=", pembagian)
    print (" ")

def PenjumlahanPecahan ():
    print ("Penjumlahan Bilangan Pecahan")
    print ("Masukkan bilangan pecahan pertama:")
    a = float(input ())
    print ("-")
    b = float(input ())
    print ("Masukkan angka pecahan kedua:")
    c = float(input ())
    print ("-")
    d = float(input ())
    print ("Hasil : ",((a*d)+(b*c)))
    print ("         -")
    print ("        ",(b*d))
    print (" ")
   
def PenguranganPecahan ():
    print ("Pengurangan Bilangan Pecahan")
    print ("Masukkan bilangan pecahan pertama:")
    a = float(input ())
    print ("-")
    b = float(input ())
    print ("Masukkan angka pecahan kedua:")
    c = float(input ())
    print ("-")
    d = float(input ())
    print ("Hasil : ",((a*d)-(b*c)))
    print ("         -")
    print ("        ",(b*d))
    print (" ")
    
def PerkalianPecahan ():
    print ("Perkalian Bilangan Pecahan")
    print ("Masukkan bilangan pecahan pertama:")
    a = float(input ())
    print ("-")
    b = float(input ())
    print ("Masukkan angka pecahan kedua:")
    c = float(input ())
    print ("-")
    d = float(input ())
    print ("Hasil : ",(a*c))
    print ("         -")
    print ("        ",(b*d))
    print (" ")
    
def PembagianPecahan ():
    print ("Pembagian Bilangan Pecahan")
    print ("Masukkan bilangan pecahan pertama:")
    a = float(input ())
    print ("-")
    b = float(input ())
    print ("Masukkan angka pecahan kedua:")
    c = float(input ())
    print ("-")
    d = float(input ())
    print ("Hasil : ",(a*d))
    print ("         -")
    print ("        ",(b*c))
    print (" ")


while 1:    
    print("Kalkulator")
    print(" ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Penjumlahan Pecahan")
    print("6. Pengurangan Pecahan")
    print("7. Perkalian Pecahan")
    print("8. Pembagian Pecahan")


    pilihan = int(input("Pilihan: "))
    print ("")
    if pilihan==1:
        Penjumlahan ()
    elif pilihan==2:
        Pengurangan ()
    elif pilihan==3:
        Perkalian ()
    elif pilihan==4:
        Pembagian ()
    elif pilihan==5:
        PenjumlahanPecahan ()
    elif pilihan==6:
        PenguranganPecahan ()
    elif pilihan==7:
        PerkalianPecahan ()
    elif pilihan==8:
        PembagianPecahan ()
    else:
        print("Pilihan salah")
        print("")