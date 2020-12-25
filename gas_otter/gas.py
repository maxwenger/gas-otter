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
        return ppo2 / self.f_o2


    @staticmethod
    def __gas_adds_to_one(f_o2, f_n, f_he):
        f_o2 = f_o2 * 100
        f_n = f_n * 100
        f_he = f_he * 100
        return (f_o2 + f_n + f_he) == 100


