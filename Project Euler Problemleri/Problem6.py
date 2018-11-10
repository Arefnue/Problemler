"""The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def aralık(işlem,limit):
    sayı = 0
    if işlem == "Kareler toplamı":
        for i in range(1,limit+1):
            sayı = sayı+i**2
    elif işlem == "Toplamların karesi":
        for i in range(1,limit+1):
            sayı = sayı+i
        sayı = sayı**2

    return sayı

print(aralık("Toplamların karesi",100)-aralık("Kareler toplamı",100))


