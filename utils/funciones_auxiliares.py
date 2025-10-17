from selenium.webdriver.common.by import By

#Clase para localizadores de login

class LoginLocators:
    USER_FIELD=(By.ID, "user-name")
    PASSWORD_FIELD=(By.ID, "password")
    LOGIN_BUTTON=(By.ID, "login-button")
    
#Clase para localizadores de inventario

class InventoryLocators:
    PAGE_TITLE=(By.CLASS_NAME, "title")
    PRODUCT_ITEM=(By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME=(By.CLASS_NAME, "inventory_item_name")
    FIRST_PRODUCT_PRICE=(By.CLASS_NAME, "inventory_item_price")
    MENU_BUTTON=(By.ID, "react-burger-menu-btn")
    ADD_TO_CART_BUTTON=(By.XPATH, "(//button[text()='Add to cart'])[1]")
    CART_BADGE=(By.CLASS_NAME, "shopping_cart_badge" )   #contador del carrito
    CART_LINK=(By.CLASS_NAME, "shopping_cart_link")     # enlace al carrito
    
#Clase para localizadores en carrito

class CartLocators:
    CART_ITEM=(By.CLASS_NAME,"cart_item")  #verifica que el item se agregó
    
