"""
A palindromic number reads the same both ways.
 The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
liste = list()
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):

        sayı = i * j
        sayı = str(sayı)

        if len(sayı) == 6:
            if sayı[0] + sayı[1] + sayı[2] == sayı[5] + sayı[4] + sayı[3]:
                liste.append(sayı)

print(max(liste))





