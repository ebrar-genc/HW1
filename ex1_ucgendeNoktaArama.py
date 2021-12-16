"""
Girilen sayinin butun tam bolenlerini bulan kod
"""
def recur_factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        mes = "Hatali bir sayi girdiniz"
        return (mes)
    else:
        return n*recur_factorial(n-1)
    
def tambölen(sayı):
    liste = list()
    for i in range(1,sayı+1):
        if (sayı % i == 0):
            liste.append(i)
    return liste



while True:
    sayı = input("sayı:")
    
    if sayı == "q":
        break
    else:
        sayı = int(sayı)
        print(sayı,"Sayısını Tam Bölenler",tambölen(sayı))






