from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones_auxiliares import LoginLocators, InventoryLocators, CartLocators

def setup_and_login():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait=WebDriverWait(driver, 10)
    
    # Login
    wait.until(EC.presence_of_element_located(LoginLocators.USER_FIELD)).send_keys("standard_user")
    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("secret_sauce")
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    
    # Espera explícita 
    wait.until(EC.url_contains("/inventory.html"))
    return driver, wait


#------Navegación y Verificación del catálogo-----

def test_verificacion_catalogo():
    driver, wait = setup_and_login()
    try:
        #Validar título 
        page_title = driver.find_element(*InventoryLocators.PAGE_TITLE).text
        assert page_title == "Products", "El título de la página de inventario no es 'Products'."

        #Validar presencia de productos 
        products = driver.find_elements(*InventoryLocators.PRODUCT_ITEM)
        assert len(products) > 0, f"Error: Se esperaban productos, pero se encontraron {len(products)}."

        #Validar elementos importantes
        assert driver.find_element(*InventoryLocators.MENU_BUTTON).is_displayed(), "El botón de menú no es visible."
        
        #Lista nombre/precio del primero
        first_product_name = driver.find_element(*InventoryLocators.FIRST_PRODUCT_NAME).text
        first_product_price = driver.find_element(*InventoryLocators.FIRST_PRODUCT_PRICE).text
        
        print(f"\nVerificación Catálogo OK. Producto listado:\nNombre: {first_product_name}\nPrecio: {first_product_price}")
        
    finally:
        driver.quit()
        
# ---------Interacción con Productos (carrito)

def test_interaccion_carrito():
    driver, wait = setup_and_login()
    try:
        #Agregar primer producto
        driver.find_element(*InventoryLocators.ADD_TO_CART_BUTTON).click()
        
        #Verificar que el contador del carrito se incremente
        cart_badge = driver.find_element(*InventoryLocators.CART_BADGE).text
        assert cart_badge == "1", f"El contador del carrito no se incrementó a 1. Valor actual: {cart_badge}"
        
        #Navegar al carrito de compras
        driver.find_element(*InventoryLocators.CART_LINK).click()
        
        #Verificar ítem en carrito
        # Espera explícita para asegurar que estamos en la página del carrito
        wait.until(EC.url_to_be("https://www.saucedemo.com/cart.html")) 
        
        cart_items = driver.find_elements(*CartLocators.CART_ITEM)
        assert len(cart_items) == 1, f"Error: Se esperaba 1 producto en el carrito, se encontraron {len(cart_items)}."
        
        print("\nInteracción con Carrito OK. Producto verificado en el carrito.")
        
    finally:
        driver.quit()