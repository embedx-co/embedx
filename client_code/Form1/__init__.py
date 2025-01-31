from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    images=['_/theme/gifs/Pink%20Thank%20You%20GIF.gif','_/theme/cork.jpg']
    self.carousel_1.items=[{'source': i, 'alt': '', 'caption': ''} for i in images]
    # Any code you write here will run before the form opens.
