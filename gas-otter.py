import sys
from container import Container

print('''
          .----.
         /     o\\
        |c  o   0).-.
        |      .-;(_/     .-.
         \    /  /)).---._|  `\   ,
         '.  '  /((       `'-./ _/|
           \  .'  )        .-.;`  /
            '.             |  `\-'
              '._        -'    /
        jgs      ``""--`------`

        Gas Otter v0.0.1 by Maxwell Wenger (GitHub @maxwenger)

''')

def getFloatInput(message, minValue, maxValue):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Please input numbers only.")
            continue

        if userInput < minValue:
            print("Choose a number greater than " + str(minValue))
        elif userInput > maxValue:
            print("Choose a number less than " + str(minValue))
        else:
            return userInput

while True:
    destinationCapacity = getFloatInput("Destination container actual capacity (cuft): ", 0, sys.float_info.max)
    destinationRatedPressure = getFloatInput("Destination container rated pressure (psi): ", 0, sys.float_info.max)
    destinationCurrentPressure = getFloatInput("Destination container current pressure (psi): ", 0, sys.float_info.max)
    destinationFo2 = getFloatInput("Percentage of oxygen in the mix (21% = 0.21): ", 0, 1)
    print()
    
    # Convert capacity in cuft to cuin
    cubicFtToCubicInConversionRatio = 1728
    destinationCapacity = destinationCapacity * cubicFtToCubicInConversionRatio
    destinationContainer = Container(destinationCapacity, destinationRatedPressure, destinationCurrentPressure, destinationFo2)
    print(destinationContainer)
    if input("Is this correct and would you like to use it as your destination container? [y/N]: ") == 'y':
        print("Gas will be used.\n")
        break

while True:
    while True: 
        sourceCapacity = getFloatInput("Source container actual capacity (cuft): ", 0, sys.float_info.max)
        sourceRatedPressure = getFloatInput("Source container rated pressure (psi): ", 0, sys.float_info.max)
        sourceCurrentPressure = getFloatInput("Source container current pressure (psi): ", destinationContainer.getCurrentPressure(), sys.float_info.max)
        sourceFo2 = getFloatInput("Percentage of oxygen in the mix (21% = 0.21): ", 0, 1)
        print()

        sourceCapacity = sourceCapacity * cubicFtToCubicInConversionRatio
        sourceContainer = Container(sourceCapacity, sourceRatedPressure, sourceCurrentPressure, sourceFo2)

        print(sourceContainer)
        gasConfirmed = input("Fill the destination container with this gas? [y/N]: ")
        if gasConfirmed == 'y':
            print("Gas will be added.\n")
            break
        else:
            print("Gas not added.\n")
    
    if(destinationContainer.getCurrentPressure() > sourceContainer.getCurrentPressure()):
        print("The destination container must be at a lower pressure than the source container. No gas was added.")
    elif(destinationContainer.getCurrentPressure() == sourceContainer.getCurrentPressure()):
        print("Containers are at the same pressure. No gas was added.")
    else:
        destinationContainer.fillUntilEqualPressure(sourceContainer)
        print("Destination container now has " + str(round(destinationContainer.getCurrentPressure())) + " psi of " + str(round(destinationContainer.getFO2() * 100)) + "% nitrox.")

    print()
    if input("Add another container? [Y/n]: ") == 'n':
        print("Goodbye.")
        break
