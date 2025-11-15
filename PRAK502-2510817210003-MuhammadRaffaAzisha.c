#include <stdio.h>
#include <math.h>

int hitung(int nilai1, int nilai2) {
    return abs(nilai1 - nilai2);
}

int mutlak(int angka) {
    return abs(angka);
}

int main() {
    int x1, y1, x2, y2;
    scanf("%d", &x1);
    scanf("%d", &y1);
    scanf("%d", &x2);
    scanf("%d", &y2);

    int hasil = hitung(x1, x2) + hitung(y1, y2);
    printf("%d", mutlak(hasil));

    return 0;
}