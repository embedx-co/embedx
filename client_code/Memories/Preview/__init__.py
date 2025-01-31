from ._anvil_designer import PreviewTemplate
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

class Preview(PreviewTemplate):
    def __init__(self, images=[], **properties):
        self.images = images
        # if not images:
        #   images.append('_/theme/IMG_8186.jpeg')
        self.init_components(**properties)
        self.vertical_align="middle"
        self.flow_panel_1.align='center'
        self.flow_panel_1.gap='small'
        for i in images:
          self.add_photo(i)
        last = self.add_photo('_/theme/upload_more.jpg',last=True)
        last.border="thin dashed white"
        
    def add_photo(self, image_url, last=False):
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
            tag={"Delete":False}
            
        )
        lnk = anvil.Link()
        lnk.add_component(photo)
        if not last:
          lnk.set_event_handler('click',self.lnk_click)
        else:
          lnk.set_event_handler('click',self.upload_more_click)
          
        self.flow_panel_1.add_component(lnk)
        animate(photo, fade_in, 1000)
        return photo
        
    def lnk_click(self, **event_args):
      """This method is called when the button is clicked"""
      if event_args['sender'].get_components()[0].role=='clicked-image':
        event_args['sender'].get_components()[0].role=''
        event_args['sender'].get_components()[0].tag={'Delete':False}
      else:
        event_args['sender'].get_components()[0].role='clicked-image'
        event_args['sender'].get_components()[0].tag={'Delete':True}
        
      if any([True for i in self.flow_panel_1.get_components() if i.get_components()[0].tag['Delete']==True]):
        self.button_1.visible = True
      else:
        self.button_1.visible=False

    def tabs_1_tab_click(self, tab_index, tab_title, **event_args):
      """This method is called when a tab is clicked"""
      Memories.navigate_tabs(tab_title)

    def upload_more_click(self, **event_args):
      confirmation = True
      if self.button_1.visible:
        confirmation=confirm("You have photos selected, if you continue your selections will be removed. Would you like to continue?")
      if confirmation: 
        self.file_loader_1.open_file_selector()
      
    def file_loader_1_change(self, files, **event_args):
      """This method is called when a new file is loaded into this FileLoader"""
      self.images.extend(files)
      anvil.open_form("Memories.Preview",images=self.images)
      
  
