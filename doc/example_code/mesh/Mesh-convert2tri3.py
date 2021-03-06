from abapy.mesh import Mesh, Nodes, RegularQuadMesh
import matplotlib.pyplot as plt
from numpy import cos, pi


def function(x, y, z, labels):
    r = (x**2 + y**2)**.5
    return cos(2 * pi * x) * cos(2 * pi * y) / (r + 1.)


N1, N2 = 30, 30
l1, l2 = 1., 1.
Ncolor = 10
mesh = RegularQuadMesh(N1=N1, N2=N2, l1=l1, l2=l2)
field = mesh.nodes.eval_function(function)

fig = plt.figure(figsize=(16, 4))
ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
ax.set_aspect('equal')
ax2.set_aspect('equal')
ax3.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])
ax3.set_xticks([])
ax3.set_yticks([])
ax.set_frame_on(False)
ax2.set_frame_on(False)
ax3.set_frame_on(False)
ax.set_title('Orginal Mesh')
ax2.set_title('Triangularized Mesh')
ax3.set_title('Field')
x, y, z = mesh.get_edges()  # Mesh edges
xt, yt, zt = mesh.convert2tri3().get_edges()  # Triangular mesh edges
xb, yb, zb = mesh.get_border()
X, Y, Z, tri = mesh.dump2triplot()
ax.plot(x, y, 'k-')
ax2.plot(xt, yt, 'k-')
ax3.plot(xb, yb, 'k-', linewidth=2.)
ax3.tricontourf(X, Y, tri, field.data, Ncolor)
ax3.tricontour(X, Y, tri, field.data, Ncolor, colors='black')
ax.set_xlim([-.1 * l1, 1.1 * l1])
ax.set_ylim([-.1 * l2, 1.1 * l2])
ax2.set_xlim([-.1 * l1, 1.1 * l1])
ax2.set_ylim([-.1 * l2, 1.1 * l2])
ax3.set_xlim([-.1 * l1, 1.1 * l1])
ax3.set_ylim([-.1 * l2, 1.1 * l2])
plt.show()
