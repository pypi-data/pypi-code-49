import os

# This is where openfaas stores secrets by default.
# Note: Can only be accessed by root users!
SECRET_STORE = "/var/openfaas/secrets"


def get_api_key():
    """Get the api key contained in the function container. If the
    "COGNITE_API_KEY" variable, this will be used. Otherwise, the
    api key given when calling creation endpoint will be used.

    Args:
    Returns:
        str: Api key

    Raises:
        FileNotFoundError: If the api key is not found on the file system
    """
    if "COGNITE_API_KEY" in os.environ:
        return os.environ["COGNITE_API_KEY"]

    function_name = os.environ.get("function_name")
    project = os.environ.get("COGNITE_PROJECT")
    filename = f"{SECRET_STORE}/{project}-{function_name}-api-key"
    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"""Api Key not found. Possibly because \n
         you are not in an openfaas function with an api-key set \n
         or because you are developing locally and haven't set COGNITE_API_KEY."""
        )
    with open(filename) as f:
        secret_value = f.read()
    return secret_value
