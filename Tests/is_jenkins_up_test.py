from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJenkinsUp:

    def test_jenkins_is_up(self):
        self.driver.get("http://localhost:8080/")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'security-token')))
        assert self.driver.title == 'Sign in [Jenkins]'
