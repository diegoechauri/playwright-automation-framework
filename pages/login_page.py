from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # --- Selectores (Locators) ---
        # Definimos CÓMO encontrar los elementos, pero no hacemos nada aún.
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    # --- Acciones (Actions) ---
    # Métodos que interactúan con la página
    
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """Flujo completo de login"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()