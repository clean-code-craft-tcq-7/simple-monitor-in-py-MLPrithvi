from Check_Temperature import *
from Check_State_Of_Charge import *

def battery_is_ok(temperature, soc):
  battery_condition = False
  battery_temperature = verify_temperature_threshold(temperature)
  battery_soc = verify_state_of_charge_threshold(soc)
  if(battery_temperature and battery_soc):
        battery_condition = True
        return battery_condition
  return battery_condition
