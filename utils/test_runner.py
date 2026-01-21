# Import webdriver module to control browser
from selenium import webdriver
# Import Options class to customize Chrome browser behavior
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Create and return a Chrome WebDriver instance"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    #for headless and jenkins
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Selenium Manager will automatically handle ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)


    return driver