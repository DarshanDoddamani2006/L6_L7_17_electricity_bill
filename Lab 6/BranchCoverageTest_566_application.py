import pytest
from electricity_bill import energy_charge, late_fee, subsidy


def test_energy_charge_branches():
    # Connection validation
    with pytest.raises(ValueError):
        energy_charge(100, "industrial")

    # Negative units
    with pytest.raises(ValueError):
        energy_charge(-10, "domestic")

    # Unit slab branches
    assert energy_charge(50, "domestic") == 200
    assert energy_charge(100, "domestic") == 350
    assert energy_charge(200, "domestic") == 850
    assert energy_charge(300, "domestic") == 1350
    assert energy_charge(400, "domestic") == 2150

    # Commercial connection
    assert energy_charge(150, "commercial") == 1250


def test_late_fee_branches():
    # No late fee
    assert late_fee(1000, 0) == 0

    # Within 15 days
    assert late_fee(1000, 10) == 50

    # More than 15 days, bill <= 2000
    assert late_fee(1000, 20) == 100

    # More than 15 days, bill > 2000
    assert late_fee(3000, 20) == 250


def test_subsidy_branches():
    # Senior citizen conditions
    assert subsidy(80, True, False) == 50
    assert subsidy(80, False, False) == 0
    assert subsidy(150, True, False) == 0

    # Solar conditions
    assert subsidy(200, False, True) == 100
    assert subsidy(400, False, True) == 0

    # Senior citizen and solar together
    assert subsidy(80, True, True) == 150
    assert subsidy(400, True, True) == 0
