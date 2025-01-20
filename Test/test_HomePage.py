import time

import pytest
from PageObject.HomePage import HomePage
from Test.conftest import switchWindows
from Utilities.Base import BaseClass


class TestAccount(BaseClass):

    # def test_LoginAccount(self):
    #
    #     homepage = HomePage(self.driver)
    #     homepage.getAccountList().click()
    #     homepage.getEmailBox().send_keys("shubhamrmrs@gmail.com")
    #     homepage.getContinueButton().click()
    #     homepage.getPasswordBox().send_keys("Sks@123456")
    #     homepage.getSignInButton().click()

    def test_AddToCart(self):

        homepage = HomePage(self.driver)
        homepage.getSearchBar().send_keys("mobile")
        homepage.getMobile().click()
        homepage.getModel().click()
        switchWindows(1)
        time.sleep(2)
        homepage.getAddToCart().click()
        homepage.getCart().click()
        print(homepage.getText().text())




