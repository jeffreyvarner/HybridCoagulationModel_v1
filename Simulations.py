import SolveBalanceEquations as Solver
from BalanceEquations import BalanceEquations
from numpy import *

def simulateFig3Butenas2002(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(12)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    return (TIME+alpha,beta*STATE)
    
    
def simulateFig3HButenas2002(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(12)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)
    

def simulateFig1AAllen2006(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.3)           # 2 FVIII
    qualitative_factor_vector.append(70.0)          # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 120
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIaNormal(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.50)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.7)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*10)       # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)


def simulateFig1BAllenRFVIIa6(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*200)      # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIa5(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*100)      # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIa4(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*50)     # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIa3(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*25)       # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIa2(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*10)       # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIa1(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*2)       # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllenRFVIIa0(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005*1)        # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig1BAllen2006(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3000)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 120
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)




def simulateFig5ABM1999150FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*1.50)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.7)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(5)              # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig5ABM1999100FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.7)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig5ABM199950FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.50)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(60.0)           # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)              # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)        # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig3BM199950FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.50)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig3BM199975FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.75)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig3BM1999100FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)           # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig3BM1999125FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*1.25)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)
    
    
def simulateFig3BM1999150FII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*1.50)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400)           # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)
    

def simulateFig2BM199950FII150ATIII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.50)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400*1.50)      # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig2BM199975FII125ATIII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*0.75)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400*1.25)      # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig2BM1999150FII50ATIII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*1.5)       # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400*0.50)      # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)

def simulateFig2BM1999125FII75ATIII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400*1.25)      # 0 FII
    initial_condition_vector.append(0.0)            # 1 FIIa
    initial_condition_vector.append(0.0)            # 2 PC
    initial_condition_vector.append(0.0)            # 3 APC
    initial_condition_vector.append(3400*0.75)      # 4 ATIII
    initial_condition_vector.append(2)             # 5 TM
    initial_condition_vector.append(0.005)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)        # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)


def simulateFig2BM1999100FII100ATIII(PROBLEM_DICTIONARY):
    
    # Setup the initial conditions for this simulation -
    initial_condition_vector = []
    initial_condition_vector.append(1400)       # 0 FII
    initial_condition_vector.append(0.0)        # 1 FIIa
    initial_condition_vector.append(0.0)        # 2 PC
    initial_condition_vector.append(0.0)        # 3 APC
    initial_condition_vector.append(3400)       # 4 ATIII
    initial_condition_vector.append(2)         # 5 TM
    initial_condition_vector.append(0.005)      # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(2.5)           # TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.7)           # 2 FVIII
    qualitative_factor_vector.append(90.0)          # 3 FIX
    qualitative_factor_vector.append(170.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    # Time and abundance scaling factors -
    scaling_vector = PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR']
    alpha = scaling_vector[0]
    beta = scaling_vector[1]
    
    # Setup time for this simulation -
    TSTART_PHASE_1 = 0.0
    TSTOP_PHASE_1 = 60
    NUMBER_OF_TIMESTEPS = 10*(TSTOP_PHASE_1 - TSTART_PHASE_1)
    local_time_vector = linspace(TSTART_PHASE_1,TSTOP_PHASE_1,NUMBER_OF_TIMESTEPS)
    
    # Solve the differential equations -
    pBalanceEquations = BalanceEquations
    solver = Solver.solveBalanceEquations
    (TIME,STATE) = solver(pBalanceEquations,local_time_vector,PROBLEM_DICTIONARY)
    
    
    return (TIME+alpha,beta*STATE)