from Check_Battery_Condition import *

def print_battery_properties(temperature, soc, charge_rate):
    if not (temperature):
        print(f'Temperature of the Battery is {temperature} & has exceeded the limit')
    if not (soc):
        print(f'State of Charge of the Battery is {soc} & has exceeded the limit')
    if not (charge_rate):
        print(f'Charge Rate of the Battery is {charge_rate} & can affect the battery life')
