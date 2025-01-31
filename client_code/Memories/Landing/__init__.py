from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from anvil_extras.animation import animate, fade_in, fade_out


class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.flow_panel_1.role = "full-screen-background-panel"
    # Any code you write here will run before the form opens.
    self.label_1.visible=True
    animate(self.label_1,fade_in, duration=4000)
    animate(self.label_1,fade_out, duration=2000)
    anvil.open_form("Memories.Upload")
    
    
