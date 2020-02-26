# Copyright (C) 2019  Neural Concept SA

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ========================================================================
from ncapi_client.utils import AttrDict, map_response, handle_response, merge_dicts
from halo import HaloNotebook
import numpy as np
import math
from time import sleep
from ncapi_client.trained_model import TrainedModel


class Training:
    """Training"""

    def __init__(self, client, uuid):
        """__init__

        Args:
            client: API client
            uuid (str): uuid or name of the model
        """
        self._session = client._session
        self.url = client.url
        self.uuid = uuid

    @staticmethod
    def submit(
        client,
        dataset_id,
        model_class="ncs.models.point_regressor.PointRegressor",
        network_complexity=0,
        log_transform_input_fields=False,
        normalize_input_fields=False,
        log_transform_input_scalars=False,
        normalize_input_scalars=False,
        log_transform_output_fields=False,
        normalize_output_fields=False,
        log_transform_output_scalars=False,
        normalize_output_scalars=False,
        restore_from=None,
        user_config=None,
    ):
        """Submit a new training to the API

        Args:
            client: API client
            dataset_id (str): uuid or name of the dataset to use for training.
            model_class (str): class of model to use.
            network_complexity (float): complexity of the model from 0 to 10 (based on EfficientNet framework).
            log_transform_input_fields (bool): whether to log transform the input fields in the dataset.
            normalize_input_fields (bool): whether to normalize the input fields in dataset.
            log_transform_input_scalars (bool): whether to log transform the input scalars in the dataset.
            normalize_input_scalars (bool): whether to normalize the input scalars in dataset.
            log_transform_output_fields (bool): whether to log transform the output fields in the dataset.
            normalize_output_fields (bool): whether to normalize the output fields in dataset.
            log_transform_output_scalars (bool): whether to log transform the output scalars in the dataset.
            normalize_output_scalars (bool): whether to normalize the output scalars in dataset.
            restore_from (str): uuid or name of a trained model to restore the training from.
            user_config (dict): custom config override.

        Returns:
            New Training
        """
        payload = dict(dataset_id=dataset_id)
        user_config = {} if not user_config else user_config

        if restore_from:
            payload["restore_from"] = restore_from
        else:
            # Configure the model
            model_config = dict(class_name=model_class)
            model_params_complexity = Training._network_complexity(network_complexity)
            model_config.update(model_params_complexity)

            normalization_params = Training._normalization_config(log_transform_input_scalars,
                                                                  normalize_input_scalars,
                                                                  log_transform_input_fields,
                                                                  normalize_input_fields,
                                                                  log_transform_output_scalars,
                                                                  normalize_output_scalars,
                                                                  log_transform_output_fields,
                                                                  normalize_output_fields)
            model_config["normalizations"] = normalization_params
            config = dict(model=model_config)
            user_config = merge_dicts(config, user_config)

        payload["user_config"] = user_config
        resp = handle_response(
            client._session.post(f"{client.url}/api/training/submit", json=payload)
        )
        return Training(client, resp["uuid"])

    @map_response
    def delete(self):
        """delete this training

        Returns:
            AttrDict: API reponse
        """
        return self._session.delete(f"{self.url}/api/training/{self.uuid}")

    @property
    @map_response
    def info(self):
        """Get verbose info about the training

       Returns:
            AttrDict: The API response
        """
        return self._session.get(f"{self.url}/api/training/{self.uuid}")

    @map_response
    def stop(self):
        """stop this training

        Returns:
            AttrDict: API reponse
        """
        return self._session.post(f"{self.url}/api/training/{self.uuid}/stop")

    @map_response
    def restart(self):
        """restart this training

        Returns:
            AttrDict: API reponse
        """
        return self._session.post(f"{self.url}/api/training/{self.uuid}/restart")

    @map_response
    def cancel(self):
        """cancel this training"""
        return self._session.post(f"{self.url}/api/training/{self.uuid}/cancel")

    @property
    @map_response
    def logs(self):
        """Get training logs

        Returns:
            AttrDict: logs
        """
        return self._session.get(f"{self.url}/api/training/{self.uuid}/logs")

    @property
    @map_response
    def checkpoints(self):
        """Get training checkpoints

        Returns:
            AttrDict: checkpoints
        """
        return self._session.get(f"{self.url}/api/training/{self.uuid}/checkpoints")

    def save(self, checkpoint_id=None, name=None):
        """Save one of the training checkpoints (if any) as a trained model

        Args:
            checkpoint_id (str): id of the checkpoint to save, defaults to lates
            name (str): name of the saved model, defaults to auto generated

        Returns:
            upon success, a description of the newly created trained model.
        """
        payload = {}
        if checkpoint_id:
            payload["checkpoint_id"] = checkpoint_id
        else:
            payload["checkpoint_id"] = self.checkpoints["checkpoints"][-1]
        if name:
            payload["name"] = name
        resp = handle_response(
            self._session.post(
                f"{self.url}/api/training/{self.uuid}/save", json=payload
            )
        )
        return TrainedModel(
            AttrDict(url=self.url, _session=self._session), resp["uuid"]
        )

    def monitor(self):
        """Plot an interactive graph monitoring training metrics"""
        # we don't want to import these at modulke level, only if we need rendering
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation

        logs = self.logs

        create_plot = True
        status = "RUNNING"
        while status == "RUNNING":
            if create_plot:
                fig = plt.figure(figsize=(10, 8))
                ax = fig.add_subplot(111)
                plt.ion()
                create_plot = False
            else:
                ax.clear()

            if len(logs.train) < 3:
                status = self.info["status"].split(".")[1]
                losses_train = np.array([[0, 1], [1, 1]])
                losses_val = np.array([[0, 1], [1, 1]])

            else:
                losses_train = np.array([[l["step"], l["loss"]] for l in logs.train])
                losses_val = np.array([[l["step"], l["loss"]] for l in logs.val])

            ax.plot(losses_train[:, 0], losses_train[:, 1], label="train")
            ax.plot(losses_val[:, 0], losses_val[:, 1], label="val")
            plt.xlabel("step")
            plt.ylabel("loss")
            fig.legend()

            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.subplots_adjust(bottom=0.30)
            logs = self.logs
            status = self.info["status"].split(".")[1]
            sleep(3)

    @classmethod
    def _network_complexity(cls, index):
        """Model config from complexity based on efficient net framework.
        Args:
            index: network complexity index from scale 0 to 10.

        Returns:
            model configurations dict corresponding to the input network complexity.

        """

        default_conf = AttrDict.convert(
            {
                "top_pointnet": {"n_layers": 2, "n_features": [8, 32]},
                "top_resnet": {"n_layers": 3, "n_features_out": 64},
                "pooling": {
                    "n_layers": 3,
                    "n_pointwise_filters": 32,
                    "num_centroids": [2000, 100, 10],
                },
                "bottom_resnet": {"n_layers": 3, "n_features_out": 32},
            }
        )

        coeff_layers = 1.4 ** index
        coeff_fts = 1.2 ** index

        default_conf.top_pointnet.n_layers = round(
            default_conf.top_pointnet.n_layers * coeff_layers
        )

        start = round(default_conf.top_pointnet.n_features[0] * coeff_fts)
        stop = round(default_conf.top_pointnet.n_features[1] * coeff_fts)

        step = math.floor((stop - start) / (default_conf.top_pointnet.n_layers - 1))
        fts = [start + i * step for i in range(default_conf.top_pointnet.n_layers)]

        default_conf.top_pointnet.n_features = fts

        default_conf.top_resnet.n_layers = round(
            default_conf.top_resnet.n_layers * coeff_layers
        )
        default_conf.top_resnet.n_features_out = round(
            default_conf.top_resnet.n_features_out * coeff_fts
        )

        default_conf.bottom_resnet.n_layers = round(
            default_conf.bottom_resnet.n_layers * coeff_layers
        )
        default_conf.bottom_resnet.n_features_out = round(
            default_conf.bottom_resnet.n_features_out * coeff_fts
        )
        return default_conf

    @classmethod
    def _normalization_config(
        cls,
        log_transform_input_fields,
        normalize_input_fields,
        log_transform_input_scalars,
        normalize_input_scalars,
        log_transform_output_fields,
        normalize_output_fields,
        log_transform_output_scalars,
        normalize_output_scalars,
    ):

        norms = {
            "input_fields": [],
            "input_scalars": [],
            "output_fields": [],
            "output_scalars": [],
        }

        log_transform_config = {"transformation": "log_scaling", "pretraining": True}

        normalize_config = {"transformation": "gaussian_scaling", "pretraining": False}

        if log_transform_input_fields:
            norms["input_fields"].append(log_transform_config)
        if normalize_input_fields:
            norms["input_fields"].append(normalize_config)

        if log_transform_input_scalars:
            norms["input_scalars"].append(log_transform_config)
        if normalize_input_scalars:
            norms["input_scalars"].append(normalize_config)

        if log_transform_output_fields:
            norms["output_fields"].append(log_transform_config)
        if normalize_output_fields:
            norms["output_fields"].append(normalize_config)

        if log_transform_output_scalars:
            norms["output_scalars"].append(log_transform_config)
        if normalize_output_scalars:
            norms["output_scalars"].append(normalize_config)

        return norms
