PLAN_TASK_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "merchandiser_settings": {
            "additionalProperties": false,
            "properties": {
                "accuracy": {
                    "default": "DAY",
                    "enum": [
                        "EXACT",
                        "DAY",
                        "CUSTOM_1",
                        "CUSTOM_2",
                        "CUSTOM_3"
                    ],
                    "type": "string"
                }
            },
            "type": "object"
        },
        "orders": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "duration": {
                        "format": "float",
                        "type": "number"
                    },
                    "facts": {
                        "items": {
                            "additionalProperties": false,
                            "nullable": false,
                            "properties": {
                                "time_window": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "from": {
                                            "format": "date-time",
                                            "type": "string"
                                        },
                                        "to": {
                                            "format": "date-time",
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "from",
                                        "to"
                                    ],
                                    "type": "object"
                                }
                            },
                            "required": [
                                "time_window"
                            ],
                            "type": "object"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "key": {
                        "type": "string"
                    },
                    "location": {
                        "additionalProperties": false,
                        "nullable": true,
                        "properties": {
                            "arrival_duration": {
                                "default": 0,
                                "format": "int32",
                                "maximum": 1440,
                                "minimum": 0,
                                "type": "integer"
                            },
                            "departure_duration": {
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
                    "reward": {
                        "format": "float",
                        "type": "number"
                    },
                    "visits": {
                        "items": {
                            "additionalProperties": false,
                            "nullable": false,
                            "properties": {
                                "time_window": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "from": {
                                            "format": "date-time",
                                            "type": "string"
                                        },
                                        "to": {
                                            "format": "date-time",
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "from",
                                        "to"
                                    ],
                                    "type": "object"
                                }
                            },
                            "required": [
                                "time_window"
                            ],
                            "type": "object"
                        },
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true
                    }
                },
                "required": [
                    "key",
                    "location",
                    "visits",
                    "duration",
                    "reward"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "performer": {
            "additionalProperties": false,
            "properties": {
                "finish_location": {
                    "additionalProperties": false,
                    "nullable": true,
                    "properties": {
                        "arrival_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer"
                        },
                        "departure_duration": {
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
                "key": {
                    "type": "string"
                },
                "shifts": {
                    "items": {
                        "additionalProperties": false,
                        "properties": {
                            "availability_time": {
                                "additionalProperties": false,
                                "properties": {
                                    "from": {
                                        "format": "date-time",
                                        "type": "string"
                                    },
                                    "to": {
                                        "format": "date-time",
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "from",
                                    "to"
                                ],
                                "type": "object"
                            },
                            "trip": {
                                "additionalProperties": false,
                                "properties": {
                                    "actions": {
                                        "items": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "location_time": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string"
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object"
                                                },
                                                "order": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "duration": {
                                                            "format": "float",
                                                            "type": "number"
                                                        },
                                                        "facts": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "nullable": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 0,
                                                            "type": "array",
                                                            "uniqueItems": true
                                                        },
                                                        "key": {
                                                            "type": "string"
                                                        },
                                                        "location": {
                                                            "additionalProperties": false,
                                                            "nullable": true,
                                                            "properties": {
                                                                "arrival_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer"
                                                                },
                                                                "departure_duration": {
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
                                                        "reward": {
                                                            "format": "float",
                                                            "type": "number"
                                                        },
                                                        "visits": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "nullable": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 1,
                                                            "type": "array",
                                                            "uniqueItems": true
                                                        }
                                                    },
                                                    "required": [
                                                        "key",
                                                        "location",
                                                        "visits",
                                                        "duration",
                                                        "reward"
                                                    ],
                                                    "type": "object"
                                                },
                                                "order_time": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string"
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object"
                                                }
                                            },
                                            "required": [
                                                "order",
                                                "order_time",
                                                "location_time"
                                            ],
                                            "type": "object"
                                        },
                                        "maxItems": 1000,
                                        "minItems": 1,
                                        "type": "array",
                                        "uniqueItems": true
                                    },
                                    "key": {
                                        "type": "string"
                                    },
                                    "trip_time": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "from": {
                                                "format": "date-time",
                                                "type": "string"
                                            },
                                            "to": {
                                                "format": "date-time",
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "from",
                                            "to"
                                        ],
                                        "type": "object"
                                    },
                                    "waitlist": {
                                        "items": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "order": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "duration": {
                                                            "format": "float",
                                                            "type": "number"
                                                        },
                                                        "facts": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "nullable": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 0,
                                                            "type": "array",
                                                            "uniqueItems": true
                                                        },
                                                        "key": {
                                                            "type": "string"
                                                        },
                                                        "location": {
                                                            "additionalProperties": false,
                                                            "nullable": true,
                                                            "properties": {
                                                                "arrival_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer"
                                                                },
                                                                "departure_duration": {
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
                                                        "reward": {
                                                            "format": "float",
                                                            "type": "number"
                                                        },
                                                        "visits": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "nullable": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 1,
                                                            "type": "array",
                                                            "uniqueItems": true
                                                        }
                                                    },
                                                    "required": [
                                                        "key",
                                                        "location",
                                                        "visits",
                                                        "duration",
                                                        "reward"
                                                    ],
                                                    "type": "object"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "maxItems": 1000,
                                        "minItems": 0,
                                        "type": "array",
                                        "uniqueItems": true
                                    }
                                },
                                "required": [
                                    "key",
                                    "trip_time"
                                ],
                                "type": "object"
                            },
                            "working_time": {
                                "additionalProperties": false,
                                "properties": {
                                    "from": {
                                        "format": "date-time",
                                        "type": "string"
                                    },
                                    "to": {
                                        "format": "date-time",
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "from",
                                    "to"
                                ],
                                "type": "object"
                            }
                        },
                        "required": [
                            "availability_time",
                            "working_time"
                        ],
                        "type": "object"
                    },
                    "maxItems": 100,
                    "minItems": 1,
                    "type": "array",
                    "uniqueItems": true
                },
                "start_location": {
                    "additionalProperties": false,
                    "nullable": true,
                    "properties": {
                        "arrival_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer"
                        },
                        "departure_duration": {
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
                "tariff": {
                    "additionalProperties": false,
                    "properties": {
                        "basic": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "cost_per_meter": {
                                    "format": "float",
                                    "type": "number"
                                },
                                "cost_per_minute": {
                                    "format": "float",
                                    "type": "number"
                                },
                                "cost_per_shift": {
                                    "format": "float",
                                    "type": "number"
                                },
                                "max_length": {
                                    "format": "float",
                                    "minimum": 1,
                                    "type": "number"
                                },
                                "max_time": {
                                    "format": "float",
                                    "minimum": 1,
                                    "type": "number"
                                }
                            },
                            "required": [
                                "cost_per_shift",
                                "cost_per_meter",
                                "max_length",
                                "cost_per_minute",
                                "max_time"
                            ],
                            "type": "object"
                        },
                        "extra": {
                            "items": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "cost_per_meter": {
                                        "format": "float",
                                        "type": "number"
                                    },
                                    "cost_per_minute": {
                                        "format": "float",
                                        "type": "number"
                                    },
                                    "cost_per_shift": {
                                        "format": "float",
                                        "type": "number"
                                    },
                                    "max_length": {
                                        "format": "float",
                                        "minimum": 1,
                                        "type": "number"
                                    },
                                    "max_time": {
                                        "format": "float",
                                        "minimum": 1,
                                        "type": "number"
                                    }
                                },
                                "required": [
                                    "cost_per_shift",
                                    "cost_per_meter",
                                    "max_length",
                                    "cost_per_minute",
                                    "max_time"
                                ],
                                "type": "object"
                            },
                            "maxItems": 10,
                            "minItems": 0,
                            "type": "array"
                        }
                    },
                    "required": [
                        "basic"
                    ],
                    "type": "object"
                },
                "transport_type": {
                    "default": "CAR",
                    "enum": [
                        "CAR",
                        "TRUCK",
                        "CAR_GT",
                        "TUK_TUK",
                        "BICYCLE",
                        "PEDESTRIAN",
                        "PUBLIC_TRANSPORT"
                    ],
                    "type": "string"
                }
            },
            "required": [
                "key",
                "transport_type",
                "shifts",
                "tariff"
            ],
            "type": "object"
        },
        "settings": {
            "additionalProperties": false,
            "properties": {
                "configuration": {
                    "default": "optimize_money",
                    "type": "string"
                },
                "flight_distance": {
                    "default": false,
                    "type": "boolean"
                },
                "planning_time": {
                    "default": 20,
                    "format": "int32",
                    "maximum": 1440,
                    "minimum": 1,
                    "type": "integer"
                },
                "predict_slots": {
                    "default": 0,
                    "format": "int32",
                    "maximum": 4,
                    "minimum": 0,
                    "type": "integer"
                },
                "result_timezone": {
                    "default": 0,
                    "format": "int32",
                    "maximum": 11,
                    "minimum": -11,
                    "type": "integer"
                },
                "result_ttl": {
                    "default": 20,
                    "format": "int32",
                    "maximum": 1440,
                    "minimum": 1,
                    "type": "integer"
                },
                "routing": {
                    "items": {
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
                            "traffic_jams": {
                                "items": {
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
                                        "time_window": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "from": {
                                                    "format": "date-time",
                                                    "type": "string"
                                                },
                                                "to": {
                                                    "format": "date-time",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "from",
                                                "to"
                                            ],
                                            "type": "object"
                                        }
                                    },
                                    "required": [
                                        "time_window",
                                        "matrix"
                                    ],
                                    "type": "object"
                                },
                                "maxItems": 24,
                                "minItems": 0,
                                "type": "array",
                                "uniqueItems": true
                            },
                            "transport_type": {
                                "default": "CAR",
                                "enum": [
                                    "CAR",
                                    "TRUCK",
                                    "CAR_GT",
                                    "TUK_TUK",
                                    "BICYCLE",
                                    "PEDESTRIAN",
                                    "PUBLIC_TRANSPORT"
                                ],
                                "type": "string"
                            }
                        },
                        "required": [
                            "transport_type",
                            "matrix"
                        ],
                        "type": "object"
                    },
                    "maxItems": 7,
                    "minItems": 1,
                    "type": "array",
                    "uniqueItems": true
                },
                "traffic_jams": {
                    "default": true,
                    "type": "boolean"
                },
                "transport_factor": {
                    "items": {
                        "additionalProperties": false,
                        "properties": {
                            "speed": {
                                "default": 1,
                                "format": "float",
                                "type": "number"
                            },
                            "transport_type": {
                                "default": "CAR",
                                "enum": [
                                    "CAR",
                                    "TRUCK",
                                    "CAR_GT",
                                    "TUK_TUK",
                                    "BICYCLE",
                                    "PEDESTRIAN",
                                    "PUBLIC_TRANSPORT"
                                ],
                                "type": "string"
                            }
                        },
                        "required": [
                            "transport_type",
                            "speed"
                        ],
                        "type": "object"
                    },
                    "maxItems": 7,
                    "minItems": 0,
                    "type": "array",
                    "uniqueItems": true
                }
            },
            "type": "object"
        }
    },
    "required": [
        "performer",
        "orders"
    ],
    "type": "object"
}'''