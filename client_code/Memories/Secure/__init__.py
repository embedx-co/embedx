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


class Secure(SecureTemplate):
  def __init__(self, **properties):
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    display_warning()

  def tabs_1_tab_click(self, tab_index, tab_title, **event_args):
    """This method is called when a tab is clicked"""
    anvil.confirm("You have entered a passcode to secure your embedding. This ",title="Passcode Applied")

def display_warning():
  anvil.alert("Your embedding is now only accessible with this passcode. Please make sure this is memorable so you do not lose access to your embedded moments",title="Passcode Applied",dismissible=True)
    