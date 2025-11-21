import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

# Marcamos este test como "smoke" (crítico)
@pytest.mark.smoke
def test_login_exitoso(page_context):
    """
    TC-01: Verificar que un usuario válido pueda iniciar sesión.
    """
    # 1. Instanciamos nuestro Page Object
    # (Le pasamos el 'page_context' que viene de nuestro conftest.py)
    login_p = LoginPage(page_context)
    
    # 2. Usamos los métodos de la clase (Abstracción)
    login_p.navigate()
    
    # Usamos las credenciales oficiales de SauceDemo
    login_p.login("standard_user", "secret_sauce")
    
    # 3. Validaciones (Assertions)
    # Verificamos que la URL haya cambiado a '/inventory.html'
    expect(page_context).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Verificamos que el título de la página sea "Swag Labs"
    expect(page_context).to_have_title("Swag Labs")

@pytest.mark.regression
def test_login_fallido_bloqueado(page_context):
    """
    TC-02: Verificar el error cuando el usuario está bloqueado.
    """
    login_p = LoginPage(page_context)
    login_p.navigate()
    
    # Usamos el usuario "locked_out_user" para provocar el error
    login_p.login("locked_out_user", "secret_sauce")
    
    # Validamos que aparezca el mensaje de error específico
    expect(login_p.error_message).to_be_visible()
    expect(login_p.error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out.")