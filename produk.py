class Product(): # List produk yang dijual beserta harga dan kode
    product_list = [
        {   'nama': 'Apel 1 kg',    'harga': 21000, 'kode': '101'   },
        {   'nama': 'Anggur 1 kg',  'harga': 30000, 'kode': '102'   },
        {   'nama': 'Stroberi 1 kg','harga': 36000, 'kode': '103'   },
        {   'nama': 'Mangga 1 kg',  'harga': 23000, 'kode': '104'   },
        {   'nama': 'Lemon 1 kg',   'harga': 35000, 'kode': '105'   },
        {   'nama': 'Alpukat 1 kg', 'harga': 32400, 'kode': '106'   },
        {   'nama': 'Melon 1 kg',   'harga': 22000, 'kode': '107'   },
        {   'nama': 'Susu 1 liter',         'harga': 18000, 'kode': '201'   },
        {   'nama': 'Beras 5 kg',           'harga': 56000, 'kode': '202'   },
        {   'nama': 'Mie instan (10 pcs)',  'harga': 24700, 'kode': '203'   },
        {   'nama': 'Minyak goreng 2 liter','harga': 28500, 'kode': '204'   },
        {   'nama': 'Saus sambal',          'harga': 14800, 'kode': '205'   },
        {   'nama': 'Paket bumbu',          'harga': 12400, 'kode': '206'   },
        {   'nama': 'Telur 1 kg',           'harga': 22400, 'kode': '207'   },
        {   'nama': 'Gula 1 kg',            'harga': 19300, 'kode': '208'   },
        {   'nama': 'Sabun mandi',      'harga': 21000, 'kode': '301'},
        {   'nama': 'Sampo',            'harga': 17800, 'kode': '302'},
        {   'nama': 'Deterjen ',        'harga': 26300, 'kode': '303'},
        {   'nama': 'Sabun cuci piring','harga': 20900, 'kode': '304'},
        {   'nama': 'Pasta gigi',       'harga': 28000, 'kode': '305'},
        {   'nama': 'Body mist',        'harga': 24000, 'kode': '306'},
    ]


    def __init__(self, nama, harga, kode): # menginisiasi data
        self.nama = nama
        self.harga = harga
        self.kode = kode

    def check_product_on_inventory(self): # check data di list penjualan
        found = False
        for index, product in enumerate(self.product_list):

            if self.kode == product['kode']:
                product_found = {'nama': product['nama'], 'harga': product['harga'], 'kode': product['kode']}
                found = True
                print(product['nama'], "- Rp  " + str(product['harga']), '\n')

        if found == True:
            return product_found
        else:
            return False
