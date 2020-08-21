class NitroxCalculations:
    def getFillInstructions(self, start_pressure, start_mix, desired_pressure, desired_mix, fill_mix, top_off_mix):
        fill_instructions = []

        fill_pressure = self.getFillPressure(start_pressure, start_mix, desired_pressure, desired_mix, fill_mix, top_off_mix)
        top_off_pressure = self.getTopOffPressure(start_pressure, desired_pressure, fill_pressure)

        if start_mix == top_off_mix and fill_pressure < 0:
            raise Exception("Top off mix too lean to make blend.")
        if start_mix == top_off_mix and top_off_pressure < 0:
            raise Exception("Its just air in the tank. Drain it and try it again (Yes this is a limitation of gas otter, will fix later)")
        elif fill_pressure < 0:
            new_start_pressure = (desired_pressure * (desired_mix - top_off_mix)) / (start_mix - top_off_mix)
            pressure_needed_to_be_blead = new_start_pressure - start_pressure

            if new_start_pressure < 0:
                raise Exception("Top off mix too lean to make blend.")

            fill_pressure = self.getFillPressure(new_start_pressure, start_mix, desired_pressure, desired_mix, fill_mix, top_off_mix)
            top_off_pressure = self.getTopOffPressure(new_start_pressure, desired_pressure, fill_pressure)
            fill_instructions.append([pressure_needed_to_be_blead, start_mix])

        fill_instructions.append([fill_pressure, fill_mix])
        fill_instructions.append([top_off_pressure, top_off_mix])
        return fill_instructions

 

    def getFillPressure(self, start_pressure, start_mix, desired_pressure, desired_mix, fill_mix, top_off_mix):
        return ((desired_pressure * (desired_mix - top_off_mix)) - (start_pressure * (start_mix - top_off_mix))) / (fill_mix - top_off_mix)

    def getTopOffPressure(self, start_pressure, desired_pressure, fill_pressure):
        return desired_pressure - start_pressure - fill_pressure
