from ._anvil_designer import MembeddingTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Membedding(MembeddingTemplate):
  def __init__(self, project_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.project_id = project_id
    self.get_images(project_id)
  
  def get_images(self, project_id):
    """Update the slideshow based on the URL hash."""
    # Extract the hash from the URL
    # Call the server function to get the images
    images = anvil.server.call('get_image_urls', project_id=project_id)
    # Populate the carousel with the images
    images.insert(0,'_/theme/gifs/Pink%20Thank%20You%20GIF.gif')
    self.carousel_1.items = [{'source': i, 'alt': '', 'caption': ''} for i in images]

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Configure',anvil.server.call('get_project',project_id = self.project_id))

