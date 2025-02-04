from ._anvil_designer import image_viewTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import js


class image_view(image_viewTemplate):
  def __init__(self, img_src, embedding, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source=img_src
    self.image_1.height="100%"
    self.image_1.width="100%"
    self.embedding=embedding
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("frm_race",embedding=self.embedding)
