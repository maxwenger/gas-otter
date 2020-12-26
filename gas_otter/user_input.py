class UserInput:

    @staticmethod
    def getFloatInput(message, min_value, max_value, default_value=None):
        while True:

            user_input = input(message)
            if user_input == '' and default_value != None:
                return default_value

            try:
                user_input = float(user_input)
            except (ValueError, SyntaxError):
                print("Please input numbers only.")
                continue
    
            if user_input < min_value:
                print("Choose a number greater than " + str(min_value))
            elif user_input > max_value:
                print("Choose a number less than " + str(max_value))
            else:
                return user_input
 
