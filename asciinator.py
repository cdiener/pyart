#!/usr/bin/env python

#  asciinator.py
#  
#  Copyright 2014 Christian Diener <ch.diener@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from __future__ import print_function		# for python2 compat

import sys; 
from PIL import Image; 
import numpy as np

# ascii chars sorted by "density"
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

# check command line arguments
if len(sys.argv) != 4: 
	print( 'Usage: asciinator.py image scale factor' )
	sys.exit()

# set basic program parameters 
# f = filename, SC = scale, GCF = gamma correction factor, WCF = width correction factor	
f, SC, GCF, WCF = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), 7/4

# open, scale and normalize image by pixel intensities
img = Image.open(f)
S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
img = np.sum( np.asarray( img.resize(S) ), axis=2)
img -= img.min()
img = (1.0 - img/img.max())**GCF*(chars.size-1)

# Assemble and print ascii art
print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) ) )
