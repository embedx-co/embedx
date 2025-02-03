from ._anvil_designer import FadeInTextComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import js

class FadeInTextComponent(FadeInTextComponentTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def set_text(self, text, delay_ms=200):
        """Animate the text using the custom fade-in effect."""
        js.call('fadeInText', 'fade-text-container', text, delay_ms)