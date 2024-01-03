daftar_buku = ['Kami (Bukan) Sarjana Kertas', 'Kami (Bukan) Jongos berdasi', 'Kami (Bukan) Generasi B*cot']
print("Daftar variable list")
print(daftar_buku)

print("\nPecah List")
for buku in daftar_buku:
    print(buku)

print("\nTampilkan berdasarkan index")
print(daftar_buku[0])

print("\n Pecah dengan range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nTambah array/list")
daftar_buku.append('Buku SiDu')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

