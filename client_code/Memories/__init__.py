import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.persistence import persisted_class

@persisted_class
class embeddings:
    key = "id"
    # _media_cache = []
    # media_updated = False

    # @property
    # def media(self):
    #     # Fetch data only if not updated
    #     if not self.media_updated or not self._media_cache:
    #         self._media_cache = anvil.server.call("get_media", embedding_id=self.id)
    #         self.media_updated = True
    #     return self._media_cache

    # def add_media(self, new_media):
    #     """Add new media and mark cache as outdated."""
    #     anvil.server.call("add_images", embedding_id=self.id, images=new_media)
    #     self.media_updated = False  # Invalidate cache

    # def delete_media(self, img_src):
    #     """Delete media by IDs and mark cache as outdated."""
    #     anvil.server.call("delete_image", embedding_id=self.id, img_src=img_src)
    #     self.media_updated = False  # Invalidate cache

    # def get_image_urls(self):
    #     """Get URLs for media objects."""
    #     media = self.media
    #     urls = [row['object'].get_url() for row in media if row.get('object') is not None]
    #     return urls
    

# class Embedding():
#   def init(self, embedding_id):
#     embedding = anvil.server.call("get_embedding",embedding_id=embedding_id)
#     for k,v in embedding.items():
#       self.set_attrs(k,v)
  

def navigate_tabs(tab_title):
  return anvil.open_form(f"Memories.{tab_title.strip(' >')}")
