import numpy as np

def lorenz_rhs(t,y_vec,sigma,rho,beta):
    """Returns the rates of change of the three Lorenz system variables for a given position in phase space
    and set of parameters.

    Args:
        t (array of floats): Necessary baggage for integration, as the Lorenz is time-independent
        y_vec (array of floats): The state of the system, expressed as an array of length 3
        parameters (tuple of floats): Values for the parameters sigma, rho, and beta.
    """
    if  len(y_vec)!=3:
        print('Error: wrong number of current position values, ' + str(len(y_vec)))
    [x,y,z] = y_vec
    x_deriv = sigma*(y-x)
    y_deriv = x*(rho-z)-y
    z_deriv = x*y-beta*z
    return np.array([x_deriv,y_deriv,z_deriv])