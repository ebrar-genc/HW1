import matplotlib.pyplot as plt

class Studens:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

s1 = Studens("s1",196,94)
s2 = Studens("s2",168,58)
s3 = Studens("s3",160,50)
s4 = Studens("s4",180,75)
s5 = Studens("s5",150,90)
s6 = Studens("s6",177,80) 
s7 = Studens("s7",167,60)
s8 = Studens("s8",182,75) 
s9 = Studens("s9",190,105)
s10 = Studens("s10",169,69) 

array = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

plt.figure(figsize=(10,6))

name = []
height = []
weight = []
for i in range(0,len(array)):
    name.append(array[i].name)
for i in range(0,len(array)):
    height.append(array[i].height)
for i in range(0,len(array)):
    weight.append(array[i].weight)


plt.subplot(2,2,1)

plt.plot(name,height,color="r",linewidth=2,linestyle="--",marker="o",markerfacecolor="yellow") 

plt.xlabel("Öğrenci Adı")

plt.ylabel("Boy")

plt.title("Boy Grafiği")


plt.subplot(2,2,2)

plt.plot(name,weight,color="blue",linewidth=2,linestyle="--",marker="o",markerfacecolor="yellow") 

plt.xlabel("Öğrenci Adı")

plt.ylabel("Kilo")

plt.title("Kilo Grafiği")

plt.show()