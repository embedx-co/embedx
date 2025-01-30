from ._anvil_designer import Stage3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from anvil_extras.animation import animate, fade_in, fade_out, fade_in_slow


class Stage3(Stage3Template):
    def __init__(self, images, **properties):
        self.init_components(**properties)
        self.vertical_align="middle"
        self.flow_panel_1.align='center'
        self.flow_panel_1.gap='small'
        for i in images:
          self.add_photo(i)
        last = self.add_photo('_/theme/Untitled.jpg')
        last.border="thin dashed white"
        

    def add_photo(self, image_url):
        # Calculate width based on the 4:3 aspect ratio
        from anvil.js.window import navigator
        is_mobile = navigator.userAgentData.mobile
        if is_mobile:
          target_height=50
          target_width=50
        else:
          target_height=100
          target_width=100
        photo = anvil.Image(
            source=image_url,
            height=target_height,
            width=target_width,
            display_mode="zoom_to_fill",
            border_radius=2,
            
        )
        self.flow_panel_1.add_component(photo)
        animate(photo, fade_in, 2000)
        return photo
