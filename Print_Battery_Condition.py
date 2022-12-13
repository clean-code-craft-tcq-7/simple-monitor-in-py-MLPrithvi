from Check_Battery_Condition import *

def print_battery_properties(temperature, soc, charge_rate):
    if temperature == True:
        print(f'Temperature of the Battery is {temperature} & is within the limit')
    else:
        print(f'Temperature of the Battery is {temperature} & has exceeded the limit')
    if soc == True:
        print(f'State of Charge of the Battery is {soc} & is within the limit')
    else:
        print(f'State of Charge of the Battery is {soc} & has exceeded the limit')
    if charge_rate == True:
        print(f'Charge Rate of the Battery is {charge_rate} & the battery life is in good condition')
    else:
        print(f'Charge Rate of the Battery is {charge_rate} & can affect the battery life')