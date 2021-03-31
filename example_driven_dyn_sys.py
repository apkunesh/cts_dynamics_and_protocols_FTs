from driven_dynamical_systems import driven_dynamical_system
from example_systems import lorenz_rhs
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import random


var_names = ['x','y','z']
param_names = ['sigma','rho','beta']

t_indexed_paramshifts = np.array([
    [0,(10.,28.,8./3.)],
    [200,(10.,100.,8./3.)],
    [400,(10.,14,8./3.)]
]) # first element is time, second is a tuple of values for the parameters

initial_condition = [1,1,1] #state variables
dt = .001

my_driven_system = driven_dynamical_system(var_names,param_names,lorenz_rhs,t_indexed_paramshifts,600)
all_data_out = my_driven_system.execute_protocol(initial_condition,dt)

fig=plt.figure()
ax = plt.axes(projection='3d')
for trajectory_data in all_data_out[1]:
    xs = trajectory_data[:,0]
    ys = trajectory_data[:,1]
    zs = trajectory_data[:,2]
    plt.plot(xs,ys,zs=zs)
plt.show()