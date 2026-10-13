def luas_persegi_panjang (p, l):
    return p * l

def luas_segitiga (a, t):
    return 0.5 * a * t

def jumlah_n (n) :
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial (n) :
    hasil = 1
    for i in range(2, n + 1):
            hasil *= i
    return hasil

def tampilkan_menu () :
    print ("1. Luas Persegi Panjang")
    print ("2. Luas Segitiga")
    print ("3. Jumlah 1 sampai n")
    print ("4. Faktorial")

tampilkan_menu ()
pilihan = input ("pilihan: ")

if pilihan == "1" :
    p = float (input ("panjang: "))
    l = float (input ("lebar: "))
    print ("luas persegi panjang:", luas_persegi_panjang (p, l))
elif pilihan == "2" :
    a = float (input ("alas: "))
    t = float (input ("tinggi: "))
    print ("luas segitiga:", luas_segitiga (a, t))
elif pilihan == "3" :
    n = int (input ("n: "))
    if n >= 0:
        print ("jumlah =", jumlah_n (n))
    else:
        print ("n harus non-negatif")
elif pilihan == "4" :
    n = int (input ("n: "))
    if n >= 0:
        print ("faktorial:", faktorial (n))
    else:
        print ("n harus non-negatif")
                          