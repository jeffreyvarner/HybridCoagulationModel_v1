__author__ = 'jeffreyvarner'
__version__ = '1.0'

# imports -
import sys
import os
import argparse
import numpy as numpy_object
import json
import CoagulationModelFactory as ModelFactory
from Objective import calculateObjectiveFunction
from PSOUtilities import *
from Simulations import *
import pdb


def doSampleMyEnsembleOfParticles(path_to_particle_file, path_to_json_file, simulation_results_directory):

    # Load array of parameters from particle collection
    parameter_array = numpy_object.loadtxt(path_to_particle_file)
    (number_of_parameters, number_of_particles) = numpy_object.shape(parameter_array)

    # Build the default model data structure -
    PROBLEM_DICTIONARY = dict()
    PROBLEM_DICTIONARY = ModelFactory.buildCoagulationModelDictionary()

    # pdb.set_trace()

    # Build the experimental data structure -
    json_data = open(path_to_json_file)
    data = json.load(json_data)
    json_data.close()

    # ok, before we start the simulation loop, we need to check to see if the output directory exsists -
    if not os.path.exists(simulation_results_directory):
        os.makedirs(simulation_results_directory)

    list_of_experiments = data['list_of_experiments']
    number_of_experiments = len(list_of_experiments)

    for experiment_index in range(0, number_of_experiments):

        experiment = list_of_experiments[experiment_index]
        experimental_model_name = experiment['experimental_simulation_model']

        for particle_index in range(0, number_of_particles):

            # get parameters -
            parameter_guess = parameter_array[:, particle_index]

            # Update the problem definition -
            number_kinetic_parameters = 9
            number_control_parameters = 14
            kinetic_parameter_vector = []
            for index in range(0, number_kinetic_parameters):
                kinetic_parameter_vector.append(abs(parameter_guess[index]))

            control_parameter_vector = []
            for index in range(number_kinetic_parameters, number_of_parameters):
                control_parameter_vector.append(abs(parameter_guess[index]))

            PROBLEM_DICTIONARY['KINETIC_PARAMETER_VECTOR'] = kinetic_parameter_vector
            PROBLEM_DICTIONARY['CONTROL_PARAMETER_VECTOR'] = control_parameter_vector

            # Construct the command -
            cmd = str(experimental_model_name) + "(PROBLEM_DICTIONARY)"

            #pdb.set_trace()

            # Evaluate the experimental model -
            (TSIM, XSIM) = eval(cmd)

            # Build paths for output, write simulation to a file -
            path_to_simulation_output_file = str(simulation_results_directory) + '/SIM_P'+str(particle_index)+'E'+str(experiment_index)+'.dat'
            writeSimulationArrayToFileWithPath(path_to_simulation_output_file, TSIM, XSIM)


# my main method - reads the path to the particle file, and the simulation JSON file
def main(argv):

    # Parse the input arguments -
    arg_parser = argparse.ArgumentParser(
        description='Execute simulation encoded in *.json file with parameters in a particle file.')
    arg_parser.add_argument('-i', '--simulation-file-input-path', type=str, required=True,
                            help='Path to simulation input file')
    arg_parser.add_argument('-p', '--parameter-file-input-path', type=str, required=True,
                            help='Path to parameter input file')
    arg_parser.add_argument('-o', '--simulation-output-directory', type=str, required=True,
                            help='Path to model output directory')
    args_list = arg_parser.parse_args(argv[1:])

    # Get the paths -
    path_to_json_file = args_list.simulation_file_input_path
    path_to_particle_file = args_list.parameter_file_input_path
    simulation_results_directory = args_list.simulation_output_directory

    # Call the sample method, write the results to disk -
    doSampleMyEnsembleOfParticles(path_to_particle_file,path_to_json_file,simulation_results_directory)

# Boiler plate code for launching main -
if __name__ == '__main__':
    main(sys.argv)