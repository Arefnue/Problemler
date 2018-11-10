"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

#Çok uzun sürüyor
"""def asal_mi(sayı):

    if sayı == 2:
        return True
    elif sayı == 1:
        return False
    else:
        for i in range(2,sayı):

            if sayı%i ==0:
                return False
        return True



def kacinci(sayı):
    asallar = list()
    for i in range(2,99999999999999):

        if asal_mi(i):
            asallar.append(i)

        if len(asallar) == sayı+1:
            return asallar[sayı-1]


print(kacinci(10001))"""


def asal_mi(sayi):

    if sayi <2:
        return False
    else:
        for i in range(2,int(sayi**0.5)+1):
            if sayi%i == 0:
                return False
        return True


def kacinci(sıra):

    asallar = list()
    sayi = 1
    while len(asallar) < sıra:
        sayi += 1
        if asal_mi(sayi):
            asallar.append(sayi)
    return sayi

print(kacinci(10001))


