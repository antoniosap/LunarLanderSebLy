from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    browser = webdriver.Chrome()
    browser.get('http://moonlander.seb.ly/')
    # driver.findElement(By.linkText("SCORE")).click()


if __name__ == '__main__':
    main()
