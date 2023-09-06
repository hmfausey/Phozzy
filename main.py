# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:10:00 2022

@author: hmfausey

This is an example main for how to run the code
"""

import os

import phozzy

import numpy as np

##If

if __name__ == "__main__":
    ##Define parameters for the simulation
    
    #Edges of photometric bands
    filter_edges = np.array([[0.5, 0.64], [0.64, 0.87], [0.87, 1.2], [1.2, 1.7], [1.7, 2.4]])

    #string that will proceed all output files for this run
    save_string = 'test_run'
    
    #Number of GRBs to be simulated and fit
    nGRBs = 500
    
    phozzy.phozzy(nGRBs, filter_edges, save_string, parallel = True, nwalkers=50, burnin=250, produc=500)






