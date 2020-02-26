"""Methods required by any kind of service of Google."""
import json
import os
import pathlib

from dotenv import load_dotenv


def generate_json_key_file():
    """Generate the json key file for google credentials.

    The variables must be set in a .env file in project:
    
    project_id ==> GOOGLE_PROJECT_ID\n
    private_key_id ==> GOOGLE_PRIVATE_KEY_ID\n
    private_key ==> GOOGLE_PRIVATE_KEY \n
    client_email ==> GOOGLE_CLIENT_EMAIL\n
    client_x509_cert_url ==> GOOGLE_CLIENT_X509_CERT_URL\n
    
    This values can be found in the json key file, downloaded from
    console.developers.google.com
    """
    load_dotenv()
    path = pathlib.Path(__file__).parent.absolute()
    rsa_key = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")
    json_key = {"type": "service_account",
                "project_id": os.getenv("GOOGLE_PROJECT_ID"),
                "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
                "private_key": rsa_key,
                "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
                }
    with open(f"{path}/google_key.json", "w", encoding="utf-8") as json_file:
        json.dump(json_key, json_file, ensure_ascii=False, indent=4)
