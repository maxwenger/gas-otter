import constants as CONST
from pressure_calcs import PressureCalcs

class Gas:
    def __init__(self, f_o2, f_n, f_he):
        self.set_gas(f_o2, f_n, f_he)

    @property
    def o2(self):
        return self.f_o2

    @property
    def n(self):
        return self.f_n

    @property
    def he(self):
        return self.f_he

    def set_gas(self, f_o2, f_n, f_he):
        if f_o2 == 0:
            raise ValueError("Oxygen must be in gas mix.")
        if not self.__gas_adds_to_one(f_o2, f_n, f_he):
            raise ValueError("Gasses must add to 1")

        self.f_o2 = f_o2
        self.f_n = f_n
        self.f_he = f_he

    def pressure_at_ppo2(self, ppo2):
        ''' Returns the atmospheric pressure at which the gas is the provided
        ppo2. Note: This number DOES include the atmosphere '''

        return ppo2 / self.f_o2

    def get_mod(self, \
            ppo2=CONST.MAX_PPO2, \
            density=CONST.DENSITY_SALTWATER, \
            surf_pressure=CONST.SEA_LEVEL_SURF_PRESSURE_BAR, \
            gravity=CONST.GRAVIITATIONAL_ACCELERATION):

        ''' Returns the max operating depth of the gas '''

        max_ppo2 = self.pressure_at_ppo2(ppo2)
        max_ppo2 = max_ppo2 - surf_pressure
        return PressureCalcs.water_pressure_to_depth(max_ppo2, density, gravity)

    def __str__(self):
        if self.f_he == 0:
            return "EAN" + str(self.f_o2 * 100)

        return str(self.f_o2 * 100) + "/" + str(self.f_he * 100)

    @staticmethod
    def __gas_adds_to_one(f_o2, f_n, f_he):
        f_o2 = f_o2 * 100
        f_n = f_n * 100
        f_he = f_he * 100
        return (f_o2 + f_n + f_he) == 100


