import sys

class Contianer:
    def __init__(self, ratedCapacity, ratedPressure, currentPressure, fo2):
        self.ratedCapacity = ratedCapacity
        self.ratedPressure = ratedPressure
        self.currentPressure = currentPressure
        self.fo2 = fo2

        oneAtmospherePsi = 14.7
        self.volume = (ratedCapacity * oneAtmospherePsi) / ratedPressure

    def getCurrentPressure(self):
        return self.currentPressure

    def getVolume(self):
        return self.volume

    def getFO2(self):
        return self.fo2
    
    def fillUntilEqualPressure(self, sourceContainer):
        if(self.currentPressure >= sourceContainer.currentPressure):
            raise Exception("Source container must have a higher pressure than the target container.")
        startPressure = self.currentPressure
        self.currentPressure = ((self.currentPressure * self.volume) + (sourceContainer.getCurrentPressure() * sourceContainer.getVolume())) / (self.volume + sourceContainer.getVolume())
        sourceContainer.currentPressure = self.currentPressure

        addedPsi = self.currentPressure - startPressure
        addedPsiOfO2 = addedPsi * sourceContainer.getFO2()
        startPsiOfO2 = startPressure * self.fo2
        self.fo2 = (startPsiOfO2 + addedPsiOfO2) / self.currentPressure

print('''
         .-"""-.
        /      o\\
       |    o   0).-.
       |       .-;(_/     .-.
        \     /  /)).---._|  `\   ,
         '.  '  /((       `'-./ _/|
           \  .'  )        .-.;`  /
            '.             |  `\-'
              '._        -'    /
        jgs      ``""--`------`
''')

print("Gas otter v0.0.1")
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

destinationCapacity = getFloatInput("Destination container actual capacity (cuft): ", 0, sys.float_info.max)
destinationRatedPressure = getFloatInput("Destination container rated pressure (psi): ", 0, sys.float_info.max)
destinationCurrentPressure = getFloatInput("Destination container current pressure (psi): ", 0, sys.float_info.max)
destinationFo2 = getFloatInput("Percentage of oxygen in the mix (21% = 0.21): ", 0, 1)
print()

# Convert capacity in cuft to cuin
cubicFtToCubicInConversionRatio = 1728
destinationCapacity = destinationCapacity * cubicFtToCubicInConversionRatio
destinationContainer = Contianer(destinationCapacity, destinationRatedPressure, destinationCurrentPressure, destinationFo2)

while True:
    while True: 
        sourceCapacity = getFloatInput("Source container actual capacity (cuft): ", 0, sys.float_info.max)
        sourceRatedPressure = getFloatInput("Source container rated pressure (psi): ", 0, sys.float_info.max)
        sourceCurrentPressure = getFloatInput("Source container current pressure (psi): ", destinationContainer.getCurrentPressure(), sys.float_info.max)
        sourceFo2 = getFloatInput("Percentage of oxygen in the mix (21% = 0.21): ", 0, 1)
        print()
        print("Container capacity: " + str(sourceCapacity) + " cuft")
        print("Rated container presssure: " + str(sourceRatedPressure) + " psi")
        print("Pressure currently in the container: " + str(sourceCurrentPressure) + " psi")
        print("Mix inside the source has " + str(sourceFo2 * 100) + "% O2")
        gasConfirmed = input("Fill the destination container with this gas? [y/N]: ")
        if gasConfirmed == 'y':
            print("Gas will be added.")
            break
        else:
            print("Gas not added.")
    
    sourceCapacity = sourceCapacity * cubicFtToCubicInConversionRatio
    sourceContainer = Contianer(sourceCapacity, sourceRatedPressure, sourceCurrentPressure, sourceFo2)
    
    print()
    if(destinationContainer.getCurrentPressure() > sourceContainer.getCurrentPressure()):
        print("The destination container must be at a lower pressure than the source container.")
    elif(destinationContainer.getCurrentPressure() == sourceContainer.getCurrentPressure()):
        print("Containers are at the same pressure. No mixing will happen.")
    else:
        destinationContainer.fillUntilEqualPressure(sourceContainer)
        print("Destination container now has " + str(round(destinationContainer.getCurrentPressure())) + " psi of " + str(round(destinationContainer.getFO2() * 100)) + "% nitrox.")

    print()
    if input("Add another container? [Y/n]: ") == 'n':
        print("Goodbye.")
        break
