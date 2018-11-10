"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

x = 600851475143

bölen = 2
en_büyük_bölen = 0

while x!=1:

    if x%bölen == 0:
        x = x // bölen
        en_büyük_bölen = max(en_büyük_bölen,bölen)
        bölen = 2

    else:
        bölen +=1
print(en_büyük_bölen)

    








