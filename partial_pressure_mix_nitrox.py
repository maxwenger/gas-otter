import sys
from user_input import UserInput
from nitrox_calculations import NitroxCalculations

while True:
    print("")
    start_mix = UserInput().getFloatInput("Enter the starting mix (decimal): ", 0, 1)
    start_pressure = UserInput().getFloatInput("Enter the starting pressure (psi): ", 0, sys.float_info.max)
    desired_mix = UserInput().getFloatInput("Enter the desired mix in (decimal): ", 0, 1)
    desired_pressure = UserInput().getFloatInput("Enter the desired pressure (psi): ", 0, sys.float_info.max)
    fill_mix = UserInput().getFloatInput("Enter the fill mix (decimal): ", 0, 1)
    
    top_off_mix = .21
    
    print("")
    print("Starting with " + str(start_pressure) + " psi of " + str(start_mix*100) + "% nitrox.")
    print("Trying to make " + str(desired_pressure) + " psi of " + str(desired_mix*100) + "% nitrox.")
    print("With a fill mix of " + str(fill_mix*100) + "% nitrox")
    print("With a top-off mix of " + str(top_off_mix*100) + "% nitrox")
    print("")
    
    try:
        fill_instructions = NitroxCalculations().getFillInstructions(start_pressure, start_mix, desired_pressure, desired_mix, fill_mix, top_off_mix)
        pressure_in_tank = start_pressure
        while len(fill_instructions) > 0:
            fill_instruction = fill_instructions.pop(0)

            pressure_in_tank = pressure_in_tank + fill_instruction[0]

            if fill_instruction[0] > 0:
                print("Fill to " + str(round(pressure_in_tank)) + " psi with " + str(round(fill_instruction[1] * 100, 2)) + "% nitrox. (Δ+" + str(round(fill_instruction[0])) + " psi)")
            elif fill_instruction[0] < 0:
                print("Bleed tank to " + str(round(pressure_in_tank)) + " psi (Δ" + str(round(fill_instruction[0])) + " psi)")
        
        print("Confirm the final mix is " + str(desired_pressure) + " psi of " + str(round(desired_mix * 100, 2)) + "% nitrox.")
        print("")
    except Exception as e:
        print(e)

    if input("Would you like to blend another tank of nitrox [Y/n]? ") == 'n':
        break

