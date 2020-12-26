import pytest
from gas import Gas


class TestGas:
    def test_gas_not_equal_to_one(self):
        pytest.raises(ValueError, Gas, 0, 0, 0)
        pytest.raises(ValueError, Gas, 0.5, 0, 0)
        pytest.raises(ValueError, Gas, 0, 0.5, 0)
        pytest.raises(ValueError, Gas, 0, 0, 0.5)
        pytest.raises(ValueError, Gas, 0.25, 0.25, 0.25)
        pytest.raises(ValueError, Gas, 0.75, 0.25, 0.25)

    def test_gas_without_oxygen(self):
        pytest.raises(ValueError, Gas, 0, 0.5, 0.5)

    def test_valid_nitrox(self):
        f_o2 = 0.7
        f_n = 0.2
        f_he = 0.1
        gas = Gas(f_o2, f_n, f_he)

        assert gas.o2 == f_o2
        assert gas.n ==  f_n
        assert gas.he == f_he

    def test_pressure_at_ppo2(self):
        gas = Gas(0.21, 0.79, 0)

        assert gas.pressure_at_ppo2(1.4) == pytest.approx(6.66666666)
        assert gas.pressure_at_ppo2(1.6) == pytest.approx(7.61904761)

    def test_get_mod(self):
        gas = Gas(0.4, 0.6, 0)
        assert gas.get_mod() == pytest.approx(25, 0.1)
        assert gas.get_mod(surf_pressure=0.8) == pytest.approx(27, 0.1)
        assert gas.get_mod(1.6) == pytest.approx(30, 0.1)
        assert gas.get_mod(1.6, surf_pressure=0.8) == pytest.approx(32, 0.1)


