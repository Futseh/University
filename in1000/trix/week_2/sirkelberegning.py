import numpy as np

radius = float(input('Hva er radiusen til sirkelen? '))

diameter = 2 * radius
areal = np.pi * radius**2
omkrets = diameter * np.pi

print('%-8s: %5.2f' % ('Diameter', diameter))
print('%-8s: %5.2f' % ('Areal', areal))
print('%-8s: %5.2f' % ('Omkrets', omkrets))

"""
Terminal> python3 sirkelberegning.py
    Hva er radiusen til sirkelen? 2
    Diameter:  4.00
    Areal   : 12.57
    Omkrets : 12.57
"""