import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.secrets
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import uuid

@anvil.server.callable
def get_embeddings(id):
    return app_tables.embeddings.get(id=id)

@anvil.server.callable
def update_embeddings(row, attrs):
    row.update(**attrs)

@anvil.server.callable
def delete_embeddings(row):
    row.delete()

@anvil.server.route("/create/embedding", methods=["POST"])
@anvil.server.callable
def create_embedding(**params):
  params['id'] = str(uuid.uuid4())
  if not params.get('media'):
    params['media'] = []
  try:
    app_tables.embeddings.add_row(**params)
  except Exception as e:
    print(e)
    raise(e)
  return "Success"


