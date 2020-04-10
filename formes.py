#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:14:39 2020

@author: erictixidor
"""
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

def plot_rectangle(vtx, size=5, color='black'):
    """plot a rectangle with matplotlib
    vtx : list of vertices [[x1,y1], [x2,y2], ...]
    size : dim figure 
    color : default = black
    """
    fig1 = plt.figure(1, figsize=(0.5,0.5))
    ax1 = fig1.add_subplot(111)
    # Create a rectangle. Size defined as lower left coordinates + width
    # + height
    for v in vtx:
      x0,y0 = v
      width = 1
      height = 1
      rectangle = ptc.Rectangle(
        (x0, y0),
        width,
        height,
        # Color option, alpha to play with transparency
        color=color, alpha=1.0,
        # Option to handle patches overlapping.
        zorder=0
        )
      # Add the rectangle patch to the plot
      ax1.add_artist(rectangle)
 
    # Set axis limits to see something
    
    ax1.set_xlim((0, 10))
    ax1.set_ylim((0, 10))
  
    ax1.set_yticklabels([]) # on retire la graduation des x
    ax1.set_xticklabels([]) # on retire la graduation des y
    
    ax1.grid(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    
    
    
    ax1.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom Edge are off
    top=False,       # ticks along the top Edge are off
    left=False,
    labelbottom=False) # labels along the bottom Edge are off
    
    
    fig1.savefig('dessin1.png')
    plt.show()
    
    
    
    
    # Create a figure and a 'plot' inside it.
    fig = plt.figure(1, figsize=(size,size))
    ax = fig.add_subplot(111)
    # Create a rectangle. Size defined as lower left coordinates + width
    # + height
    for v in vtx:
      x0,y0 = v
      width = 1
      height = 1
      rectangle = ptc.Rectangle(
        (x0, y0),
        width,
        height,
        # Color option, alpha to play with transparency
        color=color, alpha=1.0,
        # Option to handle patches overlapping.
        zorder=0
        )
      # Add the rectangle patch to the plot
      ax.add_artist(rectangle)
 
    # Set axis limits to see something
    
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))
  
    ax.set_yticklabels([]) # on retire la graduation des x
    ax.set_xticklabels([]) # on retire la graduation des y
    
    ax.grid(True)
    plt.show()
    
def plot_rectangle_gris(vtx, color='black'):
    """plot a rectangle with matplotlib
    vtx : list of vertices [(x1,y1), (x2,y2), ...]
    """
    # Create a figure and a 'plot' inside it.
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    # Create a rectangle. Size defined as lower left coordinates + width
    # + height
    #x0, y0 = vtx[0]
    for v in vtx:
      x0,y0 = v[0],v[1]
      width = 1
      height = 1
      col=plt.cm.gray(v[2]/255)
      #width = vtx[2][0] - vtx[0][0]
      #height = vtx[2][1] - vtx[0][1]
      rectangle = ptc.Rectangle(
        (x0, y0),
        width,
        height,
        # Color option, alpha to play with transparency
        #color=0.8, alpha=1.0,
        color=col, alpha=1.0,
        # Option to handle patches overlapping.
        zorder=0
        )
      # Add the rectangle patch to the plot
      ax.add_artist(rectangle)
 
    # Set axis limits to see something
    
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))
    ax.grid(True)
    ax.set_yticklabels([]) # on retire la graduation des x
    ax.set_xticklabels([]) # on retire la graduation des y
    plt.show()
    fig.savefig('dessin2.png')