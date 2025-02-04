from ._anvil_designer import UploadTemplate
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

class Upload(UploadTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.flow_panel_1.role = "full-screen-background-panel"
    # Any code you write here will run before the form opens.
    #time.sleep(1)
    animate(self.link_1,fade_in,4000)
    animate(self.file_loader_1,fade_in,4000)
    
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.file_loader_1.open_file_selector()

  def file_loader_1_change(self, files, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    for i in self.get_components():
      animate(i, fade_out, 2000)
    Memories.media+=[{'id':'','embedding_id':Memories.embedding.id,'object':file} for file in files]
    anvil.open_form("Memories.Preview")

  def tabs_1_tab_click(self, tab_index, tab_title, **event_args):
    """This method is called when a tab is clicked"""
    Memories.navigate_tabs(tab_title)
