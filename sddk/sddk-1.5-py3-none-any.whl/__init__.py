import requests
import json
import pandas as pd
import getpass
import matplotlib.pyplot as plt
import sys
from io import StringIO

def configure_session_and_url(shared_folder_name=None, owner=None): ### insert group folder name or leave empty for personal root
  '''
  interactively setup your sciencedata.dk homeurl, username and password
  in the case of shared folder, inquire for its owner as well
  check functionality and redirections
  '''
  ### set username and password
  username = input("sciencedata.dk username (format '123456@au.dk'): ")
  password = getpass.getpass("sciencedata.dk password: ")
  ### establish a request session
  s = requests.Session()
  s.auth = (username, password)
  sciencedata_homeurl_alternatives = ["https://sciencedata.dk/","https://silo1.sciencedata.dk/","https://silo2.sciencedata.dk/","https://silo3.sciencedata.dk/","https://silo4.sciencedata.dk/"]
  for sciencedata_homeurl_root in sciencedata_homeurl_alternatives:
    if s.get(sciencedata_homeurl_root + "files/").ok:
      root_folder_url = sciencedata_homeurl_root + "files/"
      ### SETTING FOR SHARED FOLDER - if their name is passed in: 
      if shared_folder_name != None:
        shared_folder_owner_url = root_folder_url + shared_folder_name + "/"
        if s.get(shared_folder_owner_url).ok: ### if you are owner of the shared folder 
          root_folder_url = shared_folder_owner_url ### use the url as the endpoint
          print("connection with shared folder established with you as its owner")
        else: # otherwise use endpoint for "shared with me"
          if owner==None:
            owner = input("\"" + shared_folder_name + "\" owner's username: ") ### in the case Vojtech is folder owner
          shared_folder_member_url = sciencedata_homeurl_root + "sharingin/" + owner + "/" + shared_folder_name + "/" 
          try:
            redirection = s.get(shared_folder_member_url, allow_redirects=False).headers["Location"]
            if redirection != None:
              shared_folder_member_url = redirection + "/"
          except:
            pass
          if s.get(shared_folder_member_url).ok:
            root_folder_url = shared_folder_member_url
            print("connection with shared folder established with you as its ordinary user")
          else:
            print("connection with shared folder failed")
    break
  print("endpoint variable has been configured to: " + root_folder_url)
  return (s, root_folder_url)

def make_data_from_object(python_object):
  '''
  process the object you want to write
  '''
  if isinstance(python_object, str):
    return (type(python_object), python_object)
  if isinstance(python_object, pd.core.frame.DataFrame): ### if it is pandas dataframe
    return (type(python_object), python_object.to_json())
  if isinstance(python_object, dict):
    return (type(python_object), json.dumps(python_object))
  if isinstance(python_object, list):
    return (type(python_object), json.dumps(python_object))
  if isinstance(python_object, plt.Figure):
    python_object.savefig('temp.png', dpi=fig.dpi)
    return (type(python_object), open("temp.png", 'rb'))
  else:
    print("The function does not support " + str(type(python_object)) + " type of objects. Change the format of your data.")

def check_path(path_and_filename, conf):
  while not conf[0].get(conf[1] + path_and_filename.rpartition("/")[0]).ok:
    path_and_filename = input("The path is not valid. Try different path and filename: ")
  if conf[0].get(conf[1] + path_and_filename.rpartition("/")[0]).ok:
    return path_and_filename
  else:
    print("Sorry, it is still not okay.")

def check_filename(path_and_filename, conf): 
  '''
  check whether there  exist a file with the same name
  '''
  if conf[0].get(conf[1] + path_and_filename).ok: ### if there already is a file with the same name
    print("A file with the same name (\"" + path_and_filename.rpartition("/")[2] + "\") already exists in this location.")
    approved_name = input("Press Enter to overwrite it or choose different path and filename: ")
    if len(approved_name) == 0: 
      approved_name = path_and_filename
  else:
    approved_name = path_and_filename           
  return approved_name

def write_file(path_and_filename, python_object, conf=None):
  '''
  write the file to the specified location
  '''
  if conf==None:
    shared_folder = input("Type shared folder name or press Enter to skip: ")
    if shared_folder != "":
      conf = configure_session_and_url(shared_folder)
    else:
      conf = configure_session_and_url()
  s = conf[0]
  sddk_url = conf[1]
  data_processed = make_data_from_object(python_object)
  path_and_filename = check_path(path_and_filename, conf)
  approved_name = check_filename(path_and_filename, conf)
  try:
    if not approved_name.rpartition(".")[2] in ["txt", "json", "png"]:
      new_filename_ending = input("Unsupported file format. Type either \"txt\", \"json\", or \"png\": ")
      approved_name = approved_name.rpartition(".")[0] + "." + new_filename_ending
      approved_name = check_filename(approved_name) ### check whether the file exists for the second time (the ending changed)
    s.put(sddk_url + approved_name, data=data_processed[1])
    print("Your " + str(data_processed[0]) + " object has been succefully written as \"" + sddk_url + approved_name + "\"")
  except:
    print("Something went wrong. Check path, filename and object.")


def read_file(path_and_filename, object_type, conf=None):
  if conf==None:
    if "shared/" in path_and_filename:
      conf = (requests.Session(), "")
    else:
      shared_folder = input("Type shared folder name or press Enter to skip: ")
      if shared_folder != "":
        conf = configure_session_and_url(shared_folder)
      else:
        conf = configure_session_and_url()
  s = conf[0]
  sddk_url = conf[1]
  response = s.get(sddk_url + path_and_filename)
  if response.ok:
    try: 
      if object_type == "str":
        object_to_return = response.text
      if object_type == "df":
        if ".csv" in path_and_filename:
          object_to_return = pd.read_csv(StringIO(response.text))
        else:
          object_to_return = pd.DataFrame(response.json())
      if object_type == "dict":
        object_to_return = json.loads(response.content)
      if object_type == "list":
        object_to_return = json.loads(response.content)
      return object_to_return
    except:
      print("file import failed")
  else:
    print("file has not been found; check filename and path.")