import anvil.google.auth
from ._anvil_designer import startupTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class startup(startupTemplate):
    def __init__(self, **properties):
        # Initialize form components and properties
        self.init_components(**properties)
        
        #js.window.location.replace('https://energetic-zigzag-illegal.anvil.app/embedding/' + self.embedding.get('id'))
        
        # Set initial URL hash for debugging
        #set_url_hash("#?page=create")
        # set_url_hash("#?embeddingId=175fa861-e07e-47d3-866d-66ebd03d5e2c")
        # url_hash = anvil.get_url_hash().get('embeddingId')
        
        # Handle URL routing
        #self.handle_routing()