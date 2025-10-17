PRE-ENTREGA QA Automation Testing

## PROPÓSITO DEL PROYECTO:

* Aplicar los conceptos vistos en la cursada para automatización de pruebas web utilizando Python, Selenium WebDriver y Pytest

Este proyecto incluye un flujo de pruebas automatizadas en el sitio  https://www.saucedemo.com/:

1. **Login** con credenciales válidas
2. **Navegación y Verificación** de los elementos del catálogo de productos
3. **Interacción** con un producto (añadirlo al carrito y verificar su presencia)

## TECNOLOGÍAS UTILIZADAS:

**Python** -> Lenguaje de programación principal
**Selenium Webdriver** -> Para automatizar la interacción con el navegador
**Pytest** -> Framework para la estructura, ejecución y reporte de las pruebas
**Pytest-html** -> Para la generación de reportes en formato html
**Git y GitHub** -> Para control de versiones y repositorio público

## ESTRUCTURA DEL PROYECTO:

El código está organizado en dos directorios principales, de acuerdo a la consigna, separando tests y funciones auxiliares:

pre-entrega-automation-testing-victoria-spandonari/
                                                    test/
                                                            test_login.py (automatiza login de usuario)
                                                            test_catalogo.py (automatiza catalogo y carrito)
                                                    utils/
                                                            funciones_auxiliares.py (contiene localizadores/selectores de la web)
                                                    reports/ (directorio para almacenar reporte html)
                                                    README.md

## INSTRUCCIONES PARA LA INSTALACION DE DEPENDENCIAS

Para ejecutar las pruebas deberás tener **Python** instalado

1.**Clonar Repositorio:**
En la TERMINAL: git clone [https://github.com/vickyspandonari/pre-entrega-automation-testing-victoria-spandonari.git]

2. **Instalar librerías necesarias**
En la TERMINAL: pip install selenium webdriver pytest pytest-html 

## EJECUCIÓN DE LAS PRUEBAS

Para ejecutar el conjunto completo de pruebas y generar el reporte de resultados en formato html usa el siguiente comando en la TERMINAL:
pytest -v --html=reports/reporte.html


NOTA: Acceso a la Planilla "Pre-Entrega | Casos de Prueba": 
https://docs.google.com/spreadsheets/d/1L3jsaTyrRStMjMl8Lhp9ruj0vXjqAFqJ3GaQeGShi64/edit?usp=sharing