import sys
import constants as CONST
from user_input import UserInput
from gas import Gas
from pressure_calcs import PressureCalcs

while True:
    print("")
    f_o2 = UserInput().getFloatInput("Fraction of oxygen (decimal): ", 0.01, 1)
    f_he = UserInput().getFloatInput("Fraction of helium (decimal): ", 0, (1-f_o2))
    f_n = 1 - f_o2 - f_he
    
    gas = Gas(f_o2, f_n, f_he)

    fresh_mod = gas.get_mod(CONST.MAX_PPO2, CONST.DENSITY_FRESHWATER)
    fresh_mod_deco = gas.get_mod(CONST.MAX_PPO2_DECO, CONST.DENSITY_FRESHWATER)
    salt_mod = gas.get_mod(CONST.MAX_PPO2, CONST.DENSITY_SALTWATER)
    salt_mod_deco = gas.get_mod(CONST.MAX_PPO2_DECO, CONST.DENSITY_SALTWATER)

    round_places = 2
    fresh_mod = round(fresh_mod, round_places)
    fresh_mod_deco = round(fresh_mod_deco, round_places)
    salt_mod = round(salt_mod, round_places)
    salt_mod_deco = round(salt_mod_deco, round_places)


    print("")
    print("MOD Table for " + str(gas) + " at mean sea level")
    print("| PPO2\t| Salt Water\t| Fresh Water\t|")
    print("| ----\t| ----------\t| -----------\t|")
    print("| " + str(CONST.MAX_PPO2) + "\t| " + str(salt_mod) + " m\t| " + str(fresh_mod) + " m\t|")
    print("| " + str(CONST.MAX_PPO2_DECO) + "\t| " + str(salt_mod_deco) + " m\t| " + str(fresh_mod_deco) + " m\t|")
    print("")
   
    if input("Would you like to enter another gas [Y/n]? ") == 'n':
        break

