from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import jQuery
from anvil.js import get_dom_node
from routing.router import navigate

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    iframe = jQuery("<iframe width='100%' height='250px'>").attr("src","https://connect.garmin.com/modern/activity/embed/17914924655")
    iframe.appendTo(get_dom_node(self.flow_panel_1))    
    # strava_div = jQuery("""
    #             <div class="strava-embed-placeholder" 
    #                 data-embed-type="activity" 
    #                 data-embed-id="13233857171" 
    #                 data-style="standard"
    #                 data-from-embed="true"></div>
    #         """)
    # strava_div.appendTo(get_dom_node(self.flow_panel_1))  # Assuming `content_panel` is a container in your form

    # # Dynamically load the Strava embed script
    # script_tag = jQuery("<script>").attr("src", "https://strava-embeds.com/embed.js")
    # script_tag.appendTo("body")
    # Any code you write here will run when the form opens.