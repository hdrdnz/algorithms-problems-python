'''
Parametre olarak verilen iki listedeki ortak elemanları tekrarsız ve sıralı
olarak geri döndüren ortak fonksiyonunu yazınız.
Fonksiyonun örnek çalışması aşağıda verilmiştir:
>>> ortak([4, 2, 1, 2, 2, 1, 2, 4, 5, 1], [2, 4, 1, 3, 5, 2, 1, 3, 1, 1])
[1, 2, 4, 5]
'''


def ortak(liste1, liste2):
    liste = list()
    list1 = sorted(set(liste1))
    list2 = sorted(set(liste2))
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                liste.append(list1[i])
    print(liste)


ortak([4, 2, 1, 2, 2, 1, 2, 4, 5, 1], [2, 4, 1, 3, 5, 2, 1, 3, 1, 1])
