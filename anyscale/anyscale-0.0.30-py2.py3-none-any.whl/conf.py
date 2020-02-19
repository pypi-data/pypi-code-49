import os

AWS_PROFILE = None

if "ANYSCALE_HOST" in os.environ:
    ANYSCALE_HOST = os.environ["ANYSCALE_HOST"]
else:
    # The production server.
    ANYSCALE_HOST = "https://anyscale.biz"

# Global variable that contains the server session token.
CLI_TOKEN = None

# Restic snapshot repo
TEST_MODE = False
SNAPSHOT_REPO = "s3:s3.amazonaws.com/anyscale-snapshots/internal"

SNAPSHOT_REPO_PASSWORD = "program_the_cloud"
