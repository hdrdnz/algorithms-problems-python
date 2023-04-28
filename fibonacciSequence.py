"Fibonacci dizisi, her sayının kendinden önceki ile toplanması sonucu oluşan bir sayı dizisidir."


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b


fib(20)
"""
output
1
1
2
3
5
8
13"""
