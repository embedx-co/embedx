from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.animation import animate, fade_in, fade_out, fade_in_slow, wait_for


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    for index, i in enumerate("Merry Christmas"):
      self.data_row_panel_1.add_component(anvil.Label(text=i,font_size=42,bold=True,visible=False),column=index)
      #self.xy_panel_1.add_component(anvil.Label(text=i,font_size=42,bold=True,visible=False),x=0,y=index+25)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    
    for i in self.data_row_panel_1.get_components():
      i.visible=True
      animate(i,fade_in, 250).wait()
