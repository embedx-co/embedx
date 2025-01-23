import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.secrets
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import uuid
import hashlib

@anvil.server.callable
def add_project(title, require_password, uploads):
  # This function is called from ConfigureMembedding when the user clicks "SUBMIT".

  # We use Anvil's built-in Data Tables to save the feedback.
  # You can find your Data Tables in the navigation on the left.
  project_id = str(uuid.uuid4())
  app_tables.projects.add_row(
    Title=title, Require_Password=require_password, Modified=datetime.now(), Created=datetime.now(), Id = project_id
  )
  for i in uploads:
      app_tables.media.add_row(
        ProjectId=project_id, Object=i, Id=str(hashlib.md5(i.get_bytes()).hexdigest()) 
      )
  
@anvil.server.callable
def update_project(project_id, title, require_password, uploads):
  
  project = app_tables.projects.get(Id=project_id)
  if True:#project['Title'] != title or project['Require_Password'] != require_password:
    project.update(Configured=datetime.now(), Modified=datetime.now(), Title=title, Require_Password=require_password)
    
    new_image_hashes = [str(hashlib.md5(i.get_bytes()).hexdigest()) for i in uploads]
    to_delete = app_tables.media.search(
        Id=q.none_of(*new_image_hashes),ProjectId=project_id
    )
    for i in to_delete:
      i.delete()

    current_image_hashes = [i['Id'] for i in app_tables.media.search(ProjectId=project_id)]
    for i in uploads:
        image_hash = str(hashlib.md5(i.get_bytes()).hexdigest())
        if image_hash not in current_image_hashes:
          app_tables.media.add_row(
            ProjectId=project_id, Id = image_hash, Object=i
          )
          
@anvil.server.callable
def get_image_urls(project_id):
    # Fetch all rows from the Data Table
    rows = app_tables.media.search(ProjectId=project_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    urls = [row['Object'].get_url() for row in rows if row['Object'] is not None]
    return urls

@anvil.server.callable
def get_project(project_id):
    # Fetch all rows from the Data Table
    row = app_tables.projects.get(Id=project_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    return row