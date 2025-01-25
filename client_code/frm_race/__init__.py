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
          self.file_loader_1_change(images)
        show_activity_config = not embedding.get("activity_id")
        self.drop_down_1.visible = show_activity_config
        self.label_2.visible = show_activity_config
        self.text_box_1.visible = show_activity_config
        self.label_1.visible = show_activity_config
        self.activity_app = self.drop_down_1 or embedding.get("activity_app")
        activity_id = re.match(r"\d{5,}",self.text_box_1.text)
        if activity_id:
          activity_id = activity_id[0]
        self.activity_id = activity_id or embedding.get('activity_id')
        if not show_activity_config:
          iframe = jQuery("<iframe width='100%' height='500px'>").attr("src",f"https://connect.garmin.com/modern/activity/embed/{self.activity_id}")
          iframe.appendTo(get_dom_node(self.embed_panel))
      
    def submit_button_click(self, **event_args):
        # Handle form submission
        title = self.title_box.text
        images = get_image_sources(self.preview_panel)
        anvil.server.call("update_project", self.embedding_id, title, images, self.activity_app, self.activity_id)
        self.refresh_data_bindings()

    def clear_inputs(self):
        # Clear form inputs and uploaded images
        self.title_box.text = ""
        self.check_box_1.checked = False
        self.preview_panel.clear()

    def checkbox_changed(self, **event_args):
        # Toggle the visibility of the 'Remove Selected Photos' button
        self.remove_button.visible = any(
            isinstance(component, anvil.ColumnPanel) and
            any(isinstance(inner_comp, anvil.CheckBox) and inner_comp.checked
                for inner_comp in component.get_components())
            for component in self.preview_panel.get_components()
        )
      
    def link_1_click(self, **event_args):
        anvil.open_form("Form1")
      
    def delete_btn_click(self, **event_args):
        event_args['sender'].tag['container'].remove_from_parent()
        #event_args['sender'].remove_from_parent()
      
    def file_loader_1_change(self, files, **event_args):
        # Handle new file uploads
        for file in files:
            container = anvil.ColumnPanel(spacing_above="small",spacing_below="small")
            image_component = anvil.Image(source=file, width=250, height=250, spacing_above="small",spacing_below="small")
            lnk = anvil.Link(spacing_above="small",spacing_below="small")
            container.add_component(lnk)
            delete_btn = anvil.Button(icon='_/theme/delete.png', icon_align="left", tag={'container':container}, spacing_above="small", spacing_below="small")
            #checkbox = anvil.CheckBox(text="Select")
            delete_btn.set_event_handler("click", self.delete_btn_click)
            lnk.add_component(image_component)
            container.add_component(delete_btn)
            #container.add_component(checkbox)
            lnk.set_event_handler('click',self.launch_preview)
            self.preview_panel.add_component(container)

        self.file_loader_1.text = "Upload additional images"

    def launch_preview(self, **event_args):
        # Get the source of the clicked image
        clicked_image = event_args['sender'].get_components()[0]  # The first component in the link is the image
        if isinstance(clicked_image, anvil.Image):
            img_src = clicked_image.source
            anvil.open_form("image_view", img_src=img_src, embedding=self.embedding)

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
