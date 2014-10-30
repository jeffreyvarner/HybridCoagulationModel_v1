import numpy as numpy_object


# === Helper methods =================================
def writeSimulationArrayToFileWithPath(simulation_array_path,time_array,simulation_array):
    
    # initialize -
    (number_of_timesteps,number_of_species) = numpy_object.shape(simulation_array)
    
    # Create data array -
    data_array = numpy_object.empty((number_of_timesteps,number_of_species + 1))
    
    # Add the time to the first col (index 0) of data_array -
    for time_index in range(0,number_of_timesteps):
        data_array[time_index][0] = time_array[time_index]
    
    for row_index in range(0,number_of_timesteps):
        
        for col_index in range(1,number_of_species + 1):
            
            data_array[row_index][col_index] = simulation_array[row_index][col_index - 1]
            
    # write the array to a file -
    numpy_object.savetxt(simulation_array_path,data_array)
    
    
def writeParticleArrayToFileWithPath(particle_array_path,particle_array):
    
    # initialize -
    number_of_particles = len(particle_array)
    
    # Inspect the array to the number of parameters -
    number_of_parameters = len(particle_array[0]['best_particle_position'])
    parameter_array = numpy_object.empty((number_of_parameters,number_of_particles))
    
    
    for particle_index in range(0,number_of_particles):
        
        parameter_vector = particle_array[particle_index]['best_particle_position']
        
        for parameter_index in range(0,number_of_parameters):
        
            value = parameter_vector[parameter_index]
            parameter_array[parameter_index][particle_index] = value
        
        
    # write the array to a file -
    numpy_object.savetxt(particle_array_path,parameter_array)

def findGlobalBestParticle(particle_array):
    
    number_of_particles = len(particle_array)
    best_error_value = 1e14
    best_particle_position = []
    for particle in particle_array:
        
        local_error_value = particle['particle_error']
        
        if (local_error_value<best_error_value):
            best_particle_position = particle['particle_position']
            best_error_value = local_error_value
        
    return (best_particle_position,best_error_value)