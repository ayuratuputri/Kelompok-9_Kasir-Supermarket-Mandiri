import csv

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

print("======== Selamat Datang di Kasir Supermarket Mandiri ========")
print("1. Login member")
print("2. Buat member")
print("3. Transaksi tanpa member")

option = int(input("\nMasukkan pilihan anda (1/2/3) : "))

if option == 1 :
    kode_member = input("Masukkan kode member anda: ")
    if kode_member in list_kode :
        print("Anda merupakan member supermarket dengan kode", kode_member)
    else :
        print("Kode yang anda masukkan salah")
        # kode_member = input("Masukkan kode member anda: ")

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

elif option == 3 :
    print("Silahkan masukkan kode dan jumlah barang")

else :
    print("Pilihan yang ada inputkan salah.")
    option = int(input("\nMasukkan pilihan anda (1/2/3) : "))
    







