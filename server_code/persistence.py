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
from anvil_extras.serialisation import datatable_schema
from datetime import datetime

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
def create_new_embedding(**params):
  params['id'] = str(uuid.uuid4())
  params['created'] = datetime.now()
  try:
    app_tables.embeddings.add_row(**params)
  except Exception as e:
    raise(e)
  return "Success"

@anvil.server.callable
def get_media(embedding_id):
    # Fetch all rows from the Data Table
    schema = datatable_schema("media")
    rows = app_tables.media.search(embedding_id=embedding_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    result = schema.dump(rows,many=True)
    return result

@anvil.server.callable
def save_media(embedding_id, to_delete, to_add):
  schema = datatable_schema("media")
  added=[]
  to_delete = [i['id'] for i in to_delete]
  app_tables.media.search(id=q.any_of(*to_delete)).delete_all_rows()
  for i in to_add:
    r=app_tables.media.add_row(id=str(uuid.uuid4()),embedding_id=embedding_id,object=i['object'])
    added.append(schema.dump(r))
  return added


