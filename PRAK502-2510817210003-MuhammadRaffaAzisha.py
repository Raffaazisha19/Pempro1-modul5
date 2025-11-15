def hitung(nilai1, nilai2):
    return abs(nilai1 - nilai2)

def mutlak(angka):
    return abs(angka)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

hasil = hitung(x1, x2) + hitung(y1, y2)
print(mutlak(hasil))