'''
Öğrenci sayısı, öğrencilerin isimleri ve bir sınavdan aldıkları notlar her biri
bir satır olacak şekilde girdi olarak verilmektedir. Sınavda aynı notu alan
öğrenciler bulunmamaktadır(her not farklı). Verilen girdiye göre en düşük ikinci
notu ve en yüksek ikinci notu alan öğrencilerin adlarını alt alta yazdıran
Python kodunu yazınız.

Programın örnek çalışması aşağıda verilmiştir:
Girdi:
7
Ogrenci 1
3
Ogrenci 2
68
Ogrenci 3
86
Ogrenci 4
87
Ogrenci 5
40
Ogrenci 6
76
Ogrenci 7
31
Çıktı:
Ogrenci 7
Ogrenci 3
'''

sayi = int(input("ögrenci sayisini giriniz:"))
notListe = []
isimListe = []

for i in range(1, sayi+1):
    isim = str(input("isim giriniz:"))
    isimListe.append(isim)
    puan = int(input("not giriniz:"))
    notListe.append(puan)

 # en yüksek ikinci notu bulmak için:
# Dizi çoğalt
new_list = set(notListe)
# Son elemanı çıkar
new_list.remove(max(new_list))
# en yüksek ikinci not:
deger = max(new_list)


for i in range(0, len(notListe)):
    if notListe[i] == deger:
        indis = i
for i in range(0, len(isimListe)):
    if i == indis:
        maxİsim = isimListe[i]

# en düşük ikinci notu bulmak için:
# Dizi çoğalt.
new_list2 = set(notListe)
# Son elemanı çıkar
new_list2.remove(min(new_list2))
# en düşük ikinci not:
deger2 = min(new_list2)


for i in range(0, len(notListe)):
    if notListe[i] == deger2:
        indis2 = i

for i in range(0, len(isimListe)):
    if i == indis2:
        minİsim = isimListe[i]


print(minİsim)
print(maxİsim)
