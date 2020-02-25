import requests
import getpass

def configure_session_and_url():
  '''interactively setup your sciencedata.dk homeurl, username and password'''
  sciencedata_homeurl = "https://sciencedata.dk/files/" ### your personal homeurl 
  username = input("sciencedata.dk username (format '123456@au.dk'): ")
  password = getpass.getpass("sciencedata.dk password: ")
  ### establish a request session
  s = requests.Session()
  s.auth = (username, password)
  ### SETTING FOR GROUP FOLDER (you either have to be its owner, or at least know user name of its owner)
  group_folder = input("sciencedata.dk group folder (ask group owner): ") ### WARNING: not the group itself!!!
  group_owner_url = "https://sciencedata.dk/files/" + group_folder + "/"
  if s.get("https://sciencedata.dk/files/" + group_folder + "/").ok: ### if you are group 
    sciencedata_groupurl = group_owner_url ### use the url as the endpoint
  else: # otherwise use endpoint for "shared with me"
    group_owner = input("group owner username: ") ### in the case Vojtech is the group owner
    group_member_url = "https://sciencedata.dk/files/sharingin/" + group_owner + "/" + group_folder + "/" 
    sciencedata_groupurl = group_member_url
  print("endpoint for your group (variable 'sciencedata_groupurl') has been configured to: " + sciencedata_groupurl)
  return(sciencedata_groupurl)
