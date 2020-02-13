# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Methods for AutoML remote runs."""
try:
    from azureml.train.automl.runtime._remote_script import setup_wrapper
    from azureml.train.automl.runtime._remote_script import driver_wrapper
    from azureml.train.automl.runtime._remote_script import model_exp_wrapper
except Exception:
    pass
