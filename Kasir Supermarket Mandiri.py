from produk import Product
from checkout2 import CheckoutRegister2
from checkout import CheckoutRegister
from time import gmtime, strftime
import csv
# import sys
import os
import sys

current_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
wishlist = []

datamember = []
with open('datamembership.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        datamember.append(row)
# print(datamember)
list_kode = []
for data in datamember :
    list_kode.append(list(data.values())[0])
# print(kodemember)

def scan_product():
    barcode = input("\nMasukkan kode produk: ")
    p1 = Product("", "", barcode)
    search_product = p1.check_product_on_inventory()
    if (search_product == False):
        print("Kode yang anda masukkan salah.\n")
        scan_another()
    else:
        wishlist.append(search_product)
        scan_another()

def scan_another():
    scan_another = input("Menambahkan produk? (Y/N)")
    if (scan_another == 'y' or scan_another == 'Y'):
        scan_product()

def diskon():
    scan_product()
    c1 = CheckoutRegister(current_date_time, wishlist)
    total_payment = c1.calculate_payment_due()
    total_diskon = total_payment * 0.9
    print("Total :", total_diskon)
    change = c1.pay_money(total_payment)
    # print("Change:",change)
    c1.print_receipt(change)
    print("\nTerima kasih telah berbelanja!")

    next = input("Keluar dari program? (Y/N)")
    if (next == "n" or next == "N"):
        wishlist[:] = []
        main()
    else:
        sys.exit(0)
        exit()

def main():
    scan_product()
    c1 = CheckoutRegister2(current_date_time, wishlist)
    total_payment = c1.calculate_payment_due()
    change = c1.pay_money(total_payment)
    # print("Change:",change)
    c1.print_receipt(change)
    print("\nTerima kasih telah berbelanja!")

    next = input("Keluar dari program? (Y/N)")
    if (next == "n" or next == "N"):
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
            break
        else :
            print("Kode yang anda masukkan salah")
            # kode_member = input("Masukkan kode member anda: ")
    print("\nPENGINPUTAN PRODUK")

    diskon()

elif option == 2 :
    print("Masukkan data diri anda")
    nama = str(input("Masukkan nama anda: "))
    no_ktp = int(input("Masukkan nomor KTP anda: "))
    no_hp = str(input("Masukkan nomor telepon anda: "))
    alamat = str(input("Masukkan alamat lengkap anda: "))
    print("\n=============")
    print("Nama: ", nama)
    print("No KTP:", no_ktp)
    print("No Telepon: ", no_hp)
    print("Alamat: ", alamat)


    from random import randint
    for i in range(1) :
        kode_baru = randint(1, 1000)
        print("Kode member anda :", kode_baru)

        data_baru = "\n{},{},{},{},{}".format(kode_baru,nama, no_ktp, no_hp, alamat)
        file_bio = open("datamembership.csv", "a")
        file_bio.write(data_baru)
        file_bio.close()
    print("\nPENGINPUTAN PRODUK")

    diskon()

elif option == 3 :
    print("Silahkan masukkan kode dan jumlah barang")

else :
    print("Pilihan yang ada inputkan salah.")
    
print("\nPENGINPUTAN PRODUK")

main()
