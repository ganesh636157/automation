import pytest
from pageobejctmodel.test_first import TestOne
@pytest.mark.usefixtures("setup")
class Test1:
    def test_n1(self,setup):
        self.driver=setup
        self.h=TestOne(self.driver)
        self.h.first("ber")
        self.h.second()
        self.h.third()
        self.h.fourth("rahulshettyacademy")
        self.h.fifth()
        self.h.six()
        self.h.seven()
        self.h.eigth("India")

