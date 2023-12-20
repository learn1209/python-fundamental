jumlah_buku = 10
total_jumlah_baca = 0
print("ibu berkata, baca semua buku")

jumlah_buku_terbaca_dan_dipahami = 0
print(f"Jumlah buku yg sudah dubaca {jumlah_buku_terbaca_dan_dipahami}")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_terbaca_dan_dipahami == 9:
        print(f"Belum Paham {jumlah_buku_terbaca_dan_dipahami + 1}")
    else:
        jumlah_buku_terbaca_dan_dipahami = jumlah_buku_terbaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_terbaca_dan_dipahami} terbaca")
    

print(f"Jumlah buku yg sudah dibaca {jumlah_buku_terbaca_dan_dipahami}")
if jumlah_buku_terbaca_dan_dipahami == jumlah_buku:
    print('Semua buku sudah terbaca')
else:
    print(f'Tidak semua bisa dipahami, sekarang masih {jumlah_buku_terbaca_dan_dipahami}')