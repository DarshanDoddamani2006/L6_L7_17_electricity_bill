import pytest
from electricity_bill import energy_charge, late_fee, subsidy


def test_energy_charge_domestic():
    assert energy_charge(50, "domestic") == 200


def test_energy_charge_commercial():
    assert energy_charge(150, "commercial") == 800


def test_energy_charge_high_units():
    assert energy_charge(400, "domestic") == 2100


def test_energy_charge_invalid_connection():
    with pytest.raises(ValueError):
        energy_charge(100, "industrial")


def test_energy_charge_negative_units():
    with pytest.raises(ValueError):
        energy_charge(-10, "domestic")


def test_late_fee_no_delay():
    assert late_fee(1000, 0) == 0


def test_late_fee_within_15_days():
    assert late_fee(1000, 10) == 50


def test_late_fee_above_15_days():
    assert late_fee(3000, 20) == 250


def test_subsidy_senior_citizen():
    assert subsidy(80, True, False) == 50


def test_subsidy_solar():
    assert subsidy(200, False, True) == 100


def test_subsidy_solar_above_300_units():
    assert subsidy(400, True, True) == 0
