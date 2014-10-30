____________________________________________________
#### Hybrid extrinsic coagulation model
____________________________________________________
#####author: jdv27@cornell.edu (Jeffrey Varner)
#####location: [Varnerlab](http://www.varnerlab.org), Cornell University
#####version: 1.0
____________________________________________________

#####How do we execute the simulation code?
The model code is executed using Main.py. Main.py will execute the simulation specified in a simulation file, using parameters specified in a parameter file. 

Main.py takes three command line arguments:
* __-i__ Relative or absolute path to the simulation input file. This file is a *.json file which specifies which simulations you want to run. Each simulation corresponds to a function in Simulation.py
* __-p__ Relative or absolute path to the parameter ensemble file (text file where each column is a parameter set).
* __-o__ Relative or absolute directory where the simulation files will be written. Simulations files are text files, where the first column is time and the remaining cols are model states. Each row is a time point.

######Example
python Main.py -i ./Simulations_Fig3-BM-1999.json -p ./Ensemble.dat -o ./results

#####What gets generated by the simulation?
The simulation will write simulation files (text files where the first column is time and the remaining cols are model states) of the form SIM_P__parameter-set-index__E__experiment-index___.dat to the directory
specified in the -o command line argument. 

* __parameter-set-index__ is the parameter ensemble member (column index) used for the simulation, starting from 0 (first column of the ensemble file). 
* __experiment-index__ is the index of the particular simulation specification encoded in the JSON simulation file. The simulations are numbered from top to bottom starting from 0.