from prettytable import PrettyTable 
import constants as CONST
from user_input import UserInput
from gas import Gas

extended_mode = False
if input("Enter extended gas info mode [y/N]? ") == 'y':
    exec(open("gas_info_extended.py").read())
    extended_mode = True

while not extended_mode:
    print("")

    f_o2 = UserInput().getFloatInput("Fraction of oxygen (decimal) [0.21]: ", 0.01, 1, default_value=0.21)
    f_he = UserInput().getFloatInput("Fraction of helium (decimal) [0]: ", 0, (1-f_o2), default_value=0)
    surf_pressure = UserInput().getFloatInput("Surface pressure (decimal, bar) [1]: ", 0, 1.1, default_value=1)
    f_n = 1 - f_o2 - f_he
    
    gas = Gas(f_o2, f_n, f_he)

    fresh_min_od = gas.get_mod(CONST.MIN_PPO2, CONST.DENSITY_FRESHWATER, surf_pressure=surf_pressure)
    fresh_mod = gas.get_mod(CONST.MAX_PPO2, CONST.DENSITY_FRESHWATER, surf_pressure=surf_pressure)
    fresh_mod_deco = gas.get_mod(CONST.MAX_PPO2_DECO, CONST.DENSITY_FRESHWATER, surf_pressure=surf_pressure)
    salt_min_od = gas.get_mod(CONST.MIN_PPO2, CONST.DENSITY_SALTWATER, surf_pressure=surf_pressure)
    salt_mod = gas.get_mod(CONST.MAX_PPO2, CONST.DENSITY_SALTWATER, surf_pressure=surf_pressure)
    salt_mod_deco = gas.get_mod(CONST.MAX_PPO2_DECO, CONST.DENSITY_SALTWATER, surf_pressure=surf_pressure)

    round_places = 2
    fresh_min_od = round(fresh_min_od, round_places)
    fresh_mod = round(fresh_mod, round_places)
    fresh_mod_deco = round(fresh_mod_deco, round_places)
    salt_min_od = round(salt_min_od, round_places)
    salt_mod = round(salt_mod, round_places)
    salt_mod_deco = round(salt_mod_deco, round_places)


    table = PrettyTable()
    table.field_names = ["PPO2 (bar)", "Salt Water (m)", "Fresh Water (m)"]

    if salt_min_od != 0 or fresh_min_od != 0:
        table.add_row([CONST.MIN_PPO2, salt_min_od, fresh_min_od])

    table.add_row([CONST.MAX_PPO2, salt_mod, fresh_mod])
    table.add_row([CONST.MAX_PPO2_DECO, salt_mod_deco, fresh_mod_deco])
    table.align = "l"


    print("")
    print("--------------------------------------------------------------------------------")
    print("")
    print("MOD Table for " + str(gas) + " with a surface pressure of " + str(surf_pressure) + " bar")
    print(table)
    print("")
   
    if input("Would you like to enter another gas [Y/n]? ") == 'n':
        break

