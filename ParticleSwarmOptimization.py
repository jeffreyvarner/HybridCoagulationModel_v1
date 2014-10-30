import json
import random
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import OptimizeResult
import CoagulationModelFactory as ModelFactory
from Objective import calculateObjectiveFunction
from PSOUtilities import *

# Algorithm parameters -
NUMBER_OF_PARTICLES = 20
MAX_NUMBER_OPERATIONS = 1200
OMEGA = 1.0
ALPHA = 0.05564
BETA = 0.02886

# Build the default model data structure -
PROBLEM_DICTIONARY = dict()
PROBLEM_DICTIONARY = ModelFactory.buildCoagulationModelDictionary()

# Do we want to exclude any of the parameters?
#EXCLUDE_LIST = [0,1,2,3,7,8,9,10,13,14,15,16,19,20]
#EXCLUDE_LIST = [4,5,6,11,12,17,18,21,22]
#EXCLUDE_LIST = [4,5,6,11,12,17,18,21,22,0,1,2,3,7,9,10,13,14,15,16,19,20]
EXCLUDE_LIST = []

# Build the experimental data structure -
path_to_json_file = './Simulations_Fig3-Butenas-2002.json'
json_data = open(path_to_json_file)
data = json.load(json_data)
json_data.close()

list_of_experiments = data['list_of_experiments']
for experiment in list_of_experiments:
    
    # Load the experimental data -
    path_to_experimental_data = str(experiment['path_to_experimental_data_file'])
    data_array = np.loadtxt(path_to_experimental_data)
    
    # Add to the dictionary -
    experiment['measurement_data'] = data_array
    
    
# Create the initial parameter guess -
    
# Initialize a population of particles, each with a different parameter guess
recycle_parameter_array = np.loadtxt('./Fig3_Butenas_R1.json.dat')
(number_of_parameters,local_number_prev_particles) = np.shape(recycle_parameter_array)
particle_array = []
for particle_index in range(0,NUMBER_OF_PARTICLES):
    
    # Create new parameter vector -
    parameter_vector = []
    initial_parameter_guess = recycle_parameter_array[:,particle_index]
    velocity_vector = np.zeros(number_of_parameters);
    
    
    
    # Fill the parameter vector with randomized parameters
    for parameter_index in range(0,number_of_parameters):
        
        old_value = initial_parameter_guess[parameter_index]
        
        if (parameter_index in EXCLUDE_LIST):
            parameter_vector.append(abs(old_value))
        else:
            new_value = random.gauss(old_value,0.01*old_value)
            parameter_vector.append(abs(new_value))
        
    # Evaluate this vector -
    particle_error = calculateObjectiveFunction(parameter_vector,list_of_experiments,PROBLEM_DICTIONARY)
    
    # Store these values in a particle dictionary -
    particle_dictionary = dict()
    particle_dictionary['particle_position'] = np.array(parameter_vector)
    particle_dictionary['particle_velocity'] = np.array(velocity_vector)
    particle_dictionary['particle_error'] = particle_error
    particle_dictionary['particle_index'] = particle_index
    particle_dictionary['best_particle_position'] = np.array(parameter_vector)
    particle_dictionary['best_particle_error'] = particle_error
    particle_dictionary['global_best_particle_position'] = np.array(parameter_vector)
    particle_dictionary['global_best_particle_error'] = particle_error
    
    print "Initialize particle "+str(particle_index)+" has error:"+str(particle_error)
    
    # Put this particle into our array -
    particle_array.append(particle_dictionary)

(best_particle_position,best_error_value) = findGlobalBestParticle(particle_array)
for particle in particle_array:
    particle['global_best_particle_position'] = best_particle_position
    particle['global_best_particle_error'] = best_error_value

for operation_index in range(0,MAX_NUMBER_OPERATIONS):
    
    for particle in particle_array:
        
        # Get data for this particle -
        current_velocity = particle['particle_velocity']
        current_position = particle['particle_position'] 
        best_current_position = particle['best_particle_position']
        global_best_particle_position =  particle['global_best_particle_position']

        # Generate two random numbers -
        rP = random.uniform(0,1)
        rG = random.uniform(0,1)

        # Update the data for this particle -
        velocity = OMEGA*current_velocity + ALPHA*rP*(best_current_position - current_position) + BETA*rG*(global_best_particle_position - current_position)
        position = current_position + velocity
        
        # Fill the parameter vector with randomized parameters
        for parameter_index in range(0,number_of_parameters):
        
            old_value = initial_parameter_guess[parameter_index]
        
            if (parameter_index in EXCLUDE_LIST):
                position[parameter_index] = old_value
            else:
                position[parameter_index] = position[parameter_index] + velocity[parameter_index]
        
        particle['particle_velocity'] = velocity
        particle['particle_position'] = position

        # Evaluate the error for this particle -
        new_particle_error = calculateObjectiveFunction(position,list_of_experiments,PROBLEM_DICTIONARY)
        current_particle_error = particle['particle_error']
        best_particle_error = particle['best_particle_error']
        global_best_particle_error =  particle['global_best_particle_error']
        
        # Ok, is this error better than my *best* local error?
        if (new_particle_error < current_particle_error):
            
            # update the user -
            print "Found new local best error ",str(new_particle_error)," (global_best:",str(global_best_particle_error),") from particle ",str(particle['particle_index'])," operation:",str(operation_index)
            
            # We found a better solution *at least* locally -
            particle['particle_error'] = new_particle_error
            particle_dictionary['best_particle_position'] = position
            particle['best_particle_error'] = new_particle_error
        
            # Is this solution better than our global best?
            if (new_particle_error<global_best_particle_error):
                
                # update the user -
                print "Found *new global best error* ",str(new_particle_error)," from particle ",str(particle['particle_index'])," operation:",str(operation_index)
                
                # we found a new global best, update all particles 
                for particle in particle_array:
                    particle['global_best_particle_position'] = position
                    particle['global_best_particle_error'] = new_particle_error

                # we found new global best, write the particles to disk -
                writeParticleArrayToFileWithPath("./Fig3_Butenas_R2.dat",particle_array)

# Ok, we exhasuted our operations, write the particles to disk -
writeParticleArrayToFileWithPath("./Fig3_Butenas_R2.dat",particle_array)             
                    