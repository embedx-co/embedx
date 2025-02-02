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

def add_embeddings(id):
    return app_tables.embeddings.add_row(**attrs)

@anvil.server.callable
def update_embeddings(row, attrs):
    row.update(**attrs)

@anvil.server.callable
def delete_embeddings(row):
    row.delete()
