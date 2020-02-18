import os
import random
import string
from enum import Enum
from typing import Iterable, Generator, Union
from typing import List
from . import config
from .parsing import parse_constructor_arguments
from subprocess import check_output, CalledProcessError

import pkgutil
import traceback


def rand_string(chars: int):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(chars)
    )


class SubClassFinder:
    @classmethod
    def get_subclasses(cls):
        subclasses = []

        def already_found(subclass: type):
            for s in subclasses:
                if (
                    s.__name__ == subclass.__name__
                    and s.__module__ == subclass.__module__
                ):
                    return True
            return False

        for subclass in cls.__subclasses__():
            subclasses.extend(
                s for s in subclass.get_subclasses() if not already_found(s)
            )
            if not already_found(subclass):
                subclasses.append(subclass)

        return subclasses

    @classmethod
    def get_subclass(cls, name: str):
        for subclass in cls.get_subclasses():
            if subclass.__name__ == name:
                return subclass


class Permanent(SubClassFinder):
    def __init__(self, obj_ref: str = ""):
        self.obj_ref = obj_ref
        if obj_ref == "":
            self.obj_ref = self.__class__.__name__ + "_" + rand_string(8)


class AnnotatedData(SubClassFinder):
    """
    A Interface to create training datasets that could be passed di AIModels
    """

    def __init__(self, data_path: str, batch_size: int = 1, sequence_length: int = 1):
        """
        Args:
            data_path: Path where to find the data
            batch_size: The number of examples that will be returned by the training and
                valdiation method
            sequence_length: The length of a sequence for spatial data
        """
        super().__init__()
        self.data_path = os.path.join(config.AYDA_DATA_PATH, data_path)
        self.batch_size = batch_size
        self.sequence_length = sequence_length

    def training(self) -> Union[Iterable, Generator]:
        """
        Must return a generator or a iterable to access training data
        Returns: A iterator for training data

        """
        raise NotImplementedError

    def validation(self) -> Union[Iterable, Generator]:
        """
        Must return a generator or a iterable to access validation data
        Returns: A iterator for validation data

        """
        raise NotImplementedError

    def get_data_shape(self) -> tuple:
        """
        Must return the shape of a single batch returned by validation and training
        generator or shape shape of the data
        in the from [xshape, yshape]

        Returns: The shape of the data

        """
        raise NotImplementedError


class AIModel(SubClassFinder):
    """
    A Interface for AIModels
    """

    def __init__(self):
        super().__init__()

    def train(
        self,
        data: AnnotatedData,
        model_dir: str,
        epochs: int = 1,
        epoch_size: int = 10,
        validation_size: int = 0,
        timeout_secs: int = 0,
        pretrained_model_name: str = "",
        callbacks: List = None,
    ) -> str:
        """
        Configures the model, and starts the training

        Args:
            data: The TrainingData to run the training on
            model_dir: The path to store model parameters and training information to
            epochs: The number of epochs to train
            epoch_size: The number of batches per epoch for training
            validation_size: The number of batches per epoch for validation
            timeout_secs: Time in seconds until the training should be stopped
            pretrained_model_name: The file name to be loaded before training to
                continue from pretrained model. This must be placed int model_dir
            callbacks: List of callbacks that will be used during training e.g. for
                uploading metrics

        Returns: The path to the trained model file

        """
        raise NotImplementedError

    @classmethod
    def is_valid_shape(cls, shape: tuple) -> bool:
        """
        Must return True if the  model can accept the data shape passed

        Returns: Return True if the  model can accept the data shape passed

        """
        return len(shape) > 0

    @staticmethod
    def checkpoint_model_file_pattern():
        return "*.h5"


class JobState(Enum):
    CREATED = "Created"
    INACTIVE = "Inactive"
    TRANSFERRED = "Transferred"
    ACTIVE = "Active"
    DONE = "Done"
    CANCELLED = "Cancelled"


class TrainingOptions(Permanent):
    def __init__(
        self,
        epochs: int = 1,
        epoch_size: int = 10,
        validation_size: int = 0,
        timeout_secs: int = 0,
    ):
        super().__init__()
        self.timeout_secs = timeout_secs
        self.validation_size = validation_size
        self.epoch_size = epoch_size
        self.epochs = epochs


class RepositoryBranch(Permanent):
    def __init__(self, name: str, repo: str, commits: List[str] = None):
        super().__init__("{}.{}".format(repo, name))
        self.name = name
        self.repo = repo
        if commits is None:
            commits = []
        self.commits = commits


