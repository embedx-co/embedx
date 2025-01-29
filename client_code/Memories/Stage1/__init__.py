from ._anvil_designer import Stage1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from anvil_extras.animation import Effect, Transition


class Stage1(Stage1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.flow_panel_1.role = "full-screen-background-panel"
    # Any code you write here will run before the form opens.
    time.sleep(5)
    fade_in = Transition(opacity=[0, 1])
    fade_out = Transition(opacity=[1, 0])
    effect_in = Effect(fade_in, duration=500)
    effect_out = Effect(fade_out, duration=3000)
    effect_out.animate(self.label_1)
    self.label_1.visible=False
    
    
