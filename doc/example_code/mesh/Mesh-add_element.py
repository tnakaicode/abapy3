from abapy.mesh import Mesh, Nodes
mesh = Mesh()
nodes = mesh.nodes
# Adding some nodes
nodes.add_node(label=1, x=0., y=0., z=0.)
nodes.add_node(label=2, x=1., y=0., z=0.)
nodes.add_node(label=3, x=1., y=1., z=0.)
nodes.add_node(label=4, x=0., y=1., z=0.)
nodes.add_node(label=5, x=2., y=0., z=0.)
nodes.add_node(label=6, x=2., y=1., z=0.)
# Adding some elements
mesh.add_element(label=1, connectivity=(1, 2, 3, 4),
                 space=2, name='QUAD4', toset='mySet')
mesh.add_element(label=2, connectivity=(2, 5, 6, 3), space=2,
                 name='QUAD4', toset=['mySet', 'myOtherSet'])
print(mesh)
