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

@persisted_class
class Media:
     embedding_id = Embeddings


# class Embedding:
#     def __init__(self, embedding_id=None):
#         if not embedding_id:
#             embedding_id = anvil.get_url_hash().get('embedding')
    
#         embedding_dict = anvil.server.call("get_embedding", embedding_id=embedding_id)
#         for k, v in embedding_dict.items():
#             setattr(self, k, v)
            
#         self._media = None  # internal cache

#     @property
#     def media(self):
#         if self._media is None:
#             self.refresh_media()
#         return self._media

#     def refresh_media(self):
#         """Force refresh the media data from the server."""
#         self._media = anvil.server.call("get_media", embedding_id=self.id)
#         self.media_urls = self.get_image_urls(self._media)

#     def add_media(self, new_media):
#         """Add new media and update cache incrementally."""
#         # Call the server and get the new media objects.
#         added_media = anvil.server.call("add_images", embedding_id=self.id, images=new_media)
#         # If we already have a local cache, append to it.
#         if self._media is not None:
#             # Assuming added_media is a list; if not, wrap it in a list.
#             if not isinstance(added_media, list):
#                 added_media = [added_media]
#             self._media.extend(added_media)
#             self.media_urls = self.get_image_urls(self._media)
#         # Optionally, if the server might make broader changes, you might instead:
#         # self._media = None  # Invalidate cache
#         # self.refresh_media()

#     def delete_media(self, img_src):
#         """Delete media by image source and update cache incrementally."""
#         # Execute deletion on the server.
#         anvil.server.call("delete_image", embedding_id=self.id, img_src=img_src)
#         # If we have a local cache, filter out the deleted item.
#         if self._media is not None:
#             self._media = [
#                 row for row in self._media 
#                 if row.get('object') is None or row['object'].get_url() != img_src
#             ]
#             self.media_urls = self.get_image_urls(self._media)
#         # Alternatively, if you’re not sure about local consistency:
#         # self._media = None  # Invalidate cache
#         # self.refresh_media()

#     def get_image_urls(self, media):
#         """Get URLs for media objects."""
#         return [row['object'].get_url() for row in media if row.get('object') is not None]



# # class Embedding():
# #   def init(self, embedding_id):
# #     embedding = anvil.server.call("get_embedding",embedding_id=embedding_id)
# #     for k,v in embedding.items():
# #       self.set_attrs(k,v)
  
#embedding = Embedding('175fa861-e07e-47d3-866d-66ebd03d5e2c')

def navigate_tabs(tab_title):
  return anvil.open_form(f"Memories.{tab_title.strip(' >')}")
