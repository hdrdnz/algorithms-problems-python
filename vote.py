'''
Bir sınıfta başkan seçimi yapılacaktır. İsimler ve oylar sözlük yapısında tutulacaktır. En yüksek oyu alan kişi başkan seçilecektir.
'''

sinif = dict()
list = []
sayi = int(input("kişi sayisini giriniz:"))

for i in range(1, sayi+1):
    isim = str(input("isim giriniz:"))
    puan = int(input("oy sayisini giriniz:"))
    sinif[isim] = int(puan)


for anahtar, deger in sinif.items():
    list.append(deger)

maxOy = max(list)

for anahtar, deger in sinif.items():
    if (deger == maxOy):
        maxİsim = anahtar

print("başkan olan kişi: "+maxİsim)
