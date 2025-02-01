import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras.persistence import persisted_class

class Embedding:
    def __init__(self, embedding_id=None):
        if not embedding_id:
            embedding_id = anvil.get_url_hash().get('embedding')
    
        embedding_dict = anvil.server.call("get_embedding", embedding_id=embedding_id)
        for k, v in embedding_dict.items():
            setattr(self, k, v)
            
        self._media = None  # internal cache

    @property
    def media(self):
        # If the media cache is empty, refresh it
        if self._media is None:
            self.refresh_media()
        return self._media

    def refresh_media(self):
        """Force refresh the media data from the server."""
        self._media = anvil.server.call("get_media", embedding_id=self.id)
        # Optionally, update media URLs as well:
        self.media_urls = self.get_image_urls(self._media)

    def add_media(self, new_media):
        """Add new media and mark cache as outdated."""
        anvil.server.call("add_images", embedding_id=self.id, images=new_media)
        # Invalidate the cache so the next access refreshes it
        self._media = None

    def delete_media(self, img_src):
        """Delete media by IDs and mark cache as outdated."""
        anvil.server.call("delete_image", embedding_id=self.id, img_src=img_src)
        # Invalidate the cache
        self._media = None

    def get_image_urls(self, media):
        """Get URLs for media objects."""
        urls = [row['object'].get_url() for row in media if row.get('object') is not None]
        return urls


# class Embedding():
#   def init(self, embedding_id):
#     embedding = anvil.server.call("get_embedding",embedding_id=embedding_id)
#     for k,v in embedding.items():
#       self.set_attrs(k,v)
  
embedding = Embedding('175fa861-e07e-47d3-866d-66ebd03d5e2c')

def navigate_tabs(tab_title):
  return anvil.open_form(f"Memories.{tab_title.strip(' >')}")
