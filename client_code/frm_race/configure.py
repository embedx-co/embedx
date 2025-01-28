from ._anvil_designer import configureTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from anvil import js

class configure(configureTemplate):
  def __init__(self, embedding, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.embedding_id = embedding.get('id')
    self.drp_races.items = [i.get('name') for i in anvil.server.call("get_events")]
    if embedding.get('configured'):
      self.heading.text = "Configure your race embedding"
    else:
      self.heading.text = "Setup your race embedding"

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
    else:
      self.lbl_activity_info.visible = False
      self.txt_activity_info.visible = False
      self.lbl_instructions.visible = False

  def btn_finish_click(self, **event_args):
    """This method is called when the button is clicked"""
    activity_id = re.search('\d{5,}',self.txt_activity_info.text)
    if activity_id:
      activity_id=activity_id[0]
    elif not self.txt_activity_info.text and self.drp_activity_app.selected_value != "None":
      anvil.alert("That is not a valid garmin activity link. Try again")
      return
    activity_app = self.drp_activity_app.selected_value
    full_name = self.txt_name.text
    bib_number = self.txt_bib.text
    owner = self.txt_email.text
    anvil.server.call("update_embedding",embedding_id=self.embedding_id,activity_id=activity_id, activity_app=activity_app, full_name=full_name, owner=owner, bib_number=bib_number)
    js.window.location.replace(anvil.server.get_app_origin() + f"/embedding/{self.embedding_id}")