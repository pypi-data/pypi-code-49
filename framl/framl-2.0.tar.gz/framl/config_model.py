import yaml

from framl.config import Config


class ConfigModel(Config):

    def __init__(self, project_path):
        self._mc = yaml.safe_load(open(project_path + "/config.yaml"))

        # project
        self._gcp_project_id: str = None
        self._model_name: str = None
        self._model_version: str = None

        # flags
        self._refresh_rate: int = None
        self._declared_flags: list = None

        # model intput/output
        self._features: dict = None
        self._model_output: dict = None

    def _load_main(func):
        def wrapper(self):
            if self._model_name is None:

                # gcp project id
                self._gcp_project_id = Config.get_key('gcp_project_id', self._mc)
                if self._gcp_project_id is None:
                    raise Exception(f'Config file is missing the GCP project ID. Check your config.yaml')

                self._model_name = Config.get_key('name', self._mc)
                if self._model_name is None:
                    raise Exception(f'Config file is missing the algo name. Check your config.yaml')

                self._model_version = Config.get_key('version', self._mc)
                if self._model_version is None or not isinstance(self._model_version, int):
                    raise Exception(f'Config file is missing the algo version or version is not an integer. '
                                    f'Check your config.yaml')

                self._features = Config.get_key('features', self._mc)
                self._model_output = Config.get_key('model_output', self._mc)
                ConfigModel._validate_features(self._features)

                if len({**self._features, **self._model_output}) != len(self._features) + len(self._model_output):
                    raise Exception('You can not use the same params name for input features and model output. '
                                    'Check your config.yaml')

            return func(self)

        return wrapper

    def _load_flags(func):
        def wrapper(self):
            if self._declared_flags is None:

                if not Config.keys_exist(['flags', 'flags_refresh_rate'], self._mc):
                    raise Exception(f'Invalid flags configuration. Check your config.yaml')

                if len(self._mc['flags']) <= 0 or not isinstance(self._mc['flags'], list):
                    raise Exception(f"Wrong flag declaration: "
                                    f"{self._mc['flags']}, make sure you're using a list. Check your config.yaml")

                self._refresh_rate = Config.get_key('flags_refresh_rate', self._mc)
                self._declared_flags = Config.get_key('flags', self._mc)

            return func(self)

        return wrapper

    @staticmethod
    def _validate_features(features: dict) -> None:
        if len(features) == 0:
            raise Exception('You must declare input features. Check your config.yaml')

        # for key, params in features.items():
        #     if "dimension" in params and params.get("dimension") in [1, 2, 3]:
        #         return
        # raise Exception(
        #     'At least one feature must be a dimension (for example: user_id, trip_id, campaign_id...).'
        #     'Check your config.yaml')

    @_load_main
    def get_gcp_project_id(self) -> str:
        return self._gcp_project_id

    @_load_main
    def get_model_name(self) -> str:
        return self._model_name

    @_load_main
    def get_model_version(self) -> str:
        return self._model_version

    @_load_main
    def get_features(self) -> dict:
        return self._features

    @_load_main
    def get_model_output(self) -> dict:
        return self._model_output

    @_load_main
    def get_input_and_output_params(self) -> dict:
        return {"input" : self.get_features(), "output": self.get_model_output()}
        #return {**self._features, **self._model_output}

    def get_monitored_fields(self) -> dict:
        fields = self.get_input_and_output_params()

        input_features = {}
        for field_name, params in fields.get("input").items():
            if "monitored" not in params or params.get("monitored") is not True:
                continue

            input_features[field_name] = params.get("data_type")

        output = {}
        for field_name, params in fields.get("output").items():
            if "monitored" not in params or params.get("monitored") is not True:
                continue

            output[field_name] = params.get("data_type")

        return {"input":input_features, "output": output}

    # Flags
    @_load_flags
    def get_refresh_rate(self) -> int:
        return self._refresh_rate

    @_load_flags
    def get_declared_flags(self) -> list:
        return self._declared_flags
