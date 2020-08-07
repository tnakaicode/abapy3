from abapy.postproc import FieldOutput, VectorFieldOutput
data1 = [1, 2, 3, 5, 6, 0]
data2 = [1. for i in data1]
labels = range(1, len(data1) + 1)
fo1, fo2 = FieldOutput(labels=labels, data=data1, position='node'), FieldOutput(
    labels=labels, data=data2, position='node')
vector = VectorFieldOutput(data1=fo1, data2=fo2)
vector2 = VectorFieldOutput(data2=fo2)
vector  # short description
print(vector)  # long description
print(vector[6])  # Returns a VectorFieldOutput instance
print(vector[1, 4, 6])  # Picking label by label
print(vector[1:6:2])  # Slicing
print(vector.get_data(6))  # Returns 3 floats
print(vector.norm())  # Returns norm
print(vector.sum())  # returns the sum of coords
print(vector * vector2)  # Itemwise product (like numpy, unlike matlab)
print(vector.dot(vector2))  # Dot/Scalar product
print(vector.cross(vector2))  # Cross/Vector product
print(vector + 2)  # Itemwise addition
print(vector * 2)  # Itemwise multiplication
print(vector)  # Itemwise division
# print(vector / vector2)  # Itemwise division between vectors (numpy way)
# print(abs(vector))  # Absolute value
# print(vector ** 2)  # Power
# print(vector ** vector)  # Itemwize power
