class Tank:

    def set_gas(self, gas):
        self.gas = gas

    def set_pressure_bar(self, pressure):
        if pressure < 0:
            raise ValueError("Fill pressure may not be negative")

        self.pressure = pressure

    def set_volume_liter(self, volume):
        if volume < 0:
            raise ValueError("Volume may not be negative")

        self.volume = volume

    def set_fill_pressure_bar(self, pressure):
        if pressure < 0:
            raise ValueError("Fill pressure may not be negative")

        self.fill_pressure = pressure

    def equalize_with(self, tank):
        raise NotImplementedError()

    
    def __check_all_properties_to_equalize_with(self, tank):
        if self.volume == None:
            raise ValueError("This tank has no assigned volume")
        if self.fill_pressure == None:
            raise ValueError("This tank has no assigned fill pressure")
        if tank.volume == None:
            raise ValueError("Tank passed has no assigned volume")
        if tank.fill_pressure == None:
            raise ValueError("Tank passed has no assigned fill pressure")

