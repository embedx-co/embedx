import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.persistence import persisted_class
import re
from anvil import js

@persisted_class
class Embeddings:
  key = "id"
embedding_id = anvil.server.call('get_session_embedding')
to_delete=[]
to_add=[]
embedding=Embeddings.get(embedding_id)
media = anvil.server.call("get_media",embedding_id=embedding.id)

def navigate_tabs(tab_title):
  return anvil.open_form(f"Memories.{tab_title.strip(' >')}")
