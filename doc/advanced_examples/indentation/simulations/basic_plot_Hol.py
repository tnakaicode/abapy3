# Importing packages
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm
from scipy.spatial import Delaunay

# Setting up the database
from classes import Simulation, Database_Manager

# ----------------------------------------------------------------------------------------------------------------
# SETTINGS
work_dir = 'workdir/'
plot_dir = 'plots/'
database_dir = 'database/'
database_name = 'database'
abqlauncher = '/opt/Abaqus/6.9/Commands/abaqus'
cls = Simulation
# ----------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------
# Starting Database Manager
db_manager = Database_Manager(
    work_dir=work_dir,
    database_dir=database_dir,
    database_name=database_name,
    abqlauncher=abqlauncher,
    cls=cls)
# ----------------------------------------------------------------------------------------------------------------



# creating some shortcuts
d = db_manager     # database manager
c = db_manager.cls  # useful to call Simulation attributs

# Load simulations
simus = d.query().filter(c.completed == True).filter(
    c.sample_mat_type == 'hollomon').all()
simus = [s for s in simus if s.sample_mat_args['yield_stress'] <= 0.01]

# --------------------------
# PLOTING CONSTRAINT FACTOR
# --------------------------

# Getting primary data
sy = np.array([s.sample_mat_args['yield_stress'] for s in simus])
E = np.array([s.sample_mat_args['young_modulus'] for s in simus])
n = np.array([s.sample_mat_args['hardening'] for s in simus])
C = np.array([s.load_prefactor for s in simus])
Ac = np.array([s.contact_area for s in simus])
hmax = np.array([s.max_disp for s in simus])
phi = np.array([s.indenter_half_angle for s in simus])
wirr_wtot = np.array([s.irreversible_work_ratio for s in simus])

# Building secondary data
ey = sy / E
H = C / Ac
hch = (Ac / (np.pi * np.tan(np.radians(phi))**2))**.5

# Building Delaunay triangular connectivity
x = ey
y = n
points = np.array([x, y]).transpose()
conn = Delaunay(points).vertices

# For checking purpose, let's plot the generated mesh. You may see that the mesh is self improving has the simulations complete (this is quite nice).


# Ploting stuff
title = 'Playing with Hollomon law'

X, xlabel = C, r'$C$'
#X, xlabel = ey, r'$\sigma_{yc}/E$'
#X, xlabel = wirr_wtot, r'$W_{irr}/W_{tot}$'
Y, ylabel = hch, '$\sqrt{A_c / A_{app}}$'
#Y, ylabel = C, '$C/E$'

Z, zlabel = n, r'$n = %1.1f$'
Zlevels = list(set(Z))
Z2, z2label = ey, r'$\epsilon_y = %1.3f$'
Z2levels = list(set(Z2))

# For checking purpose, let's plot the generated mesh. You may see that the mesh is self improving has the simulations complete (this is quite nice).

fig = plt.figure(0)
plt.clf()
fig.add_subplot(121)
plt.triplot(x, y, conn)
plt.title('Delaunay Mesh')
plt.xlabel('x')
plt.ylabel('y')
fig.add_subplot(122)
plt.triplot(X, Y, conn)
plt.title('Deformed Delaunay Mesh')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('plots/basic_plot_mesh_Hol.pdf')

plt.figure(0)
plt.clf()
plt.title(title)
plt.grid()
plt.xlabel(xlabel)
plt.ylabel(ylabel)
# plt.triplot(X,Y,conn)
#plt.tricontourf(X,Y,conn,Z, Zlevels)
cont = plt.tricontour(X, Y, conn, Z, Zlevels, colors='blue')
plt.clabel(cont, fmt=zlabel, fontsize=9, inline=1)
cont = plt.tricontour(X, Y, conn, Z2, Z2levels, colors='red')
plt.clabel(cont, fmt=z2label, fontsize=9, inline=1)
plt.savefig('plots/basic_plot_Hol.pdf')

'''
#--------------------------
# PLOTING SECTIONS
#--------------------------
plt.figure(0)
plt.clf()
plt.gca().set_aspect('equal')
rmax = 6.
x = np.linspace(0., rmax, 128)
y = np.zeros_like(x)
ey = np.array(list(set(ey)))
ey.sort()
for s in simus:
  cd = s.contact_data[2][-1]
  alt, press = cd.interpolate(x, y, method = 'linear')
  ey_s = s.sample_mat_args['yield_stress']
  loc = np.where(ey==ey_s)[0][0]
  alt += -loc 
  plt.plot(x, alt)
plt.show()
'''
