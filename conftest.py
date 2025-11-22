import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page_context():
    """
    Fixture personalizada para iniciar el navegador.
    Se ejecuta ANTES de cada test y se cierra DESPUÉS.
    """
    with sync_playwright() as p:
        # Lanzamos navegador (headless=False para ver qué pasa mientras desarrollamos)
        browser = p.chromium.launch(headless=True)
        
        # Configuramos el contexto (tamaño de pantalla, grabación de video opcional)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="test-results/videos" # Opcional: graba video de la prueba
        )
        
        # Creamos la página
        page = context.new_page()
        
        # Entregamos la página al test (yield es como return, pero pausa la ejecución)
        yield page
        
        # Todo lo que pongas después del yield se ejecuta al FINAL del test (Teardown)
        context.close()
        browser.close()