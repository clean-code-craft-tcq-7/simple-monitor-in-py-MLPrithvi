from Threshold_Limit_Constant import *

def verify_temperature_threshold(temp):
  if temp < MIN_TEMPERATURE or temp > MAX_TEMPERATURE:
    return False
  return True
