import sys
from container import Container
from user_input import UserInput

class ContainerFactory:
   
    def promptAndGetContainer(self):
        while True:
            capacity = UserInput().getFloatInput("Container's actual capacity (cuft): ", 0, sys.float_info.max)
            ratedPressure = UserInput().getFloatInput("Container's rated pressure (psi): ", 0, sys.float_info.max)
            currentPressure = UserInput().getFloatInput("Container's current pressure (psi): ", 0, sys.float_info.max)
            fo2 = UserInput().getFloatInput("Percentage of oxygen in the container (21% = 0.21): ", 0, 1)
            print()
            
            # Convert capacity in cuft to cuin
            cubicFtToCubicInConversionRatio = 1728
            capacity = capacity * cubicFtToCubicInConversionRatio
            container = Container(capacity, ratedPressure, currentPressure, fo2)
            print(container)
            if input("Is the above information accurate and would you like to use this container? [y/N]: ") == 'y':
                print("Gas will be used.\n")
                return container
            else:
                print("Gas will be used.\n")

