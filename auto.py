import time
from selenium import webdriver
import unittest
import HTMLTestRunner
from selenium.webdriver.common.keys import Keys

class Test_Class(unittest.TestCase):

	driver = webdriver.Chrome('/Users/PHE/Desktop/python/chromedriver')  # Optional argument, if not specified will search path.
	driver.get('http://www.google.com/xhtml')

	

	def test_google(self):
		driver = self.driver
		print self.driver.title
		time.sleep(5) # Let the user actually see something!
		search_box = self.driver.find_element_by_name('q')
		search_box.send_keys('ChromeDriver')
		search_box.submit()
		time.sleep(5) # Let the user actually see something!
		



	def teardown(self):
		self.driver.quit()


if __name__ == "__main__":	
	testsuite = unittest.TestSuite()    
	testsuite.addTest(Test_Class("test_google"))
	testsuite.addTest(Test_Class("teardown"))
        

filename = 'Test_result'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
			stream=fp,
			title='result',
			description='report.'
			)
runner.run(testsuite)


