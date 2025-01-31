from ._anvil_designer import frmIntroTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.animation import animate, fade_in, fade_out, fade_in_slow


class frmIntro(frmIntroTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.animated_intro.source='_/theme/gifs/christmas2024.gif'
    # Any code you write here will run before the form opens.
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    animate(self.animated_intro,fade_out,2000)
    anvil.open_form("Memories.Stage1")
    
    
