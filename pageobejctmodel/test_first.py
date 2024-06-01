from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
class TestOne:
    xpath1 = "//input[@class='search-keyword']"
    xpath2 = "//h4[@class='product-name']"

    def __init__(self,driver):
        self.driver=driver
    def first(self,text):
        self.driver.find_element(By.XPATH,self.xpath1).send_keys(text)
        time.sleep(4)
    def second(self):
        self.veg_names = self.driver.find_elements(By.XPATH,self.xpath2)
        #list2 = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
        list3 = []
        self.add = self.driver.find_elements(By.XPATH, "//*[text()='ADD TO CART']")
        for list1 in self.veg_names:
            # print(list1.text)
            list3.append(list1.text)
        for add1 in self.add:
            add1.click()
            time.sleep(2)
    def third(self):
        self.driver.find_element(By.XPATH, "//*[@alt='Cart']").click()
        self.driver.find_element(By.XPATH, "//*[text()='PROCEED TO CHECKOUT']").click()
        time.sleep(4)
        self.veg_amount = self.driver.find_elements(By.XPATH, "//tr/td[5]")
        self.amount1 = []
    # amount2=[]
        for self.amount in self.veg_amount:
        # print(amount.text)
            self.amount1.append(self.amount.text)
            self.A4 = self.amount1[1:4]
            self.A5 = []
        for x in self.A4:
            self.A5.append(int(x))
            #print(self.A5)
            self.total = sum(self.A5)
            #print("total_Amount=",self.total)

    def fourth(self,vochure):
        self.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(vochure)
        self.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        time.sleep(10)
        self.amount = self.driver.find_element(By.CSS_SELECTOR, ".totAmt")
        print("total_amount=",self.amount.text)
        self.H = self.driver.find_element(By.CSS_SELECTOR, ".discountAmt")
        print("discount_amount=",self.H.text)
        #self.driver.find_element(By.CSS_SELECTOR, "//button[text()='Place Order']").click()
        time.sleep(4)
    def fifth(self):

        if int(self.total) > float(self.H.text):
            print("Discount applied")
        else:
            print("discount not applied")
    def six(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        time.sleep(4)

    def seven(self):
        self.driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
        time.sleep(4)

    def eigth(self,Country):
        # Locate the dropdown element
        self.dropdown = self.driver.find_element(By.XPATH,"//div/select")  # Replace with the actual ID of the dropdown

        # Create a Select object
        self.select = Select(self.dropdown)
        self.select.select_by_value(Country)
        self.driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
        self.driver.find_element(By.XPATH,"//button").click()
        time.sleep(3)
