from ._anvil_designer import CarouselTemplate
from anvil import *

class Carousel(CarouselTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._items = []
    self._loaded = False
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    
  @property
  def items(self):
    return self._items
  
  @items.setter
  def items(self, value):
    self._items = value or []
    if self._loaded:
      # can only call this function after form has loaded
      self.call_js('add_slides', value)
      
      
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if not self._loaded:
      self._loaded = True
      self.items = self.items

