"""Bir 100 metre koşucusu farklı günlerde yaptığı sürelerin kaydını tutmaktadır.
Kullanıcıdan süre sayısını ve süreleri alan; en küçük, en büyük ve ortalama 
süreleri ekrana yazdıran Python kodunu yazınız.
Örnek girdi ve çıktı aşağıda verilmiştir:
Girdi:
5
9.97
10.53
11.23
11.28
10.18
Çıktı:
9.97
11.28
10.638 """

sayi = int(input('sayi giriniz'))
liste = []
toplam = 0.0
for i in range(1, sayi+1):
    a = float(input('süre giriniz:'))
    toplam += a
    liste.append(a)

print(min(liste))
print(max(liste))
print(toplam/sayi)
