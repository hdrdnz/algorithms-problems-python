"""
Kullanıcıdan alınan iki kelimede bulunan karakterlerin(harflerin) her iki
kelimede bulunma sayılarını hesaplayan ve ilgili harfin kelimelerin bir 
tanesindeki bulunma sayısı 0 ise bulunma sayılarını toplayan aksi halde
bu sayıları çarpan ve sonucu ekrana yazdıran kodu yazınız. Aşağıda örnek
hesaplamalar verilmiştir:

Örnek 1:
Kelime 1: merhaba
Kelime 2: manyetik
Harfler(alfabetik sırada): ['a','b','e','h','i','k','m','n','r','t','y']

                  abehikmnrty
merhaba sayılar:  21110010100
manyetik sayılar: 10101111011
sonuç(çıktı) :    21111111111

Örnek 2:
Kelime 1: werewolves
Kelime 2: oversee
Harfler(alfabetik sırada): ['e', 'l', 'o', 'r', 's', 'v', 'w']

                    elorsvw
werewolves sayılar: 3111112
oversee sayılar :   3011110
sonuç(çıktı):       9111112
"""
kelime1 = input("bir kelime giriniz:")
kelime2 = input("bir kelime giriniz")
kelimeler = sorted(set(list(kelime1)+list(kelime2)))
a = 0
k1 = []
k2 = []
sonuc = ""

for i in range(0, len(kelimeler)):
    for j in range(0, len(kelime1)):
        if (kelimeler[i] == kelime1[j]):
            a += 1
    k1.append(a)
    a = 0

for i in range(0, len(kelimeler)):
    for j in range(0, len(kelime2)):
        if (kelimeler[i] == kelime2[j]):
            a += 1
    k2.append(a)
    a = 0

for i in range(0, len(kelimeler)):
    if (k1[i] == 0 or k2[i] == 0):

        sonuc += str(k1[i]+k2[i])
    else:

        sonuc += str(k1[i]*k2[i])


print(sonuc)
