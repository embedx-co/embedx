import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.persistence import persisted_class
# This is a package.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Package1
#
#    Package1.say_hello()
@persisted_class
class embeddings:
  key="id"
  @property
  def media(self):
    return anvil.server.call("get_media",embedding_id=self.id)
  def add_media(self,media):
    anvil.server.call('add_images',embedding_id=self.id,images=media)
    
# class Embedding():
#   def init(self, embedding_id):
#     embedding = anvil.server.call("get_embedding",embedding_id=embedding_id)
#     for k,v in embedding.items():
#       self.set_attrs(k,v)
  

def navigate_tabs(tab_title):
  return anvil.open_form(f"Memories.{tab_title.strip(' >')}")
