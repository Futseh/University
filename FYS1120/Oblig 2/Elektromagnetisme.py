import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

me = 9.11 * 10**(-31) # kg
e = 1.60 * 10**(-19) # C (ladningen skal vere negativ pga elektron)

nano = 10**(-9)
mikro = 10**(-6)

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

#plt.plot(th, rh[0], label="Numerisk")
#plt.plot(th, rah[0], label="Analytisk")
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

#plt.plot(tn, rn[0], label="Numerisk")
#plt.plot(tn, ran[0], label="Analytisk")
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

#Task 2

piko = 10**(-12)
femto = 10**(-15)

vb = [10000, 0, 0] # m/s
B = [0, 0, 2] # T
t_mag = np.linspace(0, 30*piko, piko / femto + 1)

dt = t_mag[1]

a_mag = np.zeros(shape=(3, len(t_mag)))
v_mag = np.zeros(shape=(3, len(t_mag)))
r_mag = np.zeros(shape=(3, len(t_mag)))

temp = np.zeros(3)

temp[0] = ((vb[1] * B[2]) - (vb[2] * B[1]))
temp[1] = ((vb[2] * B[0]) - (vb[0] * B[2]))
temp[2] = ((vb[0] * B[1]) - (vb[1] * B[0]))

for i in range(len(t_mag) - 1):
    for j in range(3):
        a_mag[j][i] = (-e / me) * temp[j]
        v_mag[j][i + 1] = v_mag[j][i] + a_mag[j][i] * dt
        r_mag[j][i + 1] = r_mag[j][i] + v_mag[j][i + 1] * dt

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

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.scatter(r_mag[0], r_mag[1], r_mag[2])
ax.set_xlabel("Posisjon [m]")
ax.set_ylabel("Posisjon [m]")
ax.set_zlabel("Posisjon [m]")
plt.show()

# Task 3

mp = 1.67 * 10**(-27) # kg
q = e
rD = 50 * 10**(-3)
d = 90 * mikro
E0 = 25000 / (90 * mikro)

B = [0, 0, 1.5]

w = (q / mp) * np.sqrt(B[0]**2 + B[1]**2 + B[2]**2)

t_syk = np.linspace(0, 300*nano, 1000)#nano / (100 * femto) + 1)

dt_syk = t_syk[1]

a_syk = np.zeros(shape=(3, len(t_syk)))
v_syk = np.zeros(shape=(3, len(t_syk)))
r_syk = np.zeros(shape=(3, len(t_syk)))
E_syk = np.zeros(shape=(3, len(t_syk)))

temp_syk = np.zeros(shape=(3, len(t_syk)))

for i in range(len(t_syk) - 1):
    for j in range(3):
        if j == 0:
            temp_syk[j][i] = ((v_syk[j + 1][i] * B[2]) - (v_syk[j + 2][i] * B[1]))
        elif j == 1:
            temp_syk[j][i] = ((v_syk[j + 1][i] * B[0]) - (v_syk[j - 1][i] * B[2]))
        elif j == 2:
            temp_syk[j][i] = ((v_syk[j - 2][i] * B[1]) - (v_syk[j - 1][i] * B[0]))        
        
        if (r_syk[0][i] >= -d / 2) or (r_syk[0][i] <= d / 2):
            E_syk[0][i] = E0 * np.cos(w * t_syk[i])
        else:
            E_syk[j][i] = 0
        
        a_syk[j][i] = (q * E_syk[j][i] + q * temp_syk[j][i]) / mp
        v_syk[j][i + 1] = v_syk[j][i] + a_syk[j][i] * dt_syk
        r_syk[j][i + 1] = r_syk[j][i] + v_syk[j][i + 1] * dt_syk

plt.plot(t_syk, r_syk[0], label="x")
plt.plot(t_syk, r_syk[1], label="y")
plt.plot(t_syk, r_syk[2], label="z")
plt.legend()
plt.show()

plt.plot(r_syk[0], r_syk[1])
plt.xlabel("x Posisjon [m]")
plt.ylabel("y Posisjon [m]")
plt.show()