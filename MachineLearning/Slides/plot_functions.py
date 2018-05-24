#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 21:40:56 2018

@author: emmascala

"""

def make_plot(x_name,x_axis,y_data,y_pred,cont):
    """ >>> make_plot(x_name,x_axis,y_data,y_train,cont)
    (str,array,array,array) --> plot
    Make scatter plot of the following:
    X-axis is variable 1 and 2
    Y-axis is life expectancy
    colour of point is continent
    point style o = real data, x = country or continent
    Label the plot with colour and symbol style
    """    
    
    import matplotlib.pyplot as plt
    # colour map
    plt.figure(figsize=(12,8))
    cmap = plt.get_cmap('nipy_spectral', lut = 5)
    continents = {0:'Africa',1:'Americas',2:'Asia',3:'Europe',4:'Oceania'}
    formatter = plt.FuncFormatter(lambda val, loc: continents[val])
    
    #plot data
    plt.scatter(x_axis,y_data, c = cont, cmap = cmap, marker = 'o', label = 'Data',vmin = 0)
    if y_pred.any:
        plt.scatter(x_axis,y_pred, c = cont, cmap = cmap,marker = 'x', label = 'Prediction',vmin = 0)
    #Titles
    plt.title('Life expectancy vs.' + x_name)
    plt.xlabel(x_name)
    plt.ylabel('Life expectancy')
    #color bar
    plt.colorbar(ticks = [0,1,2,3,4,5], format = formatter)
    plt.clim(-0.5, 4.5)
    #legend
    plt.legend(loc = 'lower right')
    plt.show()
