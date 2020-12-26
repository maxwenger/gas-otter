class UserInput:
    def getFloatInput(self, message, minValue, maxValue):
        while True:
            try:
                userInput = float(input(message))
            except (ValueError, SyntaxError):
                print("Please input numbers only.")
                continue
    
            if userInput < minValue:
                print("Choose a number greater than " + str(minValue))
            elif userInput > maxValue:
                print("Choose a number less than " + str(maxValue))
            else:
                return userInput
 
