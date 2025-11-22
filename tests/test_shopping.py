import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

@pytest.mark.smoke
def test_agregar_mochila_al_carrito(page_context):
    """
    TC-03: Validar que un usuario pueda agregar un producto al carrito.
    """
    # 1. Setup (Login)
    login_p = LoginPage(page_context)
    inventory_p = InventoryPage(page_context)
    
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")
    
    # Validamos que estamos dentro antes de seguir
    expect(inventory_p.header_title).to_contain_text("Products")
    
    # 2. Acción: Agregar la mochila (Backpack)
    # El ID del producto en el HTML es 'sauce-labs-backpack'
    inventory_p.add_item_to_cart("sauce-labs-backpack")
    
    # 3. Verificación
    # El numerito rojo en el carrito debe decir "1"
    assert inventory_p.get_cart_count() == 1
    
    # Opcional: Verificar que el botón cambió de texto (ej: a "Remove")
    # Esto demuestra atención al detalle
    boton_remove = page_context.locator("[data-test='remove-sauce-labs-backpack']")
    expect(boton_remove).to_be_visible()