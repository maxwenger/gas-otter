import sys
import constants as CONST
from user_input import UserInput
from gas import Gas
from pressure_calcs import PressureCalcs

while True:
    print("")
    f_o2 = UserInput().getFloatInput("Fraction of oxygen (decimal) [0.21]: ", 0.01, 1, default_value=0.21)
    f_he = UserInput().getFloatInput("Fraction of helium (decimal) [0]: ", 0, (1-f_o2), default_value=0)
    surf_pressure = UserInput().getFloatInput("Surface pressure (decimal, bar) [1]: ", 0, 100, default_value=1)
    density = UserInput().getFloatInput("Density of the fluid diving in (decimal, kg/m^3) [1000]: ", 0, 15000, default_value=1000)
    gravity = UserInput().getFloatInput("Gravitational acceleration (decimal, m/s^2) [9.81]: ", 0, 25, default_value=9.81)
    ppo2 = UserInput().getFloatInput("Max PPO2 (decimal, bar) [1.4]: ", 0, 100, default_value=1.4)

    f_n = 1 - f_o2 - f_he
    gas = Gas(f_o2, f_n, f_he)

    round_places = 2
    mod = gas.get_mod(ppo2=ppo2, density=density, surf_pressure=surf_pressure, gravity=gravity)


    print("")
    print("MOD at " + str(ppo2) + " bars for " + str(gas))
    print("With a surface pressure of " + str(surf_pressure) + " bar")
    print("Density of fluid: " + str(density) + " kg/m^3")
    print("Gravitational acceleration: " + str(gravity) + " m/s^2")
    print("MOD: " + str(round(mod, 2)) + " m")
    print("")
   
    if input("Would you like to enter another gas [Y/n]? ") == 'n':
        break

