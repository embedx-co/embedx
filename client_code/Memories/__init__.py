import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.persistence import persisted_class

@persisted_class
class Embeddings:
  key = "id"
to_delete=[]

embedding = Embeddings.get('b572d4ad-5d5d-4a3f-ac74-b0ad89f3dc83')
media = anvil.server.call("get_media",embedding_id=embedding.id)

def navigate_tabs(tab_title):
  return anvil.open_form(f"Memories.{tab_title.strip(' >')}")
