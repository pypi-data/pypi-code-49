PLAN_TASK_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "hardlinks": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "key": {
                        "type": "string"
                    },
                    "links": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "entity_key": {
                                    "type": "string"
                                },
                                "type": {
                                    "enum": [
                                        "ORDER",
                                        "SHIFT"
                                    ],
                                    "type": "string"
                                }
                            },
                            "required": [
                                "type",
                                "entity_key"
                            ],
                            "type": "object"
                        },
                        "maxItems": 10,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true
                    }
                },
                "required": [
                    "key",
                    "links"
                ],
                "type": "object"
            },
            "maxItems": 1000,
            "minItems": 0,
            "type": "array",
            "uniqueItems": true
        },
        "locations": {
            "items": {
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                    "key": {
                        "type": "string"
                    },
                    "load_windows": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "gates_count": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer"
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
                            "type": "object"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
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
                    "transport_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    }
                },
                "required": [
                    "key",
                    "location"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "orders": {
            "items": {
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                    "cargos": {
                        "items": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "capacity": {
                                    "additionalProperties": false,
                                    "nullable": true,
                                    "properties": {
                                        "capacity_x": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "capacity_y": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "capacity_z": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "mass": {
                                            "default": 1,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "volume": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "mass"
                                    ],
                                    "type": "object"
                                },
                                "height": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number"
                                },
                                "key": {
                                    "type": "string"
                                },
                                "length": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number"
                                },
                                "max_storage_time": {
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "restrictions": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true
                                },
                                "width": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number"
                                }
                            },
                            "required": [
                                "key",
                                "capacity"
                            ],
                            "type": "object"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "demands": {
                        "items": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "demand_type": {
                                    "enum": [
                                        "PICKUP",
                                        "DROP",
                                        "WORK"
                                    ],
                                    "type": "string"
                                },
                                "key": {
                                    "type": "string"
                                },
                                "possible_events": {
                                    "items": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "duration": {
                                                "default": 5,
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "location_key": {
                                                "type": "string"
                                            },
                                            "reward": {
                                                "default": 10000,
                                                "format": "float",
                                                "type": "number"
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
                                            "location_key",
                                            "duration",
                                            "time_window",
                                            "reward"
                                        ],
                                        "type": "object"
                                    },
                                    "maxItems": 10,
                                    "minItems": 1,
                                    "type": "array",
                                    "uniqueItems": true
                                },
                                "precedence_in_order": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "precedence_in_trip": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "target_cargos": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxItems": 1000,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true
                                }
                            },
                            "required": [
                                "key",
                                "demand_type",
                                "possible_events"
                            ],
                            "type": "object"
                        },
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "key": {
                        "type": "string"
                    },
                    "order_features": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "order_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "performer_blacklist": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "performer_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    }
                },
                "required": [
                    "key",
                    "demands"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "performers": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "key": {
                        "type": "string"
                    },
                    "max_work_shifts": {
                        "format": "int32",
                        "type": "integer"
                    },
                    "own_transport_type": {
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
                    },
                    "performer_features": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "transport_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    }
                },
                "required": [
                    "key"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
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
                    "finish_location_key": {
                        "type": "string"
                    },
                    "key": {
                        "type": "string"
                    },
                    "resource_key": {
                        "type": "string"
                    },
                    "shift_type": {
                        "enum": [
                            "PERFORMER",
                            "TRANSPORT"
                        ],
                        "type": "string"
                    },
                    "start_location_key": {
                        "type": "string"
                    },
                    "tariff": {
                        "additionalProperties": false,
                        "properties": {
                            "constraints": {
                                "items": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "cost_per_unit": {
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "stage_length": {
                                            "format": "float",
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "stage_length",
                                        "cost_per_unit"
                                    ],
                                    "type": "object"
                                },
                                "maxItems": 100,
                                "minItems": 1,
                                "type": "array",
                                "uniqueItems": true
                            },
                            "cost_per_shift": {
                                "format": "float",
                                "type": "number"
                            }
                        },
                        "required": [
                            "cost_per_shift",
                            "constraints"
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
                    "key",
                    "shift_type",
                    "resource_key",
                    "availability_time",
                    "working_time",
                    "tariff"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "transports": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "boxes": {
                        "items": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "capacity": {
                                    "additionalProperties": false,
                                    "nullable": true,
                                    "properties": {
                                        "capacity_x": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "capacity_y": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "capacity_z": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "mass": {
                                            "default": 1,
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "volume": {
                                            "default": 0,
                                            "format": "float",
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "mass"
                                    ],
                                    "type": "object"
                                },
                                "features": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true
                                },
                                "height": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number"
                                },
                                "key": {
                                    "type": "string"
                                },
                                "length": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number"
                                },
                                "width": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number"
                                }
                            },
                            "required": [
                                "key",
                                "capacity"
                            ],
                            "type": "object"
                        },
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "key": {
                        "type": "string"
                    },
                    "performer_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "transport_features": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 1000,
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
                    "key"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        }
    },
    "required": [
        "locations",
        "orders",
        "performers",
        "transports",
        "shifts"
    ],
    "type": "object"
}'''