from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        #user hears about new list app which attempt to go to via the browser
        self.browser.get('http://localhost:8000')

        #They look at the title of the web page and make sure it is the list app
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #They then are invited to enter their first item in a list

        # ...


if __name__ == '__main__':
    unittest.main(warnings='ignore')