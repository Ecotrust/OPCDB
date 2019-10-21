from selenium import webdriver
import unittest

class FirefoxTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_page(self):        #test method names must start with 'test'
        self.browser.get('http://localhost:8000')
        self.assertIn('Database', self.browser.title)
        # self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()    #call unittest.main(), which launches
    #   the unittest test runner, which will automatically find test classes and
    #   methods in the file and run them
