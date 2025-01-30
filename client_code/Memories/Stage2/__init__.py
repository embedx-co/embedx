from ._anvil_designer import Stage2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from anvil_extras.animation import animate, fade_in, fade_out, fade_in_slow


class Stage2(Stage2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.flow_panel_1.role = "full-screen-background-panel"
    # Any code you write here will run before the form opens.
    #time.sleep(1)
    animate(self.image_1,fade_in_slow,3000)
    animate(self.file_loader_1,fade_in,3000)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.file_loader_1.open_file_selector()

  def file_loader_1_change(self, files, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    for i in self.get_components():
      animate(i, fade_out, 2000)
    anvil.open_form("Memories.Stage3",files)
