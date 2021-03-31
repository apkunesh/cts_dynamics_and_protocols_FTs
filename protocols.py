import numpy as np

class protocol:
    def __init__(self,parameter_names,time_indexed_paramshifts,end_time):
        """A list of stepwise changes to the parameters of a dynamical system over some time interval. To be used
        in protocol_driven_dynamical_system. By default, we start at the 0th index of the protocol.

        Args:
            parameter_names (list of strings): Ordered list of the names of the parameters, for display purposes
            time_indexed_paramshifts (array like [t,[p0,p1,p2]]): An array of "keyframes" for what all the values
                of the parameters at each "key" time.
        """
        self.shift_times = time_indexed_paramshifts[:,0]
        self.all_params = time_indexed_paramshifts[:,1]
        self.parameter_symbols = parameter_names
        self.current_params = self.all_params[0]
        self.current_region = 0
        self.previous_time = None
        self.final_time = end_time
    
    def get_times(self):
        return self.shift_times
    
    def get_params(self):
        return self.all_params
    
    def detect_paramchange(self,t_final): 
        """Checks whether or not the referenced time lies inside or outside the current timeframe for the
        current parameter settings.

        Args:
            t_final (float): The query time

        Returns:
            Bool: False if the query time is inside the current timeframe, otherwise True.
        """
        id1 = np.searchsorted(self.shift_times,t_final)-1
        if id1 != self.current_region:
            return True
        else:
            return False
    def change_params(self,t_change):
        new_param_index = np.searchsorted(self.shift_times,t_change)-1 #finding my new region
        #print(new_param_index)
        self.current_params = self.all_params[new_param_index] #altering the parameters to reflect the shift
        self.current_region = new_param_index #keeping track of my new location in the parameter set

'''
t_indexed_paramshifts = np.array([
    [0,(28.,10.,8./3.)],
    [100,(13.92655742,10.,8./3.)],
    [200,(28.,10.,8./3.)]
])

my_protocol = protocol(['sigma','rho','beta'],t_indexed_paramshifts)
print(my_protocol.detect_paramchange(100.1))
'''