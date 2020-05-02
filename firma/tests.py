from mojprojekt.firma.models import Firm


def test_firm_initialization():
    firm = Firm(firm_name="Ziaja")
    assert firm