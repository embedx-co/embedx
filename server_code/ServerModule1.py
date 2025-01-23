import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.secrets
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from hashlib import uuid
from datetime import datetime

@anvil.server.route("/embeddings/create/")
@anvil.server.callable
def create_embedding(**params):
  embedding_id = str(uuid.uuid4())
  app_tables.embeddings.add_row(
    title=params.get('title',""), hyperlink=params.get('hyperlink'), id=embedding_id, modified=datetime.now(), created=datetime.now(),configured=datetime.now()
  )

@anvil.server.callable
def rows_to_dict(rows):
  rows = [rows] if not isinstance(rows,list) else rows
  return [{column: row[column] for column in row.keys()} for row in rows]

@anvil.server.callable
def get_embedding(embedding_id):
    # Fetch all rows from the Data Table
    row = app_tables.embeddings.get(Id=embedding_id)  # Replace with your table name
    # Extract URLs for the "Object" column
    embedding = {}
    for i in row:
