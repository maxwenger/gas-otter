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
        self.currentPressure = ((self.currentPressure * self.volume) + (sourceContainer.getCurrentPressure() * sourceContainer.getVolume())) / (self.volume + sourceContainer.getVolume())
        sourceContainer.currentPressure = self.currentPressure

print("Gas otter v0.0.1")

capacity1 = float(input("Contianer 1 capacity (cuft): "))
ratedPressure1 = float(input("Contianer 1 rated pressure (psi): "))
pressure1 = float(input("Contianer 1 current pressure (psi): "))

capacity2 = float(input("Contianer 2 capacity (cuft): "))
ratedPressure2 = float(input("Contianer 2 rated pressure (psi): "))
pressure2 = float(input("Contianer 2 current pressure (psi): "))

# Convert capacity in cuft to cuin
cubicFtToCubicInConversionRatio = 1728
capacity1 = capacity1 * cubicFtToCubicInConversionRatio
capacity2 = capacity2 * cubicFtToCubicInConversionRatio

container1 = Contianer(capacity1, ratedPressure1, pressure1)
container2 = Contianer(capacity2, ratedPressure2, pressure2)

container1.fillUntilEqualPressure(container2)

print("Current pressure: " + str(round(container1.getCurrentPressure())))

