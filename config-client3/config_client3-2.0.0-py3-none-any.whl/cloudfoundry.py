import json


default_vcap_services = json.dumps(
    {
        "p.config-server": [
            {
                "credentials": {
                    "credhub-ref": ""
                }
            }
        ]
    }
)
default_vcap_application = json.dumps(
    {
        "application_name": "",
        "space_name": "",
        "organization_name": "",
        "uris": []
    }
)
