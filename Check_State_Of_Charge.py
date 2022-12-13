from Threshold_Limit_Constant import *

def verify_state_of_charge(soc):
  if soc < MIN_STATE_OF_CHARGE or soc > MAX_STATE_OF_CHARGE:
    return False
  return True
