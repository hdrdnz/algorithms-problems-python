'''Collatz sanısı, Lothar Collatz tarafından ortaya atılan, 1'den büyük tüm doğal sayıların 1'e indirebildiğini anlatan bir konjektür. 
Eğer sayı çift ise yarısını, tek ise 3 katının bir fazlası alınır. 1'e ulaşana kadar bu işlem devam eder. 
 '''

number = int(input('enter number:'))

while number != 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = number*3+1
    print(number)
