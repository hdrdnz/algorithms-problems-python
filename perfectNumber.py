'''Mükemmel sayı, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayıdır.
'''

number = int(input('enter number:'))
sum = 0
for i in range(1, number):
    if (number % i == 0):
        sum += i

if sum == number:
    print('perfect number')

else:
    print('not perfect number ')
