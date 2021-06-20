"""
def mymax(dizi):
    sayi = dizi[0]
    for i in dizi:
        if sayi < i:
            sayi = i
    return sayi


def mymin(dizi):
    sayi = dizi[0]
    for i in dizi:
        if sayi > i:
            sayi = i
    return sayi


mylist = [12,4,-3,0,29,-8,11]
print("Maximum element : ", mymax(mylist))
print("Minumum element : ", mymin(mylist))


"""










"""
import math
def psi(x,n,L):
    if x>=0 and x <=L:
        return math.sqrt((2/L)) * math.sin((n*math.pi*x)/L)
    return 0

x = -1
n = 1
L = 1

data = []
while x >= 2:
    data.append(psi(x,n,L))
    x += 1

stri = ""
for i in data:
    stri += str(i)
file = open("psi.dat","w")
file.write((stri))
file.close()

"""






"""
import math
def psi(x,n,L):
    if x>=0 and x <=L:
        return math.sqrt((2/L)) * math.sin((n*math.pi*x)/L)
    return 0


x = -1
n = 1
L = 1

data = []
while x >= 2:
    data.append(psi(x,n,L))
    x += 1



outfile = open('psi.dat', 'w')
for t in data:
    outfile.write("{}".format(str(t)))

outfile.close()
"""











"""

import math
def psi(x,n,L):
    if x>=0 and x <=L:
        return math.sqrt((2/L)) * math.sin((n*math.pi*x)/L)
    return 0

print("x, n, L giriniz")
x = int(input("x : "))
n = int(input("n : "))
L = int(input("L : "))
print(psi(x,n,L))


"""
"""
def f1():
    f2()
    print(x)
def f2():
    global x
    x = False
f1()
"""
candles = [82 ,49 ,82 ,82 ,41 ,82 ,15 ,63, 38, 25]
candles = sorted(candles)
temp = 0
tempi = 0
ans = 0
for index, value in enumerate(candles):
    if value != temp and ans < 1+ index - tempi:
        ans = index - tempi
        tempi = index
    temp = value
if ans<len(candles)-tempi:
    ans = len(candles)-tempi
print(ans)
