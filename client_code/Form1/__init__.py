from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.animation import animate, fade_in


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    animate(self.carousel_1,fade_in)
    images=['_/theme/cork.jpg','_/theme/IMG_8186.jpeg']
    self.carousel_1.items=[{'source': i, 'alt': '', 'caption': ''} for i in images]
    # Any code you write here will run before the form opens.
