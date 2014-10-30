import numpy as numpy_object
from Simulations import *
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline

def calculateObjectiveFunction(parameter_guess,list_of_experiments,PROBLEM_DICTIONARY):
    
    # Update the problem definition -
    number_kinetic_parameters = 9
    number_control_parameters = 14
    number_scaling_paramters = 2
    kinetic_parameter_vector = []
    for index in range(0,number_kinetic_parameters):
        kinetic_parameter_vector.append(abs(parameter_guess[index]))
    
    control_parameter_vector = []
    total_length = len(parameter_guess)
    for index in range(number_kinetic_parameters,(number_kinetic_parameters + number_control_parameters)):
        control_parameter_vector.append(abs(parameter_guess[index]))
    
    PROBLEM_DICTIONARY['KINETIC_PARAMETER_VECTOR'] = kinetic_parameter_vector
    PROBLEM_DICTIONARY['CONTROL_PARAMETER_VECTOR'] = control_parameter_vector
    
    # Initialize -
    error_array = []
    
    # Execute the list of experiments, compute error -
    for experiment in list_of_experiments:
        
        # ok, this is an array of experiment dictionarys -
        experimental_data = experiment['measurement_data']
        experimental_model_name = experiment['experimental_simulation_model']
        
        # Construct the command -
        cmd = str(experimental_model_name)+"(PROBLEM_DICTIONARY)"
        
        # Evaluate the experimental model -
        (TSIM,XSIM) = eval(cmd)
        
        # Ok, we need to get the experimental data -
        TEXP = experimental_data[:,0]
        DATA_EXP = experimental_data[:,1]
        
        # Interpolate the simulations onto the experimental time scale -    
        number_of_time_steps = len(TSIM)
        for time_step_index in range(0,number_of_time_steps):
            value = XSIM[time_step_index,1]
            if (numpy_object.isnan(value)):
                XSIM[time_step_index,1] = 0.0
        
        ius = InterpolatedUnivariateSpline(TSIM, XSIM[:,1])
        DATA_SIM = ius(TEXP)
        
        #import pdb; pdb.set_trace()
        
        # Calculate the error for this experiment -
        N = len(TEXP)
        error_local = 0.0
        for time_point in range(0,N):
            value = DATA_EXP[time_point] - DATA_SIM[time_point]
            error_local = error_local + pow(value,2)
    
        # Add the error to my error array -
        error_array.append(error_local)
        
        #import pdb; pdb.set_trace()
    
    total_error_value = numpy_object.sum(error_array)
    #print "Error - ",str(total_error_value)    
    
    
    
    return total_error_value