from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    accountList = (By.XPATH, "//span[text()='Account & Lists']")
    emailBox = (By.XPATH, "//input[@name='email']")
    continueButton = (By.XPATH, "//input[@class='a-button-input']")
    passwordBox = (By.XPATH, "//input[@id='ap_password']")
    signInButton = (By.XPATH, "//input[@id='signInSubmit']")

    def getAccountList(self):
        return self.driver.find_element(*HomePage.accountList)

    def getEmailBox(self):
        return self.driver.find_element(*HomePage.emailBox)

    def getContinueButton(self):
        return self.driver.find_element(*HomePage.continueButton)

    def getPasswordBox(self):
        return self.driver.find_element(*HomePage.passwordBox)

    def getSignInButton(self):
        return self.driver.find_element(*HomePage.signInButton)

    searchBar = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    mobile = (By.XPATH, "//*[@aria-label='mobile phone under 20000']")
    model = (By.LINK_TEXT, "OnePlus Nord CE4 Lite 5G (Super Silver, 8GB RAM, 128GB Storage)")
    addToCart = (By.XPATH,"(//*[@id='add-to-cart-button'])[2]")
    cart = (By.XPATH,"//*[@aria-labelledby='attach-sidesheet-view-cart-button-announce']")
    text = (By.XPATH,"//*[@class='a-truncate-cut']")

    def getSearchBar(self):
        return self.driver.find_element(*HomePage.searchBar)

    def getMobile(self):
        return self.driver.find_element(*HomePage.mobile)

    def getModel(self):
        return self.driver.find_element(*HomePage.model)

    def getAddToCart(self):
        return self.driver.find_element(*HomePage.addToCart)

    def getCart(self):
        return self.driver.find_element(*HomePage.cart)

    def getText(self):
        return self.driver.find_element(*HomePage.text)
