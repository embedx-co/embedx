import anvil.google.auth
from ._anvil_designer import startupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class startup(startupTemplate):
    def __init__(self, **properties):
        # Initialize form components and properties
        self.init_components(**properties)
        
        # Set initial URL hash for debugging
        #set_url_hash("#?page=create")
        set_url_hash("#?page=membedding&projectid=a1d13da2-bad9-48ae-a91e-cb419cced8e7")
        
        # Handle URL routing
        self.handle_routing()

    def handle_routing(self):
        """
        Handle URL hash routing to open the appropriate form.
        """
        url_hash = anvil.get_url_hash()
        if not isinstance(url_hash, str):  # Ensure url_hash is a dictionary
            page = url_hash.get('page')
            project_id = url_hash.get('projectid')
            
            if page == "create":
                # Open the Configure form in create mode
                anvil.google.auth.login()
                #todo Do not hardcode this!
                if anvil.google.auth.get_user_email() == 'trevor@embedx.co':
                  anvil.open_form("Configure", project={}, create=True)
            elif project_id:
                # Retrieve project details and route accordingly
                project = anvil.server.call('get_project', project_id=project_id)
                if project:
                    if not project['Configured']:
                        anvil.open_form('Configure', project)
                    else:
                        anvil.open_form("Membedding", project['Id'])
