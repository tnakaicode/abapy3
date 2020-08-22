import numpy as np
import pickle
import copyreg
import array

import sys
print(sys.getdefaultencoding())

#x = array.array('c', 'test')
x = array.array('b')
x.fromstring("test")
x.tobytes()
x.tobytes().decode()
x.frombytes('test'.encode())
x.tobytes()
x.tobytes().decode()

fp = open("ContactData_berk.pckl", "rb")
dat = pickle.load(fp)
print(dat)
