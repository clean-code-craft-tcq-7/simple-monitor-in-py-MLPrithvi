from Check_Temperature import *
from Check_State_Of_Charge import *
from Check_Charge_Rate import *
# from Print_Battery_Condition import *

def battery_is_ok(temperature, soc, charge_rate):
  battery_condition = False
  battery_temperature = verify_temperature_threshold(temperature)
  battery_soc = verify_state_of_charge_threshold(soc)
  battery_charge_rate = verify_charge_rate_threshold(charge_rate)
#   print_battery_properties(battery_temperature, battery_soc, battery_charge_rate)
  if(battery_temperature and battery_soc and battery_charge_rate):
        battery_condition = True
        return battery_condition
  return battery_condition
