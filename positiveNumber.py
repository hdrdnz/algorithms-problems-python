"""
Kullanıcıdan alınan, aralarında virgül bulunan elemanlardan sadece pozitif
tamsayıları toplayan ve toplamı ekrana yazdıran bir Python programı yazınız.
Programın örnek çalışması aşağıda verilmiştir:
Girdi:
15,3.14,False,-22,10,dasds,1,-123
Çıktı:
26
"""

# 1.yöntem
top = 0
n = input()
liste = n.split(",")

for i in liste:
    if (i.isdigit()):
        top += int(i)

print(top)

# 2.yöntem
top2 = 0
for i in liste:
    try:
        a = float(i)
        if (a > 0 and (a % (int(a)) == 0)):
            top2 += a
    except:
        continue
print(int(top2))

# 3.yöntem
top3 = 0
for i in liste:
    try:
        a = int(i)
        if (a > 0 and str(a) == i):
            top3 += a
    except:
        continue
print(top3)
