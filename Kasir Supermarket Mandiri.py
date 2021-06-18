from produk import Product #mengimpor list product dari file produk.py
from checkout2 import CheckoutRegister2 #mengimpor metode pembayaran tanpa diskon dari file checkout2.py
from checkout import CheckoutRegister #mengimpor metode pembayaran dengan diskon dari file checkout.py
from time import gmtime, strftime 
import csv
import sys

current_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #memberi keterangan waktu pada struk
wishlist = []

datamember = []
with open('datamembership.csv') as csv_file: #digunakan untuk import file dari csv
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        datamember.append(row)
list_kode = []
for data in datamember : #membuat list berisi kode member
    list_kode.append(list(data.values())[0])

def scan_product():
    barcode = input("\nMasukkan kode produk: ") #memasukkan kode produk
    p1 = Product("", "", barcode)
    search_product = p1.check_product_on_inventory() #check ketersediaan produk
    if (search_product == False):
        print("Kode yang anda masukkan salah.\n")
        scan_another()
    else:
        wishlist.append(search_product) #menambah produk pada list pembelian
        scan_another()

def scan_another():
    scan_another = input("Apakah anda ingin menambahkan produk lagi? (Y/N)") #menambahkan produk
    if (scan_another == 'y' or scan_another == 'Y'):
        scan_product()

def diskon(): #menghitung total belanjaan dengan diskon
    scan_product()
    c1 = CheckoutRegister(current_date_time, wishlist)
    total_payment = c1.calculate_payment_due() #menghitung jumlah total biaya
    total_diskon = total_payment
    print("Total :", total_diskon)

    change = c1.pay_money(total_payment) #menghitung total kembalian
    c1.print_receipt(change)
    print("\nTerima kasih telah berbelanja!")
    print(current_date_time)

    next = input("Keluar dari program? (Y/N)")
    if (next == "n" or next == "N"):
        wishlist[:] = []
        main()
    else:
        sys.exit(0)
        exit()

def main(): #menghitung total belanjaan tanpa diskon
    scan_product()
    c1 = CheckoutRegister2(current_date_time, wishlist)
    total_payment = c1.calculate_payment_due() #menghitung jumlah total belanjaan

    change = c1.pay_money(total_payment) #menghitung uang kembalian
    c1.print_receipt(change) #mencetak struk belanja
    print("\nTerima kasih telah berbelanja!")
    print(current_date_time)

    next = input("Keluar dari program? (Y/N)")
    if (next == "n" or next == "N"): # kembali masuk ke program untuk membeli produk
        wishlist[:] = []
        main()
    else:
        sys.exit(0)
        exit()


print("\n======== Selamat Datang di Kasir Supermarket Mandiri ========\n")
print("1. Login member")
print("2. Buat member")
print("3. Transaksi tanpa member")

option = int(input("\nMasukkan pilihan anda (1/2/3) : "))

if option == 1 :
    while True :
        kode_member = input("Masukkan kode member anda: ")
        if kode_member in list_kode :
            print("Anda merupakan member supermarket dengan kode", kode_member)
            print("Kode dan nama produk")
            print("101 : Apel 1 kg")
            print("102 : Anggur 1 kg")
            print("103 : Stroberi 1 kg")
            print("104 : Mangga 1 kg")
            print("105 : Lemon 1 kg")
            print("106 : Alpukat 1 kg")
            print("107 : Melon 1 kg")
            print("201 : Susu 1 liter")
            print("202 : Beras 5 kg")
            print("203 : Mie instan (10 pcs)")
            print("204 : Minyak goreng 2 liter")
            print("205 : Saus sambal")
            print("206 : Paket bumbu")
            print("207 : Telur 1 kg")
            print("208 : Gula 1 kg")
            print("301 : Sabun mandi")
            print("302 : Sampo")
            print("303 : Deterjen")
            print("304 : Sabun cuci piring")
            print("305 : Pasta gigi")
            print("306 : Body mist ")
            break
        else :
            print("Kode yang anda masukkan salah")

    print("\nPENGINPUTAN PRODUK")

    diskon()

elif option == 2 :
    print("Masukkan data diri anda") #memasukkan data diri
    nama = str(input("Masukkan nama anda: "))
    no_ktp = int(input("Masukkan nomor KTP anda: "))
    no_hp = str(input("Masukkan nomor telepon anda: "))
    alamat = str(input("Masukkan alamat lengkap anda: "))
    print("\n=============")
    print("Nama: ", nama)
    print("No KTP:", no_ktp)
    print("No Telepon: ", no_hp)
    print("Alamat: ", alamat)


    from random import randint #mengacak kode untuk member baru
    for i in range(1) :
        kode_baru = randint(1, 1000)
        print("Kode member anda :", kode_baru) #mencetak kode untuk member baru

        data_baru = "\n{},{},{},{},{}".format(kode_baru,nama, no_ktp, no_hp, alamat) #memasukkan data ke database datamembership.csv
        file_bio = open("datamembership.csv", "a")
        file_bio.write(data_baru)
        file_bio.close()
        print("Kode dan nama produk")
        print("101 : Apel 1 kg")
        print("102 : Anggur 1 kg")
        print("103 : Stroberi 1 kg")
        print("104 : Mangga 1 kg")
        print("105 : Lemon 1 kg")
        print("106 : Alpukat 1 kg")
        print("107 : Melon 1 kg")
        print("201 : Susu 1 liter")
        print("202 : Beras 5 kg")
        print("203 : Mie instan (10 pcs)")
        print("204 : Minyak goreng 2 liter")
        print("205 : Saus sambal")
        print("206 : Paket bumbu")
        print("207 : Telur 1 kg")
        print("208 : Gula 1 kg")
        print("301 : Sabun mandi")
        print("302 : Sampo")
        print("303 : Deterjen")
        print("304 : Sabun cuci piring")
        print("305 : Pasta gigi")
        print("306 : Body mist ")
    print("\nPENGINPUTAN PRODUK")

    diskon()

elif option == 3 :
    print("Silahkan masukkan kode dan jumlah barang")
    print("Kode dan nama produk")
    print("101 : Apel 1 kg")
    print("102 : Anggur 1 kg")
    print("103 : Stroberi 1 kg")
    print("104 : Mangga 1 kg")
    print("105 : Lemon 1 kg")
    print("106 : Alpukat 1 kg")
    print("107 : Melon 1 kg")
    print("201 : Susu 1 liter")
    print("202 : Beras 5 kg")
    print("203 : Mie instan (10 pcs)")
    print("204 : Minyak goreng 2 liter")
    print("205 : Saus sambal")
    print("206 : Paket bumbu")
    print("207 : Telur 1 kg")
    print("208 : Gula 1 kg")
    print("301 : Sabun mandi")
    print("302 : Sampo")
    print("303 : Deterjen")
    print("304 : Sabun cuci piring")
    print("305 : Pasta gigi")
    print("306 : Body mist ")
    print("\nPENGINPUTAN PRODUK")
    main()

else :
    print("Pilihan yang anda inputkan salah.")
