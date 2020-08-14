import sys

class Contianer:
    def __init__(self, ratedCapacity, ratedPressure, currentPressure):
        self.ratedCapacity = ratedCapacity
        self.ratedPressure = ratedPressure
        self.currentPressure = currentPressure

        oneAtmospherePsi = 14.7
        self.volume = (ratedCapacity * oneAtmospherePsi) / ratedPressure

    def getCurrentPressure(self):
        return self.currentPressure

    def getVolume(self):
        return self.volume

    def fillUntilEqualPressure(self, sourceContainer):
        if(self.currentPressure >= sourceContainer.currentPressure):
            raise Exception("Source container must have a higher pressure than the target container.")
        self.currentPressure = ((self.currentPressure * self.volume) + (sourceContainer.getCurrentPressure() * sourceContainer.getVolume())) / (self.volume + sourceContainer.getVolume())
        sourceContainer.currentPressure = self.currentPressure

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
destinationCurrentPressure = getFloatInput("Destination contianer current pressure (psi): ", 0, sys.float_info.max)
print()

# Convert capacity in cuft to cuin
cubicFtToCubicInConversionRatio = 1728
destinationCapacity = destinationCapacity * cubicFtToCubicInConversionRatio
destinationContainer = Contianer(destinationCapacity, destinationRatedPressure, destinationCurrentPressure)

while True:
    while True: 
        sourceCapacity = getFloatInput("Source container actual capacity (cuft): ", 0, sys.float_info.max)
        sourceRatedPressure = getFloatInput("Source container rated pressure (psi): ", 0, sys.float_info.max)
        sourceCurrentPressure = getFloatInput("Source container current pressure (psi): ", destinationContainer.getCurrentPressure(), sys.float_info.max)
        print()
        print("Tank capacity: " + str(sourceCapacity) + " cuft")
        print("Rated tank presssure: " + str(sourceRatedPressure) + " psi")
        print("Pressure currently in the tank: " + str(sourceCurrentPressure) + " psi")
        gasConfirmed = input("Fill the destination container with this gas? [y/N]: ")
        if gasConfirmed == 'y':
            print("Gas will be added.")
            break
        else:
            print("Gas not added.")
    
    sourceCapacity = sourceCapacity * cubicFtToCubicInConversionRatio
    sourceContainer = Contianer(sourceCapacity, sourceRatedPressure, sourceCurrentPressure)
    
    print()
    if(destinationContainer.getCurrentPressure() > sourceContainer.getCurrentPressure()):
        print("The destination container must be at a lower pressure than the source container.")
    elif(destinationContainer.getCurrentPressure() == sourceContainer.getCurrentPressure()):
        print("Containers are at the same pressure. No mixing will happen.")
    else:
        destinationContainer.fillUntilEqualPressure(sourceContainer)
        print("Pressure after equalising both containers: " + str(round(destinationContainer.getCurrentPressure())) + " psi")

    print()
    if input("Add another container? [Y/n]: ") == 'n':
        print("Goodbye.")
        break
