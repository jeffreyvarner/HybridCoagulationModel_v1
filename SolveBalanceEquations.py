from scipy.integrate import odeint
import numpy as np

def solveBalanceEquations(pBalanceEquations,time_vector,PROBLEM_DICTIONARY):
    
    # Get the initial conditions from the problem dictionary -
    IC = PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'];
    
    # Call the ODE solver =
    XI = odeint(pBalanceEquations,IC,time_vector,args = (PROBLEM_DICTIONARY,),rtol=1e-4,atol=1e-6)
    X = np.absolute(XI);
    
    # return a tuple of time,state array -
    return (time_vector,X)