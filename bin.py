import math

nom = int(float(input("Enter:")))
a = []

def bina(num):
    while num > 0:
        r = num%2
        if r == 0:
            num = num/2
        elif r == 1:
            num = (num-1)/2
        r = math.floor(r)
        a.append(r)
    a.reverse()
    news = ''.join(map(str, a))
    print(news)
    
        
bina(nom)

#for x in range(len(a)):
     #   print(a[x])