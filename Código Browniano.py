import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scp

data = open("data.txt", "r", encoding="utf8")

d = []
r=np.linspace(0,4.5)
def exponencial(r,D,N):
    t=5
    return N/(2*D*t)*r*np.exp(-r**2/4/D/t)*0.3
def exp(r):
    D=0.17
    N=96
    t=5
    return N/(2*D*t)*r*np.exp(-r**2/4/D/t)
for linea in data:
    
    d.append(float(linea))
    
data.close()
    
n = np.arange(0, 4.5, 0.3)
N = [0]*len(n)

for i in range(len(n)-1):
    
    for j in d:
        
        if n[i] <= j <= n[i+1]:
            
            N[i] += 1
            
plt.figure(figsize=(14, 6))
plt.suptitle("Distribución Browniana", size="16")
plt.subplot(1,2,1)
plt.grid()

data2 = open("data2.txt", "r", encoding="utf8")

d2 = []

for linea in data2:
    
    d2.append(float(linea))
    
data2.close()
    
N2 = [0]*len(n)

for i in range(len(n)-1):
    
    for j in d:
        
        if n[i] <= j <= n[i+1]:
            
            N2[i] += 1
            
plt.hist(d2, n, alpha=1)
plt.plot(r, exponencial(r,0.1,98))
plt.title("D=0.1")
plt.xlabel("r (cm)")
plt.ylabel("N")
plt.subplot(1,2,2)
plt.hist(d, n, alpha=1)
plt.plot(r, exponencial(r,0.17,96))
plt.title("D=0.17")
plt.xlabel("r (cm)")
plt.ylabel("N")
plt.grid()
plt.savefig("Comparacion.png", dpi=200)
plt.show()
print(scp.quad(exp,0,1000, args=()))

plt.figure(figsize=(9, 6))
plt.hist(d, n)
plt.grid()
plt.hist(d2, n, alpha=0.5)
plt.xlabel("r (cm)")
plt.ylabel("N")
plt.savefig("Histograma resultados.png", dpi=200)

T1 = open("tracker1.txt", "r", encoding="utf8")
T2 = open("tracker2.txt", "r", encoding="utf8")
T3 = open("tracker3.txt", "r", encoding="utf8")

def dataOut(T):
    
    t, x, y, r = [], [], [], []
    
    T.readline(), T.readline() #Eliminamos la primera línea, títulos.
    
    for linea in T:
        
        l = linea.replace(",",".").split()
        
        t.append(float(l[0]))
        x.append(float(l[1]))
        y.append(float(l[2]))
        r.append(float(l[3]))
    
    return t, x, y, r

t1, x1, y1, r1 = dataOut(T1)
t2, x2, y2, r2 = dataOut(T2)
t3, x3, y3, r3 = dataOut(T3)

T1.close()
T2.close()
T3.close()

plt.figure(figsize=(9, 9))
plt.grid()
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.scatter(0, 0)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("Random walk.png", dpi=200)

plt.figure(figsize=(9, 6))
plt.grid()
plt.plot(t1, np.array(r1)**2)
plt.plot(t2, np.array(r2)**2)
plt.plot(t3, np.array(r3)**2)
plt.ylabel("$r^2 (m^2)$")
plt.xlabel("t (s)")
plt.savefig("Radios.png", dpi=200)

def dRsq(r):
    
    return np.array([(r[i+1]-r[i])**2 for i in range(len(r)-1)])

rSq1, rSq2, rSq3 = dRsq(r1), dRsq(r2), dRsq(r3)

plt.figure(figsize=(9, 6))
plt.plot(t1[0:len(t1)-1:], rSq1)
plt.plot(t2[0:len(t2)-1:], rSq2)
plt.plot(t3[0:len(t3)-1:], rSq3)
plt.xlabel("t (s)")
plt.ylabel("$(\\Delta r)^2$")
plt.grid()
plt.savefig("Camino libre.png", dpi=200)