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
from datetime import datetime
import hashlib

@anvil.server.callable
def get_session_embedding():
  return anvil.server.session['embedding_id']

def set_session_embedding(embedding_id):
  anvil.server.session['embedding_id']=embedding_id
  
@anvil.server.route("/embedding/:embedding_id")
def embedding_router(embedding_id, **p):
  anvil.server.session['embedding_id']=embedding_id
  embedding = app_tables.embeddings.get(id=embedding_id)
  if embedding['event_id']:
    navigate = serve_race_embedding(embedding_id)
  else:
    navigate = serve_moment_embedding()
  return navigate

def serve_moment_embedding():
    return anvil.server.FormResponse('Memories.Intro')
    
def serve_race_embedding(embedding_id, **p):
  embedding = embedding=anvil.server.call('get_embedding', embedding_id=embedding_id)
  if not embedding.get("configured"):
    response = anvil.server.HttpResponse(302, "Redirecting...")
    response.headers['Location'] = anvil.server.get_app_origin() + f"/embedding/{embedding_id}/configure"
    return response
  else:
    return anvil.server.FormResponse('frm_race',embedding)

@anvil.server.route("/embedding/:embedding_id/configure")
def server_configure_embedding(embedding_id,**p):
  anvil.server.session['embedding_id']=embedding_id
  #embedding = app_tables.embeddings.get(id=embedding_id)
  embedding = anvil.server.call('get_embedding', embedding_id=embedding_id)
  if embedding.get("event_id"):
    return anvil.server.FormResponse('frm_race.configure',embedding)
  else:
    return anvil.server.FormResponse('Memories.Upload')

@anvil.server.callable
def rows_to_dict(rows):
  #TODO this should consistently return a single object type, but I will need to fix downstream code to standardize on list
  if not rows:
    return
  try:
    return dict(rows)
  except Exception as e:
    return [dict(row) for row in rows]
  return

@anvil.server.callable
def get_events(event_ids=[]):
    # Fetch all rows from the Data Table
    if event_ids:
      row = app_tables.events.search(id=q.any_of(*event_ids))  # Replace with your table name
    # Extract URLs for the "Object" column
    else:
      row = app_tables.events.search()
    return rows_to_dict(row)

@anvil.server.callable
def get_embedding(embedding_id):
    # Fetch all rows from the Data Table
    row = app_tables.embeddings.get(id=embedding_id)  # Replace with your table name
    if not row:
      return anvil.server.FormResponse('home',alrt="Not Found")
    embedding_as_dict=rows_to_dict(row)
    return embedding_as_dict
  
@anvil.server.callable
def add_images(embedding_id, images):
  for image in images:
    image_id = str(hashlib.md5(str(str(image.get_bytes()) + embedding_id).encode()).hexdigest())
    return app_tables.media.add_row(
      embedding_id=embedding_id, id = image_id, object=image
    )

@anvil.server.callable
def get_image_id(embedding_id, image_src):
  #TODO add error handling
  return str(hashlib.md5(str(str(image_src.get_bytes()) + embedding_id).encode()).hexdigest())

@anvil.server.callable
def delete_image(embedding_id, image_src):
  image_id = get_image_id(embedding_id=embedding_id,image_src=image_src)
  image = app_tables.media.get(id=image_id)
  image.delete()
  
@anvil.server.callable
def update_embedding(embedding_id, **kwargs):
  embedding = app_tables.embeddings.get(id = embedding_id)
  embedding_as_dict=rows_to_dict(embedding)
  extra_keys = [key for key in kwargs.keys() if key not in embedding_as_dict.keys()]
  if extra_keys:
    raise Exception(f"You cannot pass arguments for {', '.join(extra_keys)}. Those are not fields in the embeddings table.")
  embedding.update(configured=datetime.now(), modified=datetime.now(), **kwargs)
  
#   new_image_hashes = [str(hashlib.md5(str(str(i.get_bytes()) + embedding_id).encode()).hexdigest()) for i in kwargs['images']]
  #   to_delete = app_tables.media.search(
  #       id=q.none_of(*new_image_hashes),embedding_id=embedding_id
  #   )
  #   for i in to_delete:
  #     i.delete()

  #   current_image_hashes = [i['id'] for i in app_tables.media.search(embedding_id=embedding_id)]
  #   for i in kwargs['images']:
  #       image_hash = str(hashlib.md5(str(str(i.get_bytes()) + embedding_id).encode()).hexdigest()) 
  #       if image_hash not in current_image_hashes:
  #         app_tables.media.add_row(
  #           embedding_id=embedding_id, id = image_hash, object=i
  #         )

@anvil.server.callable
def get_image_urls(embedding_id):
    # Fetch all rows from the Data Table
    rows = app_tables.media.search(embedding_id=embedding_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    urls = [row['object'].get_url() for row in rows if row['object'] is not None]
    return urls

# @anvil.server.callable
# def get_media(embedding_id):
#     # Fetch all rows from the Data Table
#     rows = app_tables.media.search(embedding_id=embedding_id)  # Replace with your table name
#     # Extract URLs for the "Object" column
#     return rows_to_dict(rows)