import numpy as np
import pdb

def BalanceEquations(x,t,PROBLEM_DICTIONARY):
    
    #print "Time - ",str(t)
    
    # initialize -
    dxdt_total = []
    
    # Alias the species -
    FII     = x[0]
    FIIa    = x[1]
    PC      = x[2]
    APC     = x[3]
    ATIII   = x[4]
    TM      = x[5]
    TRIGGER = x[6]
    
    # Grab the kinetic parameetrs from the problem dictionary -
    kinetic_parameter_vector = PROBLEM_DICTIONARY['KINETIC_PARAMETER_VECTOR']
    control_parameter_vector = PROBLEM_DICTIONARY['CONTROL_PARAMETER_VECTOR']
    qualitative_factor_level_vector = PROBLEM_DICTIONARY['FACTOR_LEVEL_VECTOR']

    # Alias the qualitative factors -
    TFPI = qualitative_factor_level_vector[0]
    FV = qualitative_factor_level_vector[1]
    FVIII = qualitative_factor_level_vector[2]
    FIX = qualitative_factor_level_vector[3]
    FX = qualitative_factor_level_vector[4]
    PL = qualitative_factor_level_vector[5]

    # Calculate the control vector -
    # Trigger -
    alpha_trigger_activation = control_parameter_vector[0]
    order_trigger_activation = control_parameter_vector[1]
    alpha_trigger_inhibition_APC = control_parameter_vector[2]
    order_trigger_inhibition_APC = control_parameter_vector[3]
    alpha_trigger_inhibition_TFPI = control_parameter_vector[4]
    order_trigger_inhibition_TFPI = control_parameter_vector[5]
    
    # Amplification -
    alpha_amplification_FIIa = control_parameter_vector[6]
    order_amplification_FIIa = control_parameter_vector[7]
    alpha_amplification_APC = control_parameter_vector[8]
    order_amplification_APC = control_parameter_vector[9]
    alpha_amplification_TFPI = control_parameter_vector[10]
    order_amplification_TFPI = control_parameter_vector[11]
    
    # APC generation -
    alpha_shutdown_APC = control_parameter_vector[12]
    order_shutdown_APC = control_parameter_vector[13]
    
    # Initiation model -
    initiation_trigger_term = pow(alpha_trigger_activation*TRIGGER,order_trigger_activation)/(1 + pow(alpha_trigger_activation*TRIGGER,order_trigger_activation))
    initiation_TFPI_term = 1 - pow(alpha_trigger_inhibition_TFPI*TFPI,order_trigger_inhibition_TFPI)/(1 + pow(alpha_trigger_inhibition_TFPI*TFPI,order_trigger_inhibition_TFPI))
    
    # Amplification model -
    activation_term = pow(alpha_amplification_FIIa*FIIa,order_amplification_FIIa)/(1 + pow(alpha_amplification_FIIa*FIIa,order_amplification_FIIa))
    inhibition_term = 1 - pow(alpha_amplification_APC*APC,order_amplification_APC)/(1 + pow(alpha_amplification_APC*APC,order_amplification_APC))
    inhibition_term_TFPI = 1 - pow(alpha_amplification_TFPI*TFPI,order_amplification_TFPI)/(1 + pow(alpha_amplification_TFPI*TFPI,order_amplification_TFPI))
    factor_product = FV*FX*FVIII*FIX
    factor_amplification_term = pow(0.1*factor_product,2)/(1+pow(0.1*factor_product,2))
    
    # Shutdown phase -
    shutdown_term = pow(alpha_shutdown_APC*FIIa,order_shutdown_APC)/(1 + pow(alpha_shutdown_APC*FIIa,order_shutdown_APC))

    control_vector = [0,0,0,0]
    control_vector[0] = min(initiation_trigger_term,initiation_TFPI_term)
    control_vector[1] = min(inhibition_term,inhibition_term_TFPI,factor_amplification_term)
    control_vector[2] = shutdown_term
    control_vector[3] = 1

    # Calculate the kinetics -
    k_trigger = kinetic_parameter_vector[0]
    K_FII_trigger = kinetic_parameter_vector[1]
    k_amplification = kinetic_parameter_vector[2]
    K_FII_amplification = kinetic_parameter_vector[3]
    k_APC_formation = kinetic_parameter_vector[4]
    K_PC_formation = kinetic_parameter_vector[5]
    k_inhibition = kinetic_parameter_vector[6]
    K_FIIa_inhibition = kinetic_parameter_vector[7]
    k_inhibition_ATIII = kinetic_parameter_vector[8]
    #K_inhibition_ATIII = kinetic_parameter_vector[9]
    #K_inhibition_ATIII_FIIa = kinetic_parameter_vector[10]
    
    rate_vector = [0,0,0,0]
    rate_vector[0] = k_trigger*TRIGGER*(FII/(K_FII_trigger + FII))
    rate_vector[1] = k_amplification*FIIa*(FII/(K_FII_amplification + FII))
    rate_vector[2] = k_APC_formation*TM*(PC/(K_PC_formation + PC))
    #rate_vector[3] = k_inhibition*APC*(FIIa/(FIIa + K_FIIa_inhibition)) + k_inhibition_ATIII*(ATIII)*pow(FIIa,1.26)
    rate_vector[3] = k_inhibition_ATIII*(ATIII)*pow(FIIa,1.26)

    # modified rate vector -
    modified_rate_vector = np.array(rate_vector)*np.array(control_vector);

    # calculate dxdt_reaction -
    dxdt_total = [0,0,0,0,0,0,0]
    dxdt_total[0] = -1*modified_rate_vector[1] - modified_rate_vector[0]                            # 0 FII
    dxdt_total[1] = modified_rate_vector[1] + modified_rate_vector[0] - modified_rate_vector[3]     # 1 FIIa
    dxdt_total[2] = -1*modified_rate_vector[2]                                                      # 2 PC
    dxdt_total[3] = 1*modified_rate_vector[2]                                                       # 3 APC
    dxdt_total[4] = -1*k_inhibition_ATIII*(ATIII)*pow(FIIa,1.26)                                    # 4 ATIII
    dxdt_total[5] = 0.0                                                                             # 5 TM (acts as enzyme, so no change)
    dxdt_total[6] = -0.0*TRIGGER                                                                    # 6 TRIGGER

    return dxdt_total