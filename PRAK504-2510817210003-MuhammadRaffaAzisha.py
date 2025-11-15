def reverse(n):
    # Ubah ke string, balik, lalu ubah kembali ke int (otomatis hilangkan leading zero)
    return int(str(n)[::-1])

# Input dua bilangan
A, B = map(int, input().split())

# Balik representasi desimal A dan B
A_reversed = reverse(A)
B_reversed = reverse(B)

# Jumlahkan
C = A_reversed + B_reversed

# Balik lagi hasil penjumlahan
hasil = reverse(C)

# Tampilkan hasil
print(hasil)