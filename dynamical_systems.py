from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from example_systems import lorenz_rhs

class dynamical_system:
    def __init__(self,system_variable_names,parameter_names,local_derivative_functions):
        """A continuous-time dynamical system. This class is directed toward quick integration of single trajectories.

        Args:
            system_variable_names (list of str): Ordered list of the "system variables" (x, y, z, etc)
            parameter_names (list of str): Ordered list of the "parameter variables" or "constants" (rho, beta, alpha)
            local_derivative_functions (callable function): t must be the first variable that you input, then a 
                vector of system-variable values, then each parameter. So, the total number of inputs is (1 float for 
                time) + (1 array for the system variables) + len(parameter_names)
        """
        self.variable_symbols = system_variable_names
        self.parameter_symbols = parameter_names
        self.equations_of_motion = local_derivative_functions
        self.implicit_time = 0
        self.current_var_vals = None
        self.current_param_vals = None
    def set_state(self,y):
        self.current_var_vals = y
    def evolve_single(self,t,y=None,parameters =None):
        """Generates a single trajectory with an unchanging set of parameters.

        Args:
            t (array of floats): The times for which to solve the equations of motion.
            y (array of floats, optional): The initial condition (same length as self.variable_symbols). Defaults to self.current_var_vals.
            params (array of floats, optional): [description]. Defaults to self.current_param_vals.
        """
        if type(y) == type(None):
            y=self.current_var_vals
        if type(parameters) == type(None):
            parameters = self.current_param_vals
        trajectory = odeint(self.equations_of_motion,y,t,args=parameters,tfirst=True)
        self.current_var_vals = trajectory[-1]
        self.current_param_vals = parameters
        return trajectory




'''
lorenz_sys = dynamical_system(['x','y','z'],['sigma','rho','beta'],lorenz_rhs)
integ_times = np.linspace(0,200,50000)
trajectory = lorenz_sys.evolve_single(integ_times,np.array([1,1,1]),(10.,28.,8./3.))
xs = trajectory[:,0]
ys = trajectory[:,1]
zs = trajectory[:,2]

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
plt.plot(xs,ys,zs=zs)
plt.show()
'''