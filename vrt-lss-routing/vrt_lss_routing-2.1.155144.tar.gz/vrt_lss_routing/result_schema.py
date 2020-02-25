PLAN_RESULT_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "matrix": {
            "additionalProperties": false,
            "nullable": true,
            "properties": {
                "distances": {
                    "items": {
                        "items": {
                            "format": "int64",
                            "type": "integer"
                        },
                        "maxItems": 7000,
                        "minItems": 2,
                        "type": "array",
                        "uniqueItems": false
                    },
                    "maxItems": 7000,
                    "minItems": 2,
                    "type": "array",
                    "uniqueItems": false
                },
                "durations": {
                    "items": {
                        "items": {
                            "format": "int64",
                            "type": "integer"
                        },
                        "maxItems": 7000,
                        "minItems": 2,
                        "type": "array",
                        "uniqueItems": false
                    },
                    "maxItems": 7000,
                    "minItems": 2,
                    "type": "array",
                    "uniqueItems": false
                },
                "waypoints": {
                    "items": {
                        "additionalProperties": false,
                        "nullable": true,
                        "properties": {
                            "duration": {
                                "default": 0,
                                "format": "int32",
                                "maximum": 1440,
                                "minimum": 0,
                                "type": "integer"
                            },
                            "latitude": {
                                "format": "float",
                                "maximum": 90,
                                "minimum": -90,
                                "type": "number"
                            },
                            "longitude": {
                                "format": "float",
                                "maximum": 180,
                                "minimum": -180,
                                "type": "number"
                            }
                        },
                        "required": [
                            "latitude",
                            "longitude"
                        ],
                        "type": "object"
                    },
                    "maxItems": 7000,
                    "minItems": 2,
                    "type": "array",
                    "uniqueItems": false
                }
            },
            "required": [
                "waypoints",
                "distances",
                "durations"
            ],
            "type": "object"
        },
        "tracedata": {
            "additionalProperties": false,
            "properties": {
                "code": {
                    "type": "string"
                }
            },
            "required": [
                "code"
            ],
            "type": "object"
        }
    },
    "required": [
        "matrix"
    ],
    "type": "object"
}'''