class RepositoryConfig(Permanent):
    def __init__(
        self, name: str, url: str, branch: str = "master", ssh_key: str = "",
    ):
        super().__init__(name)
        self.name = name
        self.url = url
        self.branch = branch
        self.ssh_key = ssh_key


class DockerConfig(Permanent):
    def __init__(self, image_name: str, url: str = "", key: str = ""):
        super().__init__(image_name)
        self.image_name = image_name
        self.url = url
        self.key = key


class ClientState(Enum):
    ACTIVE = "Active"
    WAITING = "Waiting"
    INACTIVE = "Inactive"
    STARTING = "Starting"


class ClientRegisterInfo(Permanent):
    def __init__(
        self,
        pw_hash: str,
        username: str,
        client_state: str,
        is_google: bool = False,
        last_active: float = 0.0,
        docker: DockerConfig = None,
        repo: RepositoryConfig = None,
        storage: str = "",
        compute_type: str = "",
        checkout: str = "",
    ):
        super().__init__(username)
        self.is_google = is_google
        self.username = username
        if username == "":
            self.username = self.obj_ref
        self.client_state = client_state
        self.pw_hash = pw_hash
        self.last_active = last_active
        self.docker = docker
        self.repos = repo
        self.checkout = checkout
        self.storage = storage
        self.compute_type = compute_type


class JobInfo(Permanent):
    def __init__(
        self,
        creation_date: float,
        train_options: TrainingOptions,
        model_parameter: dict,
        training_data: dict,
        obj_ref: str = "",
        start_time: float = -1,
        run_time: float = -1,
        end_time: float = -1,
        status: str = JobState.CREATED.name,
        job_name: str = "",
        project: str = "",
        target_machine: ClientRegisterInfo = None,
        pretrained_model: str = "",
    ):
        super().__init__(obj_ref)
        self.train_options = train_options
        self.training_data = training_data
        self.creation_date = creation_date
        self.job_name = job_name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.run_time = run_time
        self.model_parameter = model_parameter
        self.target_machine = target_machine
        self.project = project
        self.pretrained_model = pretrained_model

    def _rand_string(self, chars: int = 10):
        return "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(chars)
        )


class EpochTrainResult(Permanent):
    def __init__(self, epoch: int, job_ref: str, metrics: dict):
        super().__init__()
        self.metrics = metrics
        self.epoch = epoch
        self.job_ref = job_ref


class ClassTemplate(Permanent):
    def __init__(
        self, class_name: str, package: str, description: dict, version: str = ""
    ):
        super().__init__("{}.{}.{}".format(package, class_name, version))
        self.class_name = class_name
        self.package = package
        self.description = description
        self.version = version

    @classmethod
    def from_desc(cls, desc: dict):
        module = desc["module"]
        if "." in module:
            module = module.split(".")[0]
        name = desc["class"]
        version = desc["version"] if "version" in desc else ""
        return cls(name, module, desc, version)

    @classmethod
    def from_type(cls, class_type: type):
        desc = parse_constructor_arguments(class_type)
        return cls.from_desc(desc)

    @classmethod
    def from_object(cls, obj: object):
        desc = parse_constructor_arguments(obj.__class__, default_object=obj)
        return cls.from_desc(desc)


class ModelTemplate(ClassTemplate):
    pass


class DatasetTemplate(ClassTemplate):
    pass


class ClientMode(Enum):
    # This client is only started for one job and afterwards it is shutted down
    ONE_JOB = "ONE_JOB"
    # client is started and can process multiple jobs in a row
    MULTIPLE_JOB = "MULTIPLE_JOB"


def get_git_version() -> str:
    try:
        commit = check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
        return commit
    except CalledProcessError:
        return ""


def get_git_branch() -> str:
    try:
        branch = (
            check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        )
        return branch
    except CalledProcessError:
        return ""


def get_compatible_classes(path_list):
    all_modules = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(path_list):
        if module_name == "setup":
            continue
        all_modules.append(module_name)
        try:
            _module = loader.find_module(module_name).load_module(module_name)
            globals()[module_name] = _module
        except Exception as e:
            print("Failed to load module {}: {}".format(module_name, e))
            traceback.print_exc()
    models = AIModel.get_subclasses()
    datasets = AnnotatedData.get_subclasses()
    version = get_git_version()
    branch = get_git_branch()
    parsed_models = [parse_constructor_arguments(m, version=version) for m in models]
    parsed_datasets = [
        parse_constructor_arguments(d, version=version) for d in datasets
    ]
    return {"models": parsed_models, "datasets": parsed_datasets, "branch": branch}


class Project(Permanent):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
