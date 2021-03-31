from dynamical_systems import dynamical_system
from protocols import protocol
from example_systems import lorenz_rhs
import numpy as np
from copy import copy

class driven_dynamical_system:
    """A dynamical system which 1) evolves system variables and 2) allows for
    predetermined stepwise changes in the system parameters. Typically used
    to generate single trajectories under a protocol (which specifies at which time
    and to what the system parameters change).
    """
    def __init__(self,system_variable_names,parameter_names,local_derivatives_function,time_indexed_paramshifts,end_time):
        self.system = dynamical_system(system_variable_names,parameter_names,local_derivatives_function)
        self.protocol = protocol(parameter_names,time_indexed_paramshifts,end_time)
        self.end_time = end_time
    def execute_protocol(self,y_0,min_time_between_points = .005): #may, at some point, have to debug integrator time here
        all_shift_times = self.protocol.get_times()
        start_times = all_shift_times
        end_times = np.append(all_shift_times[1:],self.end_time)
        self.system.set_state(y_0)
        all_times = []
        all_trajectory_pieces = []
        for start_time,end_time in zip(start_times,end_times):
            n_datapoints = int(np.ceil((end_time-start_time) / min_time_between_points))
            data_times = np.linspace(start_time,end_time,n_datapoints,endpoint=False)
            self.protocol.change_params((end_time+start_time)/2)
            input(self.protocol.current_params)
            local_trajectory = self.system.evolve_single(data_times,parameters = self.protocol.current_params)
            #input(local_trajectory)
            all_times.append(data_times)
            all_trajectory_pieces.append(local_trajectory)
            #input(all_trajectory_pieces)
        return np.array(all_times),np.array(all_trajectory_pieces)