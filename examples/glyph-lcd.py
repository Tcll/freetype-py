# -----------------------------------------------------------------------------
#
#  FreeType high-level python API - Copyright 2011 Nicolas P. Rougier
#  Distributed under the terms of the new BSD license.
#
# -----------------------------------------------------------------------------
'''
Glyph bitmap monochrome rendring
'''
from freetype import *

def bits(x):
    data = []
    for i in range(8):
        data.insert(0, int((x & 1) == 1))
        x = x >> 1
    return data

if __name__ == '__main__':
    import numpy
    import matplotlib.pyplot as plt

    face = Face('./arial.ttf')
    face.set_char_size( 48*64 )
    face.load_char('S', FT_LOAD_RENDER |
                        FT_LOAD_TARGET_LCD )
    bitmap = face.glyph.bitmap
    width  = face.glyph.bitmap.width
    rows   = face.glyph.bitmap.rows
    pitch  = face.glyph.bitmap.pitch
    
    data = []
    for i in range(rows):
        data.extend(bitmap.buffer[i*pitch:i*pitch+width])
    Z = numpy.array(data,dtype=numpy.ubyte).reshape(rows, width/3, 3)
    plt.imshow(Z, interpolation='nearest')
    plt.show()