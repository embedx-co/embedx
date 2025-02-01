from ._anvil_designer import ReliveTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.animation import animate, fade_in
from ... import Memories

class Relive(ReliveTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    animate(self.carousel_1,fade_in)
    print([i.source.get_url() for i in Memories.g_images])
    self.carousel_1.items=[{'source': i.source.get_url(), 'alt': '', 'caption': ''} for i in Memories.g_images]
    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.open_form("Memories.Landing")
