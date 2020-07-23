from abapy.mesh import RegularQuadMesh, Mesh
from matplotlib import pyplot as plt

m = RegularQuadMesh(N1=2, N2=2)
m.add_set('el_set', [1, 2])
m.add_surface('my_surface', [('el_set', 2), ])
m2 = m.extrude(l=1., N=2)
x, y, z = m.get_edges()
x2, y2, z2 = m2.get_edges()

# Adding some 3D "home made" perspective:
zx, zy = .3, .3
for i in range(len(x2)):
    if x2[i] != None:
        x2[i] += zx * z2[i]
        y2[i] += zy * z2[i]

# Plotting stuff
plt.figure()
plt.clf()
plt.gca().set_aspect('equal')
plt.axis('off')
plt.plot(x, y, 'b-', linewidth=4., label='Orginal Mesh')
plt.plot(x2, y2, 'r-', linewidth=1., label='Extruded mesh')
plt.legend()
plt.show()
