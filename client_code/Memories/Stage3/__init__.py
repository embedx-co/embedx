from ._anvil_designer import Stage3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from anvil_extras.animation import Effect, Transition


class Stage3(Stage3Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.vertical_align="middle"
        self.add_photo('_/theme/image1.jpg')
        self.add_photo('_/theme/image2.jpg')
        self.add_photo('_/theme/image3.jpg')
        self.add_photo('_/theme/image4.jpg')
        self.flow_panel_1.align='justify'

    def add_photo(self, image_url):
        # Calculate width based on the 4:3 aspect ratio
        target_height = 225
        target_width = 175

        photo = anvil.Image(
            source=image_url,
            height=target_height,
            width=target_width,
            display_mode="zoom_to_fill",
        )
        
        self.flow_panel_1.add_component(photo)
