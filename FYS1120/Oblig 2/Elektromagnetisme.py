import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

me = 9.11 * 10**(-31) # kg
e = 1.60 * 10**(-19) # C (ladningen skal vere negativ pga elektron)

mp = 1.67 * 10**(-27) # kg
q = e

mikro = 10**(-6)
nano = 10**(-9)
piko = 10**(-12)
femto = 10**(-15)

rD = 50 * 10**(-3)
d = 90 * mikro
E0 = 25000 / (90 * mikro)

tol = 4*10**(-11)

# *args should be given in (t, a, v, r, E, B, temp)
def calculater(cross, magnet, syklo, *args):
    t = args[0]
    a = args[1]
    v = args[2]
    r = args[3]
    E = args[4]
    B = args[5]
    temp = args[6]
    dt = t[1]
    
    for i in range(len(t) - 1):
        for j in range(3):
            # Cross product
            if cross:
                if j == 0:
                    temp[j][i] = ((v[j + 1][i] * B[2]) - (v[j + 2][i] * B[1]))
                elif j == 1:
                    temp[j][i] = ((v[j + 1][i] * B[0]) - (v[j - 1][i] * B[2]))
                elif j == 2:
                    temp[j][i] = ((v[j - 2][i] * B[1]) - (v[j - 1][i] * B[0]))        
            
            if syklo:
                w = (q / mp) * np.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
                
                if (r[0][i] >= -d / 2) and (r[0][i] <= d / 2):
                    E[0][i] = E0 * np.cos(w * t[i])
                else:
                    E[j][i] = 0
                
                a[j][i] = (q * E[j][i] + q * temp[j][i]) / mp
            elif magnet:
                a_mag[j][i] = (-e / me) * temp[j][i]
                
                if (r[0][i] >= r[0][0] - tol) and (r[0][i] <= r[0][0] + tol) and (r[1][i] >= r[1][0] - tol) and (r[1][i] <= r[1][0] + tol) and i > 75:
                    print t[i] 
            
            v[j][i + 1] = v[j][i] + a[j][i] * dt
            r[j][i + 1] = r[j][i] + v[j][i + 1] * dt
    
    return t, a, v, r
"""
th = np.linspace(0, mikro, float(mikro) / (100*nano) + 1) # 100 ns per steg
dth = th[1]

E = [-1.0, -2.0, 5.0] # N/C

rh = np.zeros(shape=(3, len(th))) # [[x], [y], [z]]
vh = np.zeros(shape=(3, len(th))) # [[vx], [vy], [vz]]
ah = np.zeros(shape=(3, len(th))) # [[ax], [ay], [az]]
rah = np.zeros(shape=(3, len(th))) # [[x], [y], [z]] analytisk

#Task 1

for i in range(len(th)):
    for j in range(3):
        ah[j][i] = (-e / me) * E[j]
        rah[j][i] = 0.5 * ah[j][i] * th[i]**2

for i in range(len(th) - 1):
    for j in range(3):
        vh[j][i + 1] = vh[j][i] + ah[j][i] * dth
        rh[j][i + 1] = rh[j][i] + vh[j][i + 1] * dth

plt.plot(th, rh[0], label="Numerisk")
plt.plot(th, rah[0], label="Analytisk")
plt.legend()
plt.show()

plt.plot(th, rh[0], label="x")
plt.plot(th, rh[1], label="y")
plt.plot(th, rh[2], label="z")
plt.xlabel("Tid [s]")
plt.ylabel("Posisjon [m]")
plt.legend()
plt.show()

tn = np.linspace(0, mikro, float(mikro) / nano + 1) # 1 ns per steg
dtn = tn[1]

rn = np.zeros(shape=(3, len(tn))) # [[x], [y], [z]]
vn = np.zeros(shape=(3, len(tn))) # [[vx], [vy], [vz]]
an = np.zeros(shape=(3, len(tn))) # [[ax], [ay], [az]]
ran = np.zeros(shape=(3, len(tn))) # [[x], [y], [z]] analytisk

for i in range(len(tn)):
    for j in range(3):
        an[j][i] = (-e / me) * E[j]
        ran[j][i] = 0.5 * an[j][i] * tn[i]**2

for i in range(len(tn) - 1):
    for j in range(3):
        vn[j][i + 1] = vn[j][i] + an[j][i] * dtn
        rn[j][i + 1] = rn[j][i] + vn[j][i + 1] * dtn

plt.plot(tn, rn[0], label="Numerisk")
plt.plot(tn, ran[0], label="Analytisk")
plt.legend()
plt.show()

plt.plot(tn, rn[0], label="x")
plt.plot(tn, rn[1], label="y")
plt.plot(tn, rn[2], label="z")
plt.xlabel("Tid [s]")
plt.ylabel("Posisjon [m]")
plt.legend()
plt.show()

#3D plot

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(rn[0], rn[1], rn[2])
ax.set_xlabel("Posisjon [m]")
ax.set_ylabel("Posisjon [m]")
ax.set_zlabel("Posisjon [m]")
plt.show()
"""
#Task 2

