from ._anvil_designer import homeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

class home(homeTemplate):
  def __init__(self, alrt=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if alrt and alrt == "Not Found":
      anvil.alert("No embeddings found with the provided id!")
    # Any code you write here will run when the form opens.
