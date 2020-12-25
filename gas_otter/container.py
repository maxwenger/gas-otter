class Container:
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

    def __str__(self):
        cuinToCuftConversionRatio = 1728
        out = "Container capacity: " + str(self.ratedCapacity / cuinToCuftConversionRatio) + " cuft\n"
        out = out + "Rated container presssure: " + str(self.ratedPressure) + " psi\n"
        out = out + "Pressure currently in the container: " + str(self.currentPressure) + " psi\n"
        out = out + "Mix inside the source has " + str(self.fo2 * 100) + "% O2"
        return out


