print("~~~~~~~~~~Selamat Datang di Kasir Supermarket Mandiri~~~~~~~~~~")
print("Pilih option :")
print("1. Login member")
print("2. Buat member")
print("3. Transaksi tanpa member")
option=int(input("Silahkan pilih option: "))
if option==1:
    kode_member = int(input("Masukkan kode member anda: "))
    print("Kode member anda adalah:",  kode_member)
elif option==2:
    print("Masukkan data diri anda")
    nama = str(input("Masukkan nama anda: "))
    no_ktp = int(input("Masukkan nomor KTP anda: "))
    no_hp = str(input("Masukkan nomor telepon anda: "))
    alamat = str(input("Masukkan alamat lengkap anda: "))
    print("Nama: ", nama)
    print("No KTP:", no_ktp)
    print("No Telepon: ", no_hp)
    print("Alamat: ", alamat)
else:
    print("Silahkan masukkan kode dan jumlah barang")




