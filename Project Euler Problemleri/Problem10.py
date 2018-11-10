"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#Çok yavaş
def asal_mi(sayi):

    if sayi <2:
        return False
    else:
        for i in range(2,int(sayi**0.5)+1):
            if sayi%i == 0:
                return False
        return True


sinir = 2000000
toplam = 0
for i in range(2,sinir):

    if asal_mi(i):
        toplam += i
print(toplam)

#Daha hizli yol
"""def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

print(sum(get_primes(2000000)))"""