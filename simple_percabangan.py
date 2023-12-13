print('Ibu Berkata, "Pergi ke Toko"')
print('Budi Menjawab, "Baik, Apa yang harus saya lakukan di toko?"')
print('Ibu Menjawab, "Beli satu botol susu"')
print('Budi berangkat ke toko')
print('Dan Mulai berbelanja')

# Percabangan
jumlah_botol_susu = 184
jumlah_telur = 1642

print(f"Jumlah botol susu {jumlah_botol_susu} btl")

if jumlah_botol_susu > 0:
    print('Budi mengecek harga, ternyata uangnya cukup')
    if jumlah_telur == 0:
        print('Budi membelu 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')
else:
    print('Budi tidak jadi membel 1 botol susu')

print('Budi pulang ke rumah')
print('Budi menyerahkan barang belanjaan')
