'''
Miscellaneous
=============
'''

import pickle
import copyreg
import array


def array_unpickler(data):
    x = array.array(data[0])
    # x.fromstring(data[1:].encode())
    x.frombytes(data[1:].encode('utf-8'))
    return x


def array_pickler(arr):
    return array_unpickler, ("%s%s" % (arr.typecode, arr.tostring()),)


copyreg.pickle(array.ArrayType, array_pickler, array_unpickler)


def load(name):
    '''
    Loads back a pickled object.

    :param name: file name or path to file.
    :type name: string
    :rtype: unpickled object

    .. note:: This function allows clean array unpickling whereas standard ``pickle.load`` will raise an error if ``array.array`` are in the pickled object (which is the case of all objects in Abapy).
    '''
    f = open(name, 'rb')
    out = pickle.load(f)
    f.close()
    return out


def dump(data, name, protocol=2):
    '''
    Dumps an object to file using ``pickle``.

    :param data: object to dump.
    :type data: any
    :param name: file name or path to file.
    :type name: string

    .. note:: This function allows clean array pickling whereas standard ``pickle.dump`` will raise an error if ``array.array`` are in the pickled object (which is the case of all objects in Abapy).
    '''
    f = open(name, 'wb')
    pickle.dump(data, f, protocol)
    f.close()


def read_file(path, ncol=2, separator=None):
    """
    Read a tabular data file and returns a `numpy.array` containing the data. Header lines must begin with a #.
    """
    import numpy as np
    lines = open(path, "rb").readlines()
    out = []
    for line in lines:
        if line[0] != "#":
            ldata = []
            words = line.split()
            for i in range(ncol):
                ldata.append(float(words[i]))
            out.append(ldata)
    return np.array(out).transpose()
