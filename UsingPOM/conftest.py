import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from testdata.testData import test


@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.close()
@pytest.fixture(params=test.test_data)
def getData(request):
    return request.param

#@pytest.fixture(params=[("India","Aruba","Fiji"),("Aruba","India","Fiji")])
#def getData(request):
    #return request.param