B = [0, 0, 2] # T

t_mag = np.linspace(0, 30*piko, 30 * piko / femto + 1)
dt = t_mag[1]

a_mag = np.zeros(shape=(3, len(t_mag)))
v_mag = np.zeros(shape=(3, len(t_mag)))
r_mag = np.zeros(shape=(3, len(t_mag)))
temp_mag = np.zeros(shape=(3, len(t_mag)))

v_mag[0][0] = 10000

t_mag, a_mag, v_mag, r_mag = calculater(True, True, False, t_mag, a_mag, v_mag, r_mag, None, B, temp_mag)

plt.plot(t_mag, r_mag[0], label="x")
plt.plot(t_mag, r_mag[1], label="y")
plt.plot(t_mag, r_mag[2], label="z")
plt.xlabel("Tid [s]")
plt.ylabel("Posisjon [m]")
plt.legend()
plt.show()

plt.plot(t_mag, v_mag[0], label="vx")
plt.plot(t_mag, v_mag[1], label="vy")
plt.plot(t_mag, v_mag[2], label="vz")
plt.xlabel("Tid [s]")
plt.ylabel("Hastighet [m]")
plt.legend()
plt.show()
"""
x = np.fft.fft(r_mag[0])
freqx = np.fft.fftfreq(len(r_mag[0]), t_mag[1] - t_mag[0])
y = np.fft.fft(r_mag[1])
freqy = np.fft.fftfreq(len(r_mag[1]), t_mag[1] - t_mag[0])

plt.plot(np.abs(x), np.abs(y))
plt.show()

plt.plot(freqx / 10**(14), np.abs(x))
plt.show()

plt.plot(freqy / 10**(14), np.abs(y))
plt.show()
"""
fig = plt.figure()
ax = plt.axes(projection="3d")

ax.scatter(r_mag[0], r_mag[1], r_mag[2])
ax.set_xlabel("x Posisjon [m]")
ax.set_ylabel("y Posisjon [m]")
ax.set_zlabel("z Posisjon [m]")
plt.show()

# Task 3

B = [0, 0, 1.5]

t_syk = np.linspace(0, 300*nano, 1000 )#300*nano / (100 * femto) + 1)

dt_syk = t_syk[1]

a_syk = np.zeros(shape=(3, len(t_syk)))
v_syk = np.zeros(shape=(3, len(t_syk)))
r_syk = np.zeros(shape=(3, len(t_syk)))
E_syk = np.zeros(shape=(3, len(t_syk)))

temp_syk = np.zeros(shape=(3, len(t_syk)))

#r_syk[0][0] = rD

t_syk, a_syk, v_syk, r_syk = calculater(True, False, True, t_syk, a_syk, v_syk, r_syk, E_syk, B, temp_syk)

plt.plot(r_syk[0], r_syk[1])
plt.xlabel("x Posisjon [m]")
plt.ylabel("y Posisjon [m]")
plt.show()

plt.plot(t_syk, r_syk[0], label="x")
plt.plot(t_syk, r_syk[1], label="y")
plt.plot(t_syk, r_syk[2], label="z")
plt.legend()
plt.show()

plt.plot(t_syk, v_syk[0], label="vx")
plt.plot(t_syk, v_syk[1], label="vy")
plt.plot(t_syk, v_syk[2], label="vz")
plt.legend()
plt.show()