"""
Girilen bir metin icinde aranan kelimeyi bulan fonksiyon 
"""

x = input("Metin giriniz:")
word= input("Metnin icinde aranacak kelimeyi giriniz:")
def find_word(sentence):
    words_list=x.split(" ")
    for i in words_list:
        if i == word :
            return "True"

print("Kelimenin metinde olup olmama durumu:",find_word(x))


