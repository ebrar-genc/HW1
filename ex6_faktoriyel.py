"""
İki terminal arasında resim gönderme islemi. 
Resim boyutu en az = 100kb
"""
#!/usr/bin/env python3
#server dosyasi

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 12345))
s.listen(10)


print("Sunucu acildi...\nİstemciler bekleniyor...")

while True:
    c, addr = s.accept()
    print('\n{} baglandi.'.format(addr))
    datas = c.recv(1024)
    f = open("dosya.jpg", "wb")
    while datas:
        f.write(datas)
        datas = c.recv(1024)
    f.close()
    print("resim alindi...")
    continue