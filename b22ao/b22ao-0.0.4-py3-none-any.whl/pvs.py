
AD_PVBASE = "BL22B-DI-CAM-10"  # Area Detector

DM1_PVBASE = "BL22B-OP-ALPAO-01"  # Deformable mirror 1
DM2_PVBASE = "BL22B-OP-ALPAO-02"  # Deformable mirror 2


AD_ARRAY_COUNTER = "CAM:ArrayCounter_RBV"  # Frame counter
AD_ACQUIRE = "CAM:Acquire"  # Acquire button - write with 'Acquire'
AD_ARRAY_DATA = "ARR:ArrayData"  # Data
AD_DIM_X = "ARR:ArraySize0_RBV"
AD_DIM_Y = "ARR:ArraySize1_RBV"

DM_ACTUATOR_PREFIX = "ACT"  # individual actuator pv: pv base + ACT + actuator number
DM_ACTUATOR_SETPOINT = ":SP"
DM_APPLY_MASK = "CP_ST_TO_ACT.PROC"
