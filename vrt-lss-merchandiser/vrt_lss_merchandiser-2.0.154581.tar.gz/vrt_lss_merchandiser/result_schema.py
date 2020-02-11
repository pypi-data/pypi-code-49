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
        "timetable": {
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
        "unplanned_orders": {
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
                    },
                    "reason": {
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
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
            "type": "array"
        }
    },
    "type": "object"
}'''