from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones_auxiliares import LoginLocators, InventoryLocators
import time

def test_login_exitoso():
    driver=webdriver.Chrome()
    wait= WebDriverWait(driver,10) # espera explícita
    try:
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.presence_of_element_located(LoginLocators.USER_FIELD)).send_keys("standard_user")
        
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("secret_sauce")
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        
        inventory_title = wait.until(EC.presence_of_element_located(InventoryLocators.PAGE_TITLE))   #espera explicita
        
        #Validar inventory
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
        print("Login exitoso y validado correctamente")
        
        #Validar titulo
        assert inventory_title.text == "Products", "Validación de título de página fallida."
        
    except Exception as e:
        print(f"Error en test_login_exitoso: {e}")   
        raise
    finally:
        driver.quit()