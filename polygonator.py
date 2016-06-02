#!/usr/bin/env python

#  polygonator.py
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

from __future__ import print_function		# for python2 compatibility

import sys, os
from PIL import Image
from numpy import mgrid, vstack, asarray
from matplotlib import use
use("Agg")
from matplotlib.pyplot import scatter, figure, axis, xlim, ylim, savefig, subplots_adjust

# Check for right number of command line arguments
if len(sys.argv) not in [5,6]:
	print( 'Usage: polygonator.py image_file scale spacing plot_obj [background_color]' )
	sys.exit()

# Get command line arguments
f, SCALE, SPACING, OBJ = sys.argv[1:5]
FC = "black"
if len(sys.argv) == 6: FC = sys.argv[5]
SPACING = float(SPACING)
SCALE = float(SCALE)

# resize image by scale and derive size of polygons
img = Image.open(f)
img = img.resize( ( int(img.size[0]*SCALE), int(img.size[1]*SCALE) ) )
size = img.size
img = asarray(img, dtype="float")
inch_scale = size[0]/10.0
msize = 72.0*(1.0-SPACING)/inch_scale

# Build up grid points
X, Y = mgrid[0:(size[0]-1), 0:(size[1]-1)]
Y = Y.max() - Y		# invert y-axis
grid = vstack([X.ravel(), Y.ravel()]).T

# Initialize plot and colors
fig = figure( figsize=(int(size[0]/inch_scale), int(size[1]/inch_scale)) )
axis('off')
xlim((-1,size[0]-1))
ylim((-1,size[1]-1))
cols = [img[ size[1]-1-p[1], p[0], ]/255 for p in grid]

# Draw and save image
scatter( grid[:,0], grid[:,1], marker=OBJ, c=cols, linewidths=0, edgecolors="black", s=msize**2 )
subplots_adjust(left=0, right=1, bottom=0, top=1)
# If you want another image file format or background color you can change it in the
# following line
fig.savefig(os.path.splitext(f)[0]+'_poly.svg', dpi=300, facecolor=FC)
