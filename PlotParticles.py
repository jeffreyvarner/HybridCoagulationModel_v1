import numpy as np
import math
import matplotlib.pyplot as plt
import json
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import rcParams


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100

# Set fonts -
rcParams['font.family'] = 'sans-serif'
rcParams['font.serif'] = ['Helvetica']
rcParams['text.usetex'] = True

number_of_experiments = 5
number_of_particles = 20
numner_of_timesteps = 600
SIGMA = 2.575

RED_COLOR = [1,0,0]
BLUE_COLOR = [0,0,1]
GREEN_COLOR = [0,1,0]
GREY_COLOR = [0.8,0.8,0.8]
LBLUE_COLOR = [135.0/255.0,206.0/255.0,250.0/255.0]
LGREEN_COLOR = [152.0/255.0,251.0/255.0,152.0/255.0]
ORANGE_COLOR = [244.0/255.0,164.0/255.0,96.0/255.0]

# Build the experimental data structure -
path_to_json_file = './Simulations-rFVIIa-Hemophilia.json'
json_data = open(path_to_json_file)
data = json.load(json_data)
json_data.close()

list_of_experiments = data['list_of_experiments']

experiment_vector = [0,1,2,3,4]
number_of_experiments = len(experiment_vector)
(f, axarr) = plt.subplots(number_of_experiments, sharex=True)
experiment_color_vector = [LBLUE_COLOR,LGREEN_COLOR,ORANGE_COLOR,RED_COLOR,BLUE_COLOR,GREEN_COLOR,GREY_COLOR]
for experiment_vector_index in range(0,number_of_experiments):
	
    # What experiment r we looking at?
    experiment_index = experiment_vector[experiment_vector_index]
    
    # Build simulation array -
    simulation_array = np.empty((numner_of_timesteps,number_of_particles))

    # Load the data for each particle -
    for particle_index in range(0,number_of_particles):
        
        # load data -
        path_to_simulation_file = "./results/SIM_P"+str(particle_index)+"E"+str(experiment_index)+".dat"
        data_array = np.loadtxt(path_to_simulation_file)
        (number_of_timesteps,number_of_states) = np.shape(data_array)

        time_vector = 1.0*data_array[:,0]
        state_vector = 1.0*data_array[:,2]
        
        for row_index in range(0,number_of_timesteps):
            simulation_array[row_index][particle_index] = state_vector[row_index]
            
        
    
    
    # Calculate the M, and STD for this experiment -
    M = np.mean(simulation_array,axis=1)
    STD = np.std(simulation_array,axis=1)
    
    factor = math.sqrt(20)
    UP = M + SIGMA*(1/factor)*STD
    DOWN = abs(M - SIGMA*(1/factor)*STD)
    max_value = roundup(1.2*np.max(UP))
    tick_step = round((max_value)/4)
    
    
    #import pdb; pdb.set_trace()
    color_value = experiment_color_vector[experiment_index]
    
    axarr[experiment_vector_index].plot(time_vector,UP,lw=1,color='k')
    axarr[experiment_vector_index].plot(time_vector,M,lw=2,color='k')
    axarr[experiment_vector_index].plot(time_vector,DOWN,lw=1,color='k')
    axarr[experiment_vector_index].fill_between(time_vector,M,UP,color=color_value,alpha=0.25)
    axarr[experiment_vector_index].fill_between(time_vector,M,DOWN,color=color_value,alpha=0.25)
    axarr[experiment_vector_index].set_xlim([-1,14])
    axarr[experiment_vector_index].set_ylim([0,max_value])
    axarr[experiment_vector_index].yaxis.set_ticks(np.arange(0,max_value+1,tick_step))
    axarr[experiment_vector_index].set_ylabel("Thrombin [nM]",fontsize=12)

    # plot the experimental data corresponding to this experiment -
    path_to_experimental_data_file = list_of_experiments[experiment_index]["path_to_experimental_data_file"]
    D = np.loadtxt(path_to_experimental_data_file)
    axarr[experiment_vector_index].plot(D[:,0],D[:,1],'o',color=color_value)



plt.xlabel("Time [min]",fontsize=16)
plt.savefig("Fig-hemo-rFVIIa.pdf")
plt.show()