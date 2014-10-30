

def buildCoagulationModelDictionary():
    
    # Initialize -
    PROBLEM_DICTIONARY = dict()
    
    # FII     = local_state_vector[0]
    # FIIa    = local_state_vector[1]
    # PC      = local_state_vector[2]
    # APC     = local_state_vector[3]
    # ATIII   = local_state_vector[4]
    # TM      = local_state_vector[5]
    # TRIGGER = local_state_vector[6]
    
    # Initial condition -
    initial_condition_vector = []
    initial_condition_vector.append(1400)       # 0 FII
    initial_condition_vector.append(0.0)        # 1 FIIa
    initial_condition_vector.append(0.0)        # 2 PC
    initial_condition_vector.append(0.0)        # 3 APC
    initial_condition_vector.append(3400)       # 4 ATIII
    initial_condition_vector.append(10)         # 5 TM
    initial_condition_vector.append(0)          # 6 TRIGGER
    PROBLEM_DICTIONARY['INITIAL_CONDITION_VECTOR'] = initial_condition_vector
    
    # Kinetic parameters -
    kinetic_parameter_vector = []
    kinetic_parameter_vector.append(7200)       # 0 k_trigger
    kinetic_parameter_vector.append(1400)       # 1 K_FII_trigger
    kinetic_parameter_vector.append(4.5)        # 2 k_amplification
    kinetic_parameter_vector.append(1200)       # 3 K_FII_amplification
    kinetic_parameter_vector.append(0.1)        # 4 k_APC_formation
    kinetic_parameter_vector.append(30)         # 5 K_PC_formation
    kinetic_parameter_vector.append(0.2)        # 6 k_inhibition
    kinetic_parameter_vector.append(1200)       # 7 K_FIIa_inhibition
    kinetic_parameter_vector.append(0.0001)     # 8 k_inhibition_ATIII
    #kinetic_parameter_vector.append(0.001)      # 9 K_inhibition_ATIII
    #kinetic_parameter_vector.append(100.0)      # 10 K_inhibition_FIIa
    PROBLEM_DICTIONARY['KINETIC_PARAMETER_VECTOR'] = kinetic_parameter_vector
    
    # Control parameters -
    control_parameter_vector = []
    # Trigger -
    control_parameter_vector.append(140.0)      # 0 9 alpha_trigger_activation = control_parameter_vector[0]
    control_parameter_vector.append(2.0)        # 1 10 order_trigger_activation = control_parameter_vector[1]
    control_parameter_vector.append(1.0)        # 2 11 alpha_trigger_inhibition_APC = control_parameter_vector[2]
    control_parameter_vector.append(2.0)        # 3 12 order_trigger_inhibition_APC = control_parameter_vector[3]
    control_parameter_vector.append(0.1)        # 4 13 alpha_trigger_inhibition_TFPI = control_parameter_vector[4]
    control_parameter_vector.append(2.0)        # 5 14 order_trigger_inhibition_TFPI = control_parameter_vector[5]
    
    # Amplification -
    control_parameter_vector.append(0.1)        # 6 15 alpha_amplification_FIIa = control_parameter_vector[6]
    control_parameter_vector.append(2.0)        # 7 16 order_amplification_FIIa = control_parameter_vector[7]
    control_parameter_vector.append(0.4)        # 8 17 alpha_amplification_APC = control_parameter_vector[8]
    control_parameter_vector.append(2.0)        # 9 18 order_amplification_APC = control_parameter_vector[9]
    control_parameter_vector.append(0.01)       # 10 19 alpha_amplification_TFPI = control_parameter_vector[10]
    control_parameter_vector.append(2.0)        # 11 20 order_amplification_TFPI = control_parameter_vector[11]
    
    # APC generation -
    control_parameter_vector.append(2.0)        # 12 21 alpha_shutdown_APC = control_parameter_vector[12]
    control_parameter_vector.append(2.0)        # 13 22 order_shutdown_APC = control_parameter_vector[13]
    PROBLEM_DICTIONARY['CONTROL_PARAMETER_VECTOR'] = control_parameter_vector
    
    # Experimental output scaling -
    # Fig 5A scaling (3.20,1.0)
    # Fig 3 scaling (-1.0,1.0)
    # Fig 2 scaling (1.8)
    # Fig 1 allen scaling (4.0,1.0)
    scaling_parameter_vector = []
    scaling_parameter_vector.append(4.0)        # 0 Time scale 
    scaling_parameter_vector.append(1.0)        # 1 Abundance scale
    PROBLEM_DICTIONARY['SCALING_PARAMETER_VECTOR'] = scaling_parameter_vector
    
    # QFactor vector -
    qualitative_factor_vector = []
    qualitative_factor_vector.append(3.0)           # 0 TFPI
    qualitative_factor_vector.append(20.0)          # 1 FV
    qualitative_factor_vector.append(0.0)           # 2 FVIII
    qualitative_factor_vector.append(0.0)           # 3 FIX
    qualitative_factor_vector.append(135.0)         # 4 FX
    qualitative_factor_vector.append(1.0)           # 5 Platelets
    PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR'] = qualitative_factor_vector
    
    return PROBLEM_DICTIONARY