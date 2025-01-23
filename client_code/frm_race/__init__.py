from ._anvil_designer import frm_raceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class frm_race(frm_raceTemplate):
    def __init__(self, embedding, create=False, **properties):
        self.init_components(**properties)
        self.file_loader_1.multiple = True
        self.embedding_id = embedding['id']
        self.title_box.text = embedding.['title']
        images = anvil.server.call('get_image_urls', embedding_id=self.embedding_id)
        if images:
          self.file_loader_1_change(images)

    def submit_button_click(self, **event_args):
        # Handle form submission
        title = self.title_box.text
        images = get_image_sources(self.flow_panel_1)
        anvil.server.call("update_project", self.project_id, title, require_password, uploads)
        
        self.clear_inputs()

    def clear_inputs(self):
        # Clear form inputs and uploaded images
        self.title_box.text = ""
        self.check_box_1.checked = False
        self.flow_panel_1.clear()

    def checkbox_changed(self, **event_args):
        # Toggle the visibility of the 'Remove Selected Photos' button
        self.remove_button.visible = any(
            isinstance(component, anvil.ColumnPanel) and
            any(isinstance(inner_comp, anvil.CheckBox) and inner_comp.checked
                for inner_comp in component.get_components())
            for component in self.flow_panel_1.get_components()
        )

    def file_loader_1_change(self, files, **event_args):
        # Handle new file uploads
        for file in files:
            container = anvil.ColumnPanel()
            image_component = anvil.Image(source=file, width=200, height=200)
            checkbox = anvil.CheckBox(text="Select")
            checkbox.set_event_handler("change", self.checkbox_changed)
            container.add_component(image_component)
            container.add_component(checkbox)
            self.flow_panel_1.add_component(container)

        self.file_loader_1.text = "Upload additional images"

    def remove_button_click(self, **event_args):
        # Remove containers with selected checkboxes
        for component in list(self.flow_panel_1.get_components()):
            checkbox = component.get_components()[-1]
            if isinstance(checkbox, anvil.CheckBox) and checkbox.checked:
                component.remove_from_parent()
        
        self.remove_button.visible = False
        if not self.flow_panel_1.get_components():
            self.file_loader_1.text = "Upload Images"

    def link_1_click(self, **event_args):
        # Open another form
        anvil.open_form("Form1")


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
