import numpy as numpy_object
import json
import CoagulationModelFactory as ModelFactory
from Objective import calculateObjectiveFunction
from PSOUtilities import *
from Simulations import *
import pdb

# Load array of parameters from particle collection
path_to_particle_file = './Fig5A_R19.dat'
parameter_array = numpy_object.loadtxt(path_to_particle_file)
(number_of_parameters,number_of_particles) = numpy_object.shape(parameter_array)

# Build the default model data structure -
PROBLEM_DICTIONARY = dict()
PROBLEM_DICTIONARY = ModelFactory.buildCoagulationModelDictionary()

#pdb.set_trace()

# Build the experimental data structure -
path_to_json_file = './Simulations-rFVIIa-HvsN.json'
json_data = open(path_to_json_file)
data = json.load(json_data)
json_data.close()

list_of_experiments = data['list_of_experiments']
number_of_experiments = len(list_of_experiments)

for experiment_index in range(0,number_of_experiments):
    
    experiment = list_of_experiments[experiment_index]
    experimental_model_name = experiment['experimental_simulation_model']
    
    for particle_index in range(0,number_of_particles):
        
        # get parameters -
        parameter_guess = parameter_array[:,particle_index]
        
        # Update the problem definition -
        number_kinetic_parameters = 9
        number_control_parameters = 14
        kinetic_parameter_vector = []
        for index in range(0,number_kinetic_parameters):
            kinetic_parameter_vector.append(abs(parameter_guess[index]))
    
        control_parameter_vector = []
        for index in range(number_kinetic_parameters,number_of_parameters):
            control_parameter_vector.append(abs(parameter_guess[index]))
    
        PROBLEM_DICTIONARY['KINETIC_PARAMETER_VECTOR'] = kinetic_parameter_vector
        PROBLEM_DICTIONARY['CONTROL_PARAMETER_VECTOR'] = control_parameter_vector
        
        # Construct the command -
        cmd = str(experimental_model_name)+"(PROBLEM_DICTIONARY)"
        
        #pdb.set_trace()
        
        # Evaluate the experimental model -
        (TSIM,XSIM) = eval(cmd)
        
        # Build paths for output, write simulation to a file -
        path_to_simulation_output_file = './results/SIM_P'+str(particle_index)+"E"+str(experiment_index)+".dat"
        writeSimulationArrayToFileWithPath(path_to_simulation_output_file,TSIM,XSIM)
