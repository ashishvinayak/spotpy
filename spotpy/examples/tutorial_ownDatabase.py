'''
Copyright 2015 by Tobias Houska
This file is part of Statistical Parameter Estimation Tool (SPOTPY).

:author: Tobias Houska

This example implements the Rosenbrock function into SPOT.  
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import numpy as np
import spotpy

        
class spot_setup(object):
    slow = 1000
    def __init__(self):
        self.params = [spotpy.parameter.List('x',[1,2,3,4,6,7,8,9,0]), #Give possible x values as a List
                       spotpy.parameter.List('y',[0,1,2,5,7,8,9,0,1])]  #Give possible y values as a List
                       
        self.database = file('MyOwnDatabase.txt','w')
        
    def parameters(self):
        return spotpy.parameter.generate(self.params)
        
    def simulation(self,vector):
        x=np.array(vector)
        for i in range(self.slow):
            s = np.sin(i)
        simulations= [sum(100.0*(x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)]
        return simulations
        
    def evaluation(self):
        observations = [0]
        return observations
    
    def objectivefunction(self,simulation,evaluation):
        objectivefunction = -spotpy.objectivefunctions.rmse(evaluation = evaluation,simulation = simulation)      
        return objectivefunction
        
    def save(self, objectivefunctions, parameter, simulations):
        line=str(objectivefunctions)+','+str(parameter).strip('[]')+','+str(simulations).strip('[]')+'\n'
        self.database.write(line)
        
spot_setup=spot_setup()
'Leave out dbformat and dbname and spotpy will return results in spot_setup.save function'
sampler=spotpy.algorithms.mc(spot_setup) 
sampler.sample(10) #Choose equaly or less repetitions as you have parameters in your List
spot_setup.database.close() # Close the created txt file