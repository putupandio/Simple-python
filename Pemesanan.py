class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        
        # Jika count lebih besar dari atau sama dengan 3, kalikan dengan 0.9
        if count >= 3:
            total_price *= 0.9
        
        # Bulatkan total_price ke nomor non-desimal terdekat dan return nilainya
        return round(total_price)

menu_item1 = MenuItem('Roti Lapis', 5)
menu_item2 = MenuItem('Kue Coklat', 4)
menu_item3 = MenuItem('Kopi', 3)
menu_item4 = MenuItem('Jus Jeruk', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Masukkan nomor menu: '))
selected_menu = menu_items[order]
print('Item yang di pilih: ' + selected_menu.name)

# Terima input dari console, dan Berikan input ke variable count
count = int(input("Jumlah pesanan (diskon 10% untuk 3 atau lebih): "))

# Panggil method get_total_price 
result = selected_menu.get_total_price(count)

# Cetak 'Total harga adalah $____'
print("Total harga adalah$" + str(result))