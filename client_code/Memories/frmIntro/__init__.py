from ._anvil_designer import frmIntroTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time


class frmIntro(frmIntroTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.animated_intro.source='_/theme/gifs/christmas2024.gif'
    # Any code you write here will run before the form opens.
    #anvil.open_form("Memories.Stage1")
    
    
