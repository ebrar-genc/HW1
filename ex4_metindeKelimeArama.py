"""
faktoriyel hesabı yapan fonksiyon
"""

x=int(input("Bir sayi giriniz:"))
def faktoryel(x):
    carpim=1
    i=1
    if x == 0:
        return (1)
    if x < 0:
        return "Negatif bir sayi girdiniz"
    while i<=x:
        carpim*=i
        i+=1
    return(carpim)

print(faktoryel(x))