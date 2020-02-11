PLAN_RESULT_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "progress": {
            "format": "int32",
            "maximum": 100,
            "minimum": 0,
            "type": "integer"
        },
        "statistics": {
            "additionalProperties": false,
            "nullable": true,
            "properties": {
                "total_statistics": {
                    "additionalProperties": false,
                    "nullable": true,
                    "properties": {
                        "capacity_utilization": {
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
                        "cost": {
                            "format": "float",
                            "type": "number"
                        },
                        "measurements": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "arriving_time": {
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "departure_time": {
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "distance": {
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "driving_time": {
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
                                },
                                "total_time": {
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "waiting_time": {
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "working_time": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "driving_time",
                                "waiting_time",
                                "working_time",
                                "arriving_time",
                                "departure_time",
                                "total_time",
                                "time_window",
                                "distance"
                            ],
                            "type": "object"
                        },
                        "orders_count": {
                            "format": "int32",
                            "type": "integer"
                        },
                        "performers_count": {
                            "format": "int32",
                            "type": "integer"
                        },
                        "reward": {
                            "format": "float",
                            "type": "number"
                        }
                    },
                    "required": [
                        "cost",
                        "reward",
                        "measurements",
                        "orders_count",
                        "performers_count"
                    ],
                    "type": "object"
                },
                "trips_statistics": {
                    "items": {
                        "additionalProperties": false,
                        "nullable": true,
                        "properties": {
                            "max_load": {
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
                                    "count": {
                                        "format": "int32",
                                        "type": "integer"
                                    }
                                },
                                "required": [
                                    "count",
                                    "capacity"
                                ],
                                "type": "object"
                            },
                            "statistics": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "capacity_utilization": {
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
                                    "cost": {
                                        "format": "float",
                                        "type": "number"
                                    },
                                    "measurements": {
                                        "additionalProperties": false,
                                        "nullable": true,
                                        "properties": {
                                            "arriving_time": {
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "departure_time": {
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "distance": {
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "driving_time": {
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
                                            },
                                            "total_time": {
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "waiting_time": {
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "working_time": {
                                                "format": "int32",
                                                "type": "integer"
                                            }
                                        },
                                        "required": [
                                            "driving_time",
                                            "waiting_time",
                                            "working_time",
                                            "arriving_time",
                                            "departure_time",
                                            "total_time",
                                            "time_window",
                                            "distance"
                                        ],
                                        "type": "object"
                                    },
                                    "orders_count": {
                                        "format": "int32",
                                        "type": "integer"
                                    },
                                    "performers_count": {
                                        "format": "int32",
                                        "type": "integer"
                                    },
                                    "reward": {
                                        "format": "float",
                                        "type": "number"
                                    }
                                },
                                "required": [
                                    "cost",
                                    "reward",
                                    "measurements",
                                    "orders_count",
                                    "performers_count"
                                ],
                                "type": "object"
                            },
                            "stop_statistics": {
                                "items": {
                                    "additionalProperties": false,
                                    "nullable": true,
                                    "properties": {
                                        "current_load": {
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
                                                "count": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "count",
                                                "capacity"
                                            ],
                                            "type": "object"
                                        },
                                        "demand_ids": {
                                            "items": {
                                                "type": "string"
                                            },
                                            "type": "array"
                                        },
                                        "download": {
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
                                                "count": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "count",
                                                "capacity"
                                            ],
                                            "type": "object"
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
                                        "measurements": {
                                            "additionalProperties": false,
                                            "nullable": true,
                                            "properties": {
                                                "arriving_time": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                },
                                                "departure_time": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                },
                                                "distance": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                },
                                                "driving_time": {
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
                                                },
                                                "total_time": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                },
                                                "waiting_time": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                },
                                                "working_time": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "driving_time",
                                                "waiting_time",
                                                "working_time",
                                                "arriving_time",
                                                "departure_time",
                                                "total_time",
                                                "time_window",
                                                "distance"
                                            ],
                                            "type": "object"
                                        },
                                        "upload": {
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
                                                "count": {
                                                    "format": "int32",
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "count",
                                                "capacity"
                                            ],
                                            "type": "object"
                                        }
                                    },
                                    "required": [
                                        "location",
                                        "measurements"
                                    ],
                                    "type": "object"
                                },
                                "type": "array"
                            },
                            "total_load": {
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
                                    "count": {
                                        "format": "int32",
                                        "type": "integer"
                                    }
                                },
                                "required": [
                                    "count",
                                    "capacity"
                                ],
                                "type": "object"
                            },
                            "trip_key": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "trip_key",
                            "statistics",
                            "stop_statistics"
                        ],
                        "type": "object"
                    },
                    "type": "array"
                }
            },
            "required": [
                "total_statistics",
                "trips_statistics"
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
        },
        "trips": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "actions": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "cargo_placements": {
                                    "items": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "box_key": {
                                                "type": "string"
                                            },
                                            "cargo_key": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "box_key",
                                            "cargo_key"
                                        ],
                                        "type": "object"
                                    },
                                    "maxItems": 1000,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true
                                },
                                "demand_key": {
                                    "type": "string"
                                },
                                "location_key": {
                                    "type": "string"
                                },
                                "order_key": {
                                    "type": "string"
                                },
                                "todolist": {
                                    "items": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "job_time": {
                                                "format": "date-time",
                                                "type": "string"
                                            },
                                            "job_type": {
                                                "enum": [
                                                    "LOCATION_ARRIVAL",
                                                    "READY_TO_WORK",
                                                    "START_WORK",
                                                    "FINISH_WORK",
                                                    "LOCATION_DEPARTURE"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "job_type",
                                            "job_time"
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
                                "order_key",
                                "demand_key",
                                "location_key",
                                "todolist"
                            ],
                            "type": "object"
                        },
                        "maxItems": 1000,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "assigned_shifts": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "shift_key": {
                                    "type": "string"
                                },
                                "shift_time": {
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
                                "shift_key",
                                "shift_time"
                            ],
                            "type": "object"
                        },
                        "maxItems": 2,
                        "minItems": 2,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "key": {
                        "type": "string"
                    },
                    "waitlist": {
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
                    "assigned_shifts"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 0,
            "type": "array",
            "uniqueItems": true
        },
        "unplanned_orders": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "order": {
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
                    "reason": {
                        "type": "string"
                    }
                },
                "required": [
                    "order"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 0,
            "type": "array",
            "uniqueItems": true
        },
        "validations": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "entity_key": {
                        "type": "string"
                    },
                    "entity_type": {
                        "type": "string"
                    },
                    "info": {
                        "type": "string"
                    },
                    "type": {
                        "enum": [
                            "info",
                            "warning",
                            "error"
                        ],
                        "type": "string"
                    }
                },
                "required": [
                    "type",
                    "info"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 0,
            "type": "array",
            "uniqueItems": true
        }
    },
    "required": [
        "trips"
    ],
    "type": "object"
}'''