import pytest
from pressure_calcs import PressureCalcs


class TestPressureCalcs:
    def test_water_pressure_to_depth(self):
       assert PressureCalcs.water_pressure_to_depth(0) == 0
       assert PressureCalcs.water_pressure_to_depth(0.098) == pytest.approx(1, 0.1)
       assert PressureCalcs.water_pressure_to_depth(1) == pytest.approx(10, 0.1)
       assert PressureCalcs.water_pressure_to_depth(2.5) == pytest.approx(25, 0.1)

    def test_invalid_water_pressure_to_depth(self):
        pytest.raises(ValueError, PressureCalcs.water_pressure_to_depth, -1)
