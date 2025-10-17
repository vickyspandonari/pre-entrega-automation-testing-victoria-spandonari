from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver=webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
        print("Login exitoso y validado correctamente")
        
    except Exception as e:
        print(f"Error en test-login: {e}")   
        raise
    finally:
        driver.quit() 