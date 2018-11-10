"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

devam = True
while devam:

    for a in range(1,1000):
        for b in range(1,1000):

            c = ((a**2)+(b**2))**(0.5)
            if a<b<c:
                if c == int(c):
                    if a+b+c == 1000:
                        print("Product is {}".format(a*b*c))
                        devam = False




