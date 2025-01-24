import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.secrets
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import uuid
from datetime import datetime
import hashlib

@anvil.server.route("/embeddings/create/")
@anvil.server.callable
def create_embedding(**params):
  embedding_id = str(uuid.uuid4())
  app_tables.embeddings.add_row(
    title=params.get('title',""), hyperlink=params.get('hyperlink'), id=embedding_id, modified=datetime.now(), created=datetime.now(),configured=datetime.now()
  )

@anvil.server.callable
def rows_to_dict(rows):
  result = dict(rows) if not isinstance(rows,list) else [dict(row) for row in rows]
  return result

@anvil.server.callable
def get_embedding(embedding_id):
    # Fetch all rows from the Data Table
    row = app_tables.embeddings.get(id=embedding_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    return rows_to_dict(row)

@anvil.server.callable
def update_project(embedding_id, title, images):
  
  embedding = app_tables.embeddings.get(id = embedding_id)
  if True:#project['Title'] != title or project['Require_Password'] != require_password:
    embedding.update(configured=datetime.now(), modified=datetime.now(), title=title)
    new_image_hashes = [str(hashlib.md5(i.get_bytes() + embedding_id).hexdigest()) for i in images]
    to_delete = app_tables.media.search(
        id=q.none_of(*new_image_hashes),embedding_id=embedding_id
    )
    for i in to_delete:
      i.delete()

    current_image_hashes = [i['id'] for i in app_tables.media.search(embedding_id=embedding_id)]
    for i in images:
        image_hash = str(hashlib.md5(i.get_bytes() + 1).hexdigest())
        if image_hash not in current_image_hashes:
          app_tables.media.add_row(
            embedding_id=embedding, id = image_hash, object=i
          )

@anvil.server.callable
def get_image_urls(embedding_id):
    # Fetch all rows from the Data Table
    rows = app_tables.media.search(embedding_id=embedding_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    urls = [row['object'].get_url() for row in rows if row['object'] is not None]
    return urls
