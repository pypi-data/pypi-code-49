import json
import os
import requests
import sys

import dcyd.utils.constants as constants


def main(account_name=None):
    """Calls the account service to get credentials."""

    # main() needs to take no args, so that it functions as an entry point.
    if account_name is None:
        account_name = sys.argv[1]

    # Call the account service.
    r = requests.post(
        os.path.join(constants.DCYD_APP_BASE_URL, constants.CONFIG_ROUTE),
        data={'name': account_name}
    )

    # Save the config data.
    with open(constants.CONFIG_FILE, 'w') as f:
        json.dump(r.json(), f)


if __name__ == '__main__':
    main()
