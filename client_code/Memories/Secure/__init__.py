from ._anvil_designer import SecureTemplate
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


class Secure(SecureTemplate):
  def __init__(self, **properties):
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if len(self.text_box_1.text.strip())>0:
      display_warning()
      anvil.open_form('Memories.Share')
    else:
      anvil.open_form('Memories.Share')

  def tabs_1_tab_click(self, tab_index, tab_title, **event_args):
    """This method is called when a tab is clicked"""
    confirmation=True
    if len(self.text_box_1.text.strip())>0:
      confirmation = anvil.confirm("You have entered a passcode to secure your embedding. This will be saved if you continue. Would you like to continue?",title="Passcode Applied")
    if confirmation:
      Memories.navigate_tabs(tab_title)

def display_warning():
  anvil.Notification("Your embedding is now only accessible with this passcode. Please make sure this is memorable so you do not lose access to your embedded moments",title="Passcode Applied",dismissible=True)
    