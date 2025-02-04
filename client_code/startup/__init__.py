import anvil.google.auth
from ._anvil_designer import startupTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

set_url_hash("#?embedding=175fa861-e07e-47d3-866d-66ebd03d5e2c&configure=True")
set_url_hash("#?embedding=b9899320-9fcb-43e4-838a-eb49b6a5fc5d")
url_hash = anvil.get_url_hash()
embedding = url_hash.get('embedding')
anvil.server.call("set_session_embedding",embedding_id=embedding)
from .. import Memories #this must be called here because the Memories module references the session embedding id which is set above
print( Memories.embedding.title)

class startup(startupTemplate):
    def __init__(self, **properties):
        # Initialize form components and properties
        self.init_components(**properties)
        
        #js.window.location.replace('https://energetic-zigzag-illegal.anvil.app/embedding/' + self.embedding.get('id'))
        if Memories.embedding.event_id:
          if not Memories.embedding.configured or url_hash.get('configure')=="True":
            anvil.set_url_hash(f"#?embedding={Memories.embedding.id}&configure=True")
            anvil.open_form('frm_race.configure')
          else:
            anvil.open_form("frm_race")
        else:
          anvil.open_form("Memories.Intro")