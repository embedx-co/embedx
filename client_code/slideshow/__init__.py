from ._anvil_designer import slideshowTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import js


class slideshow(slideshowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.set_images("_/theme/gifs/Pink%20Thank%20You%20GIF.gif")
    
  def set_images(self, image_urls):
      """Pass images from Python to JavaScript"""
      js.call("setImages", image_urls)

  def next(self):
      """Move to the next slide"""
      js.call("nextSlide")

  def previous(self):
      """Move to the previous slide"""
      js.call("prevSlide")

  def toggle_pause(self):
      """Pause or resume the slideshow"""
      js.call("togglePause")
