daftar_buku = ['Kami (Bukan) Sarjana Kertas', 'Kami (Bukan) Jongos berdasi', 'Kami (Bukan) Generasi B*cot']
print("\nPerintah Del")
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['Kami (Bukan) Sarjana Kertas', 'Kami (Bukan) Jongos berdasi', 'Kami (Bukan) Generasi B*cot']

print("\nHapus semua list dengal del")
# [start:stop], [0:1], [0:-2]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru")
daftar_buku = ['Kami (Bukan) Sarjana Kertas', 'Kami (Bukan) Jongos berdasi', 'Kami (Bukan) Generasi B*cot']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru news")
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

