from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # --- Selectores ---
        # Estrategia robusta: Usamos data-test que es lo más estable
        self.header_title = page.locator(".title")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        
        # Selectores dinámicos (para botones de "Add to cart")
        # Nota: En SauceDemo, los botones tienen ids como 'add-to-cart-sauce-labs-backpack'
        
    def add_item_to_cart(self, item_name_id):
        """
        Agrega un ítem al carrito dado su ID parcial (ej: 'sauce-labs-backpack')
        """
        # Construimos el selector dinámicamente
        item_selector = f"[data-test='add-to-cart-{item_name_id}']"
        self.page.click(item_selector)

    def get_cart_count(self):
        """Devuelve el número entero de ítems en el carrito"""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0