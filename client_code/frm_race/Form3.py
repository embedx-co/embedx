from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drp_races = [i.get('name') for i in anvil.server.call("get_event")]
    
    # Any code you write here will run when the form opens.

  def drp_activity_app_change(self, **event_args):
    """This method is called when an item is selected"""
    if event_args['sender'].selected_value == 'Garmin':
      self.lbl_activity_info.text = "Garmin activity link"
    elif event_args['sender'].selected_value == 'Strava':
      self.lbl_activity_info.text = "Strava embed code"
    if event_args['sender'].selected_value != 'None':
      self.lbl_activity_info.visible=True
      self.txt_activity_info.visible=True
      self.lbl_instructions.visible=True
      self.lbl_instructions.text=f"How do I find my {event_args['sender'].selected_value} activity information?"
