class CheckoutRegister2():
    def __init__(self, checkout_date, checkout_items):
        self.checkout_date = checkout_date
        self.checkout_items = checkout_items

    def add_item_to_cart(self, p):
        self.checkout_items.append(p)

    def display_checkout_items(self):
        print("Checkout Items")
        print(self.checkout_items)

    def calculate_payment_due(self):
        cart_items = self.checkout_items
        cart_totals = 0

        for index, product in enumerate(self.checkout_items):
            cart_totals += product['harga']
        self.due = cart_totals
        return cart_totals

    def pay_money(self, total):
        amount_to_pay = total
        print("\nTotal : Rp " + str(amount_to_pay))
        change = self.accept_payment(amount_to_pay)
        return change

    def accept_payment(self, amount_to_pay):
        paid = int(0)
        customer_pay = int(0)
        due = int(0)
        total = amount_to_pay
        due = True

        while due == True :
            print("\nMETODE PEMBAYARAN")
            print("1. Tunai")
            print("2. Non tunai")
            metode = int(input("Masukkan pilihan pembayaran (1/2) :"))
            if metode == 1 :
                try:
                    paid = float(input("\nMasukkan uang pembayaran: "))
                    if (paid < 0):
                        print("Pastikan angka yang anda masukkan benar.\n")
                        continue
                    else:
                        customer_pay += paid
                        self.customer_pay = customer_pay
                        if (paid < total):
                            due = total - paid
                            total = due
                            print("Kekurangan uang pembayaran: Rp " + str(due))
                            due = True
                            continue
                        else:
                            change = paid - total
                            self.change = change
                            return change
                        break
                    break

                except ValueError:
                    print('Mohon masukkan angka yang benar.')
            else :
                str(input("Masukkan jenis e-wallet yang digunakan (Gopay/DANA/OVO) : "))
                input("Masukkan username e-wallet : ")
                input("Masukkan No.HP akun e-wallet : ")
                paid = float(input("\nMasukkan jumlah uang yang dibayarkan (tulis sesuai total): "))
                if (paid < 0):
                    print("Pastikan angka yang anda masukkan benar.\n")
                    continue
                else:
                    customer_pay += paid
                    self.customer_pay = customer_pay
                    if (paid < total):
                        due = total - paid
                        total = due
                        print("Kekurangan uang pembayaran: Rp " + str(due))
                        due = True
                        continue
                    else:
                        change = paid - total
                        self.change = change
                        return change
                    break
        return change

    def print_receipt(self, change):
        print("-----------------------------")
        print("\n----- Struk Belanja -----\n")
        print("-----------------------------")

        for index, item in enumerate(self.checkout_items):
            print(item['nama'],'\t\tRp     ' + str(item['harga']))

        print("\n")
        print("Total    :"  ,'Rp           ' + str(self.due))
        print("Cash     :"  ,'Rp           ' + str(self.customer_pay))
        print("Change   :"  ,'Rp           ' + str(self.change), '\n')
