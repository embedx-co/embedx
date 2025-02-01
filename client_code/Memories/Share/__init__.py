from ._anvil_designer import ShareTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from anvil_extras.animation import animate, fade_in, fade_out, fade_in_slow
from ... import Memories


class Share(ShareTemplate):
  def __init__(self, **properties):
    pass

  def tabs_1_tab_click(self, tab_index, tab_title, **event_args):
    Memories.navigate_tabs(tab_title)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form("Memories.Relive",Memories.g_images)
