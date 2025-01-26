from ._anvil_designer import frm_raceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from anvil.js import get_dom_node
from anvil.js.window import jQuery

class frm_race(frm_raceTemplate):
    def __init__(self, embedding, **properties):
        self.init_components(**properties)
        self.file_loader_1.multiple = True
        self.embedding=embedding
        self.embedding_id = embedding.get('id')
        # self.title_box.text = embedding.get('title')
        # self.title_box.enabled = not embedding.get('title')
        event = anvil.server.call("get_event",embedding.get("event_id"))
        self.title_box.text = event.get("name")
        self.race_link.url = event.get("url")
        self.results_link.url = embedding.get("hyperlink")
        self.title_box.enabled = False
        images = anvil.server.call('get_image_urls', embedding_id=self.embedding_id)
        if images:
          self.file_loader_1_change(images, on_load=True)
        show_activity_config = not embedding.get("activity_id")
        self.drop_down_1.visible = show_activity_config
        self.label_2.visible = show_activity_config
        self.text_box_1.visible = show_activity_config
        self.label_1.visible = show_activity_config
        self.activity_app = self.drop_down_1 or embedding.get("activity_app")
        self.activity_id = embedding.get('activity_id')
        if not show_activity_config:
          iframe = jQuery("<iframe width='100%' height='500px'>").attr("src",f"https://connect.garmin.com/modern/activity/embed/{self.activity_id}")
          iframe.appendTo(get_dom_node(self.embed_panel))
      
    # def submit_button_click(self, **event_args):
    #     # Handle form submission
    #     title = self.title_box.text
    #     images = get_image_sources(self.preview_panel)
    #     anvil.server.call("update_project", self.embedding_id, title, images, self.activity_app, self.activity_id)
    #     self.refresh_data_bindings()

    # def clear_inputs(self):
    #     # Clear form inputs and uploaded images
    #     self.title_box.text = ""
    #     self.check_box_1.checked = False
    #     self.preview_panel.clear()

    def delete_btn_click(self, **event_args):
      event_args['sender'].tag['container'].remove_from_parent()
      anvil.server.call('delete_image',embedding_id=self.embedding_id,image_src=event_args['sender'].tag['image_src'])

    def file_loader_1_change(self, files, on_load=False, **event_args):
    # Handle new file uploads
      if not on_load:
        anvil.server.call('add_images',embedding_id=self.embedding_id,images=files)
      
      for file in files:
          # Create a container for each uploaded file
          container = anvil.FlowPanel(spacing_above="small", spacing_below="small")
          container.role = "image-container"
          
        # Create an Image component with the responsive role
          image_component = anvil.Image(source=file)
          image_component.role = "responsive-image"
    
          # Add a Link component to wrap the image
          lnk = anvil.Link()
          lnk.add_component(image_component)
          lnk.set_event_handler('click', self.launch_preview)
  
          # Add a Delete button that overlaps the bottom-right corner
          delete_btn = anvil.Button(icon='fa:remove', icon_align="left", tag={'container': container,'image_src':image_component.source}, foreground="grey")
          delete_btn.set_event_handler("click", self.delete_btn_click)
          delete_btn.role = "overlapping-button"
          
          # Add the components to the container
          container.add_component(lnk)
          container.add_component(delete_btn)
          
          # Add the container to the preview panel
          self.preview_panel.add_component(container)

      # Update the file loader text
      self.file_loader_1.text = "Upload additional images"

    def launch_preview(self, **event_args):
        # Get the source of the clicked image
        clicked_image = event_args['sender'].get_components()[0]  # The first component in the link is the image
        if isinstance(clicked_image, anvil.Image):
            img_src = clicked_image.source
            anvil.open_form("image_view", img_src=img_src, embedding=self.embedding)

    def drop_down_1_change(self, **event_args):
      """This method is called when an item is selected"""

    def btn_embed_results_click(self, **event_args):
      anvil.alert("click ok",inp)
      if len(self.text_box_1.text.strip())>0:
        activity_id = re.match(r"\d{5,}",self.text_box_1.text)
        if activity_id:
          activity_id = activity_id[0]
        else:
          anvil.alert((f"A valid share link or {self.activity_app} activity id is required"))
          return
        self.activity_id = activity_id or self.activity_id
        anvil.server.call('update_project',embedding_id=self.embedding_id, activity_id=activity_id)
        self.refresh_data_bindings()

def get_image_sources(container):
    """
    Recursively collect sources of Image components in a container.
    :param container: Anvil container component
    :return: List of Media objects from Image components
    """
    image_sources = []
    for component in container.get_components():
        if isinstance(component, anvil.Image):
            image_sources.append(component.source)
        elif hasattr(component, 'get_components'):
            image_sources.extend(get_image_sources(component))
    return image_sources