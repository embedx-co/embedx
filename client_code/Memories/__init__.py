import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a package.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Package1
#
#    Package1.say_hello()
#

def navigate_tabs(index):
  tab_map={0:"Upload",1:"Preview",2:"Secure",4:"Share",5:"Relive"}
  return anvil.server.FormResponse('frm_race.configure',embedding)
