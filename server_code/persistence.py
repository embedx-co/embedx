import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.secrets
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_embeddings(id):
    return app_tables.embeddings.get(id=id)

@anvil.server.callable
def get_media(id):
    return app_tables.media.get(id=id)

@anvil.server.callable
def search_media(*args, **kwargs):
    return app_tables.media.search(*args, **kwargs)