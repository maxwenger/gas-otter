class UserInput:
    def getFloatInput(self, message, minValue, maxValue):
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
 
