import sys
from user_input import UserInput

start_mix = UserInput().getFloatInput("Enter the starting mix: ", 0, 1)
start_pressure = UserInput().getFloatInput("Enter the starting pressure: ", 0, sys.float_info.max)
desired_mix = start_mix = UserInput().getFloatInput("Enter the desired mix: ", 0, 1)
desired_pressure = UserInput().getFloatInput("Enter the desired pressure: ", 0, sys.float_info.max)
fill_mix = start_mix = UserInput().getFloatInput("Enter the fill mix: ", 0, 1)

top_off_mix = .21

fill_pressure = ((desired_pressure * (desired_mix - top_off_mix)) - (start_pressure * (start_mix - top_off_mix))) / (fill_mix - top_off_mix)
top_off_pressure = desired_pressure - start_pressure - fill_pressure

print("Add " + str(round(fill_pressure)) + " psi of " + str(fill_mix * 100) + "%.")
print("Add " + str(round(top_off_pressure)) + " psi of " + str(top_off_mix * 100) + "%.")

