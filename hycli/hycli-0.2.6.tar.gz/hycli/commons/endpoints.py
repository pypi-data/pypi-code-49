default_endpoints = {
    "production": {
        "extractor": "https://api.hypatos.ai/v2/subscription/invoices",
        "vat_validation": None,
        "validation": None,
        "authentication": "https://customers.hypatos.ai/auth/realms/hypatos/protocol/openid-connect/token",
    },
    "staging": {
        "extractor": "https://api.stage.hypatos.ai/v2/extract",
        "vat_validation": None,
        "validation": None,
        "authentication": "https://customers.stage.hypatos.ai/auth/realms/hypatos/protocol/openid-connect/token",
    },
    "localhost": {
        "extractor": "http://localhost:8000/v2/extract",
        "vat_validation": "http://localhost:7000/validate",
        "validation": "http://localhost:7001/validate",
        "authentication": None,
    },
}
