from ._anvil_designer import SecureTemplate
from anvil import *
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

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    display_warning()
  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    pass

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    display_warning()

def display_warning():
  anvil.alert("Your embedding is now only accessible with this passcode. Please make sure this is memorable so you do not lose access to your embedded moments",title="Passcode Applied",dismissible=True)
    