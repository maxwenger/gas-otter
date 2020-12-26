import constants as CONST

class PressureCalcs:
    @staticmethod
    def water_pressure_to_depth(pressure, \
            density = CONST.DENSITY_FRESHWATER, \
            gravity = CONST.GRAVIITATIONAL_ACCELERATION):
        ''' 
        Takes in pressure, density, and gravity, and returnes at what depth
        the given pressure would be at given the density and gravity.
        Uses the following formula to calculate the depth:

        Depth (m) = Pressure (Pa) / Density (Kg/m^3) / Gravity (m/s^2)
        
        Parameters:
            pressure (float): Pressure given in bar, not including atmospheric
                pressure
            density (float): Density of fluid given in kg/m^3
            gravity (float): Gravitational acceleration given in m/s^2

        Returns:
            A float depth in meters.
        '''

        if pressure < 0:
            raise ValueError("Pressure must be greater than or equal to zero")

        depth = pressure * CONST.BAR_TO_PA
        depth = depth / density
        depth = depth / gravity
        
        return depth
