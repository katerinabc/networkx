#!/usr/bin/env python
"""
Draw a graph with matplotlib, color by degree.
You must have matplotlib for this to work.
"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
__date__ = "$Date: 2005-03-22 13:57:46 -0700 (Tue, 22 Mar 2005) $"
__credits__ = """"""
__revision__ = "$Revision: 831 $"
#    Copyright (C) 2004 by 
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    Distributed under the terms of the GNU Lesser General Public License
#    http://www.gnu.org/copyleft/lesser.html

try:
    from pylab import *
except:
    print "pylab not found: see https://networkx.lanl.gov/Drawing.html for info"
    raise 
    
from networkx import *

G=grid_2d_graph(4,4)  #4x4 grid
pos=spring_layout(G)
draw(G,pos,node_color=array([G.degree(v) for v in G]))
savefig("grid.png") # save as png
show() # display