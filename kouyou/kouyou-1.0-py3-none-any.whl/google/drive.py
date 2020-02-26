import pathlib

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from kouyou.google import utils


def connect_to_google_drive():
    """Create connection with google drive api.

    :return: instance of google drive api connection
    :rtype: googleapiclient.discovery.Resource
    """
    SCOPES = ["https://www.googleapis.com/auth/drive"]
    
    cred_file = (str(pathlib.Path(__file__).parent.absolute()) +
                 "/google_key.json")
    try:
        credentials = ServiceAccountCredentials. \
            from_json_keyfile_name(cred_file, SCOPES)
    except FileNotFoundError:
        utils.generate_json_key_file()
        credentials = ServiceAccountCredentials. \
            from_json_keyfile_name(cred_file, SCOPES)
    except ValueError:
        raise ValueError("Couldn't find keys for Google Credential, " +
                         "verify if you have set environment variables in " +
                         "your machine or in a .env file (for pipenv usage)")

    driver_service = build("drive", "v3",
                           credentials=credentials,
                           cache_discovery=False)
    return driver_service


def delete_file_in_drive(file_name, folder_id):
    """Delete every file with name from especific dir on Drive.

    :param file_name: Name of the file to be deleted
    :type file_name: str
    :param folder_id: parent folder id where lies the files
    :type folder_id: str
    """
    drive_service = connect_to_google_drive()
    # Get files in directory
    search_query = f"'{folder_id}' in parents and name='{file_name}'"
    result = drive_service.files().list(q=search_query).execute()

    # Get file(s) ID
    id_list = list()
    for file in result["files"]:
        id_list.append(file["id"])
    # Deleting file(s)
    for file_id in id_list:
        drive_service.files().delete(fileId=file_id).execute()


def create_3rdparty_file_in_drive(file_name, folder_id):
    """Create an empty file of type 3rd party app on Drive Folder.
    
    :param file_name: Name of the file.
    :type file_name: str
    :param folder_id: Folder id to save the file
    :type folder_id: str
    """
    driver_service = connect_to_google_drive()
    body = {"name": file_name,
            "mimeType": "application/vnd.google-apps.drive-sdk",
            "parents": [folder_id]}
    driver_service.files().create(body=body).execute()
    