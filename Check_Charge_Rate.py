from Threshold_Limit_Constant import *

def verify_charge_rate_threshold(cr):
  if cr > MAX_CHARGE_RATE:
    return False
  return True
