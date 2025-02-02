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
from datetime import datetime

class Preview(PreviewTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.vertical_align="middle"
        self.flow_panel_1.align='center'
        self.flow_panel_1.gap='small'
        for i in Memories.media:
          self.add_photo(i)
        last = self.add_photo('_/theme/image_placeholder.png',last=True)
        last.border="thin dashed white"
        animate(self.button_1_copy,fade_in,2000)
      
    def add_photo(self, media_row, last=False):
        # Calculate width based on the 4:3 aspect ratio
    
        from anvil.js.window import navigator
        import re
        mobile_devices = "Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini"
        is_mobile = re.search(mobile_devices, navigator.userAgent) is not None

        if is_mobile:
          target_height=75
          target_width=75
        else:
          target_height=150
          target_width=150
        photo = anvil.Image(
            source=media_row.get('object') if not last else media_row,
            height=target_height,
            width=target_width,
            display_mode="zoom_to_fill",
            border_radius=2,
            tag={'id':media_row.get('id') if not last else '',"Delete":False,"Last":True if last else False}
        )
        lnk = anvil.Link()
        lnk.add_component(photo)
        if not last:
          lnk.set_event_handler('click',self.lnk_click)
        else:
          lnk.set_event_handler('click',self.upload_more_click)
          
        self.flow_panel_1.add_component(lnk)
        animate(photo, fade_in, 2000)
        return photo
        
    def lnk_click(self, **event_args):
      """This method is called when the button is clicked"""
      if event_args['sender'].get_components()[0].role=='clicked-image':
        event_args['sender'].get_components()[0].role=''
        event_args['sender'].get_components()[0].tag['Delete']=False
      else:
        event_args['sender'].get_components()[0].role='clicked-image'
        event_args['sender'].get_components()[0].tag['Delete']=True
        
      if any([True for i in self.flow_panel_1.get_components() if i.get_components()[0].tag['Delete']]):
        self.button_1.visible = True
      else:
        self.button_1.visible=False

    def tabs_1_tab_click(self, tab_index, tab_title, **event_args):
      """This method is called when a tab is clicked"""
      save_media()
      Memories.navigate_tabs(tab_title)

    def upload_more_click(self, **event_args):
      confirmation = True
      if self.button_1.visible:
        confirmation=confirm("You have photos selected, if you continue your selections will be removed. Would you like to continue?")
      if confirmation: 
        self.file_loader_1.open_file_selector()
      
    def file_loader_1_change(self, files, **event_args):
      """This method is called when a new file is loaded into this FileLoader"""
      Memories.media+=[{'id':'','embedding_id':Memories.embedding.id,'object':file} for file in files]
      anvil.open_form("Memories.Preview")

    def button_1_copy_click(self, **event_args):
      """This method is called when the button is clicked"""
      anvil.open_form("Memories.Secure")
      save_media()
  
    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      deleted_objects = [i.get_components()[0].source for i in self.flow_panel_1.get_components() if i.get_components()[0].tag['Delete']]
      Memories.to_delete = [i.get_components()[0].tag for i in self.flow_panel_1.get_components() if i.get_components()[0].tag['Delete'] and  i.get_components()[0].tag['id']]
      Memories.media = [i for i in Memories.media if i['object'] not in deleted_objects]
      anvil.open_form("Memories.Preview")

def save_media():
  to_add = [i for i in Memories.media if not i.get('id')]
  added = anvil.server.call("save_media",to_delete=Memories.to_delete,to_add=to_add,embedding_id=Memories.embedding.id)
  Memories.media = [i for i in Memories.media + added if i.get('id')]
  if len(Memories.media)>0:
    Memories.embedding.configured = datetime.now()
  if Memories.to_delete or added:
    Memories.embedding.modified = datetime.now()
  Memories.embedding.update()
      
  
