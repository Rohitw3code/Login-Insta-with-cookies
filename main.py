from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pickle
import time


# Instagram URL and credentials (replace with actual details)
login_url = 'https://www.instagram.com/login'

username = ''  # Your Instagram username
password = ''    # Your Instagram password


# File to save cookies
cookies_file = 'instagram_cookies.pkl'

def login_and_save_cookies():
    # Initialize the WebDriver (Chrome in this case)
    service = Service()
    driver = webdriver.Chrome(service=service)
    
    # Go to the Instagram login page
    driver.get(login_url)
    
    # Wait for the page to load completely
    time.sleep(3)
    
    # Find the username and password fields and enter the credentials
    driver.find_element(By.ID, 'username').send_keys(username)  # The name for the username input
    driver.find_element(By.ID, 'password').send_keys(password)  # The name for the password input
    
    driver.find_element(By.CSS_SELECTOR, '.btn__primary--large.from__button--floating').click()
    
    time.sleep(5)
    
    with open(cookies_file, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)
    
    print("Cookies saved successfully!")
    
    # Close the browser
    driver.quit()

def load_cookies_and_use():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.instagram.com/')
    
    try:
        with open(cookies_file, 'rb') as f:
            cookies = pickle.load(f)
        
        for cookie in cookies:
            driver.add_cookie(cookie)
        
        print("Cookies loaded successfully!")
        protected_url = 'https://www.instagram.com/'  
        driver.get(protected_url)
        time.sleep(10)
        
    except FileNotFoundError:
        print("Cookies file not found. Please login first.")
    driver.quit()

if __name__ == '__main__':
    login_and_save_cookies()
    
    load_cookies_and_use()
