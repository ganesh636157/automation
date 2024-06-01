import pytest
from pageobejctmodel.test_first import TestOne
@pytest.mark.usefixtures("setup","getData")
class Test1:
    def test_n1(self,setup,getData):
        self.driver=setup
        self.h=TestOne(self.driver)
        self.h.first("ber")
        self.h.second()
        self.h.third()
        self.h.fourth()
        self.h.fifth()
        self.h.six()
        self.h.seven()
        #it will run two times(first time:Arub and Second time:India)
        self.h.eigth(getData[1])
        #self.h.eigth("India")U
#pytest --html=report.html