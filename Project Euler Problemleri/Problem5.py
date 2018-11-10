"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#Çok uzun sürüyor
"""  def bölenler(limit):
        liste = list()
        for sayı in range(1,limit+1):
            liste.append(sayı)
        return liste
    kilit = 0
    sayı = 2
    while kilit <= 10:
    
    
        for bölen in bölenler(10):
    
            if sayı%bölen !=0:
                sayı +=1
                kilit = 0
    
            else:
                kilit +=1
                
    
    
    print(sayı)
"""
#2. yol daha kısa sürüyor

#2520 1 ile 10 arasındaki tüm sayılara tam bölünüyor.11 ve 20 arasındaki asal sayıları eklersek sorun çözülür.
#16 = 2**4 oldugundan ve ilk 10 sayıdaki 2**3 den buyuk oldugu icin bir tane 2 carpanı ekleriz.

print(2520*11*13*17*19*2)








