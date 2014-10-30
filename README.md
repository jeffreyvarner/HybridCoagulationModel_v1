____________________________________________________
#### Hybrid extrinsic coagulation model
____________________________________________________
#####author: jdv27@cornell.edu (Jeffrey Varner)
#####location: [Varnerlab](http://www.varnerlab.org), Cornell University
#####version: 1.0
____________________________________________________

######How do we execute the simulation code?
Simulation code is executed using Main.py. Main.py will execute the simulation specified in a simulation file, using parameters specified in a parameter file. 
Main.py takes three command line arguments:
-i Relative or absolute path to the simulation input file. This file is a *.json file which specifies which simulations you want to run. Each simulation corresponds to a function in Simulation.py
-p Relative or absolute path to the parameter ensemble file (text file where each column is a parameter set).
-o Relative or absolute directory where the simulation files will be written. Simulations files are text files, where the first column is time and the remaining cols are model states. Each row is a time point.