from Check_Temperature import *
from Check_State_Of_Charge import *
from Check_Charge_Rate import *

def battery_is_ok(temperature, soc, charge_rate):
  battery_condition = False
  battery_temperature = verify


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
