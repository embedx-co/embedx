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

    from anvil.js.window import navigator
    import re
    mobile_devices = "Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini"
    is_mobile = re.search(mobile_devices, navigator.userAgent) is not None

    if is_mobile:
      self.headline_1.font_size=36
    else:
      self.headline_1.font_size=54
      
    animate(self.headline_1,fade_in, duration=2000)

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    animate(self.headline_1, fade_out, 2000).wait()
    anvil.open_form("Memories.Upload")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    animate(self.headline_1, fade_out, 2000).wait()
    anvil.open_form("Memories.Upload")
    
    
