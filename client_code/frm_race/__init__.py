from ._anvil_designer import frm_raceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from anvil.js import get_dom_node
from anvil.js.window import jQuery
from anvil import js
from anvil_extras import routing

class frm_race(frm_raceTemplate):
    def __init__(self, embedding, **properties):
        #routing.set_warning_before_app_unload(True)
        self.init_components(**properties)
        self.file_loader_1.multiple = True
        self.embedding=embedding
        self.embedding_id = embedding.get('id')
        # self.title_box.text = embedding.get('title')
        # self.title_box.enabled = not embedding.get('title')
        event = anvil.server.call("get_events",event_ids=[embedding.get("event_id")])
        if event:
          event = event[0]
        else:
          pass #todo ERROR HANDLING
        self.title_box.text = event.get("name")
        self.race_link.url = event.get("url")
        self.results_link.url = embedding.get("hyperlink")
        images = anvil.server.call('get_image_urls', embedding_id=self.embedding_id)
        self.file_loader_1_change(images, on_load=True)
        self.activity_app = embedding.get("activity_app")
        self.activity_id = embedding.get('activity_id')
        if self.activity_app == 'Garmin':
          iframe = jQuery("<iframe width='100%' height='500px'>").attr("src",f"https://connect.garmin.com/modern/activity/embed/{self.activity_id}")
          iframe.appendTo(get_dom_node(self.embed_panel))
        elif self.activity_app == "Strava":
          strava_div = jQuery(f"""
                      <div class="strava-embed-placeholder" 
                          data-embed-type="activity" 
                          data-embed-id={self.activity_id}
                          data-style="standard"
                          data-from-embed="true"></div>
          """)
          strava_div.appendTo(get_dom_node(self.embed_panel))
          script_tag = jQuery("<script>").attr("src", "https://strava-embeds.com/embed.js")
          script_tag.appendTo("body")
        else:
          self.embed_panel.border='thin dashed red'
          empty_txt = anvil.Link()
          empty_txt.set_event_handler('click',self.configure_btn_click)
          empty_txt.text = "Add your Garmin or Strava results!"
          empty_txt.foreground="black"
          empty_txt.align = 'center'
          self.embed_panel.add_component(empty_txt)
          self.embed_panel.align ='center'
        if embedding.get("hyperlink"):
          self.results_link.visible=True
    def delete_btn_click(self, **event_args):
      event_args['sender'].tag['container'].remove_from_parent()
      anvil.server.call('delete_image',embedding_id=self.embedding_id,image_src=event_args['sender'].tag['image_src'])

    def configure_btn_click(self, **event_args):
      self.open_configure_form()
      
    def open_configure_form(self):
      js.window.location.replace(anvil.server.get_app_origin() + f"/embedding/{self.embedding_id}/configure")
      
    def file_loader_1_change(self, files, on_load=False, **event_args):
    # Handle new file uploads
      self.preview_panel.spacing='tiny'
      self.preview_panel.align='center'
      self.preview_panel.spacing_above="tiny"
      self.preview_panel.spacing_below="tiny"
      if files:
        self.file_loader_1.text="Upload additional photos"
      else:
        self.file_loader_1.text="Upload photos from your race day!"
      if not on_load:
        anvil.server.call('add_images',embedding_id=self.embedding_id,images=files)

      for i, file in enumerate(files):
        # Create a container for each uploaded file
        container = anvil.ColumnPanel()
        container.role = "image-container"
        container.spacing = "tiny"
        
        # Create an Image component with the responsive role
        image_component = anvil.Image(source=file)
        image_component.role = "responsive-image"
        image_component.spacing_above="small"
        image_component.spacing_below="small"
        
        # Add a Link component to wrap the image (preserves your preview-on-click)
        lnk = anvil.Link()
        lnk.add_component(image_component)
        lnk.set_event_handler('click', self.launch_preview)
        lnk.col_spacing = 'tiny'
        lnk.spacing_above="tiny"
        lnk.spacing_below="tiny"
    
        # Create the delete button
        delete_btn = anvil.Button(
            icon="fa:trash",
            tag={'container': container, 'image_src': image_component.source},
            foreground="black",
            role='overlapping-button'
        )
        delete_btn.spacing_above='none'
        delete_btn.spacing='none'
        delete_btn.set_event_handler("click", self.delete_btn_click)
    
        # Add Link + Delete to container, and the container to your preview panel
        container.add_component(lnk)
        container.add_component(delete_btn)
        self.preview_panel.add_component(container)
      
      # # Add the placeholder last
      # placeholder_container = anvil.FlowPanel(spacing_above="small", spacing_below="small")
      # placeholder_container.role = "image-container"
      
      # placeholder_link = anvil.Link()
      # placeholder_link.spacing_above="tiny"
      # placeholder_link.spacing_below="tiny"
      # placeholder_link.set_event_handler('click', self.placeholder_link_click)
      
      # placeholder_image = anvil.Image(
      #     source=anvil.URLMedia('_/theme/upload_more.jpg' if files else '_/theme/upload_initial.jpg'),
      #     role=["placeholder-image", "responsive-image"]
      # )
      # placeholder_image.spacing_above="small"
      # placeholder_image.spacing_below="small"
      # placeholder_link.add_component(placeholder_image)
      # placeholder_container.add_component(placeholder_link)
      # self.preview_panel.add_component(placeholder_container)
  
    def placeholder_link_click(self, **event_args):
        # Show the hidden file loader
        event_args['sender'].parent.remove_from_parent()
        self.file_loader_1.open_file_selector()

    def launch_preview(self, **event_args):
        # Get the source of the clicked image
        clicked_image = event_args['sender'].get_components()[0]  # The first component in the link is the image
        if isinstance(clicked_image, anvil.Image):
            img_src = clicked_image.source
            anvil.open_form("image_view", img_src=img_src, embedding=self.embedding)

    def text_box_1_lost_focus(self, **event_args):
      """This method is called when the TextBox loses focus"""
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

    def drop_down_1_change(self, **event_args):
      """This method is called when an item is selected"""

    def link_1_click(self, **event_args):
      """This method is called when the link is clicked"""
      self.open_configure_form()

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