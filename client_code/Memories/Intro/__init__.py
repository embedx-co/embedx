from ._anvil_designer import IntroTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.animation import animate, fade_in, fade_out, fade_in_slow, wait_for


class Intro(IntroTemplate):
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
      self.headline_1.font_size=72
    animate(self.link_1,fade_in,duration=4000)
    
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    animate(self.link_1, fade_out, 2000).wait()
    anvil.open_form("Memories.Landing")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.timer_1_tick()
