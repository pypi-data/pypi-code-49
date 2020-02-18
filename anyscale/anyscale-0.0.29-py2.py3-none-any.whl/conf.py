import os

AWS_PROFILE = None

if "ANYSCALE_HOST" in os.environ:
    ANYSCALE_HOST = os.environ["ANYSCALE_HOST"]
else:
    # The production server.
    ANYSCALE_HOST = "https://anyscale.biz"

# Global variable that contains the server session token.
CLI_TOKEN = None
