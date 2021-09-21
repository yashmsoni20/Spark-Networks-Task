
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
validsite = "Spark Networks SE | A global leading dating company"

class Task():
    
    
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")     #Opens the Chrome Browser
        self.driver.maximize_window()
        try:   
            self.driver.get("https://www.google.com")          #Navigates to the google homepage 
        
        except Exception as ex:                                #If google is not present in any case
            print('An exception has occurred. Test cannot proceed ', ex)
            self.driver.close()
            raise Exception(ex)
       
        
        self.driver.implicitly_wait(50)
        self.driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()
    
    def task1(self):
        try:
            self.driver.get("https://www.google.com")
            self.driver.find_element(By.NAME, "q").send_keys("Spark networks" + Keys.ENTER)   #Searching for Spark Networks keyword 
            list_html_elems = self.driver.find_elements_by_xpath('//*[@id="search"]//h3')     
            if len(list_html_elems) >= 0 and list_html_elems[0].text == validsite:
                print('Sparks Network SE site detected as first result.')
     
        except Exception as ex:
                print('An exception has occurred. Test cannot proceed ', ex)
                self.driver.close()
     
    def task2(self):
        try:
            self.driver.get("https://www.google.com")
            self.driver.find_element(By.NAME, "q").send_keys("funny cat memes" + Keys.ENTER)  #Searching for Funny cat memes keyword
            self.driver.get_screenshot_as_file("screenshot.png")                              #Screenshot saved in the directory.
            print("Screenshot taken as screenshot.png")
              
        except Exception as ex:
                print('An exception has occurred. Test cannot proceed ', ex)
                self.driver.close() 
 
    def cleanup(self):
        self.driver.close()       
            
X = Task()
X.task1()
X.task2()
X.cleanup()
