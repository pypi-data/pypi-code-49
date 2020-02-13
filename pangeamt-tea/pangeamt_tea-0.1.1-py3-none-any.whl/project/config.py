import yaml
from autoclass import autoclass
import pathlib
from typing import Optional, Dict
import os


@autoclass
class Config:
    DATA_DIR = "data"

    def __init__(
        self,
        project_dir: pathlib.Path,
        customer: str,
        src_lang: str,
        tgt_lang: str,
        flavor: Optional[str] = None,
        version=1,
        processors: Dict = None,
        tokenizer: Dict = None,
        truecaser: Dict = None,
        bpe: Dict = None,
        translation_model: Dict = None,
    ):
        self.data_dir = project_dir.joinpath(Config.DATA_DIR)

    # Takes the path to the config and returns a Config object
    @staticmethod
    def load(project_dir: pathlib.Path) -> "Config":
        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        return Config(
            project_dir,
            data["customer"],
            data["src_lang"],
            data["tgt_lang"],
            data["flavor"],
            data["version"],
            data["processors"],
            data["tokenizer"],
            data["truecaser"],
            data["bpe"],
            data["translation_model"],
        )

    # Writes the state of the Config object to the config file
    def save(self) -> None:
        with open(self.project_dir.joinpath("config.yml"), "w") as file:
            data = {
                "customer": self.customer,
                "src_lang": self.src_lang,
                "tgt_lang": self.tgt_lang,
                "flavor": self.flavor,
                "version": self.version,
                "processors": self.processors,
                "tokenizer": self.tokenizer,
                "truecaser": self.truecaser,
                "bpe": self.bpe,
                "translation_model": self.translation_model,
            }

            yaml.dump(data, file, sort_keys=False)

    # Add the tokenizer info to the config
    @staticmethod
    def add_tokenizer(
        src_tokenizer: str, tgt_tokenizer: str, project_dir: pathlib.Path
    ):
        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            data["tokenizer"] = {"src": src_tokenizer, "tgt": tgt_tokenizer}

            total_data = {
                "customer": data["customer"],
                "src_lang": data["src_lang"],
                "tgt_lang": data["tgt_lang"],
                "flavor": data["flavor"],
                "version": data["version"],
                "processors": data["processors"],
                "tokenizer": data["tokenizer"],
                "truecaser": data["truecaser"],
                "bpe": data["bpe"],
                "translation_model": data["translation_model"],
            }

            with open(project_dir.joinpath("config.yml"), "w") as file_write:
                yaml.dump(total_data, file_write, sort_keys=False)

    # Add the truecaser config info to the config file
    @staticmethod
    def add_truecaser(
        src_truecaser: bool, tgt_truecaser: bool, project_dir: pathlib.Path
    ):
        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            data["truecaser"] = {
                "src": "enabled" if src_truecaser else "disabled",
                "tgt": "enabled" if tgt_truecaser else "disabled",
            }

            total_data = {
                "customer": data["customer"],
                "src_lang": data["src_lang"],
                "tgt_lang": data["tgt_lang"],
                "flavor": data["flavor"],
                "version": data["version"],
                "processors": data["processors"],
                "tokenizer": data["tokenizer"],
                "truecaser": data["truecaser"],
                "bpe": data["bpe"],
                "translation_model": data["translation_model"],
            }

            with open(project_dir.joinpath("config.yml"), "w") as file_write:
                yaml.dump(total_data, file_write, sort_keys=False)

    # Add the processors config info to the config file
    @staticmethod
    def add_processors(processors: str, project_dir: pathlib.Path):
        processors_dict = {}

        # Splits the input string to get a list of processors names and their arguments
        for processor in processors.split(";"):
            if processor:
                # Splits the processor name and the arguments
                p = processor.split(",")
                processor_name = p[0]
                processors_dict[processor_name] = []
                processor_args = p[1:]
                # Eliminates the whitespaces at the left of the arguments and appends to
                # the list of arguments of the processor
                for arg in processor_args:
                    while arg[0] == " ":
                        arg = arg[1:]
                    processors_dict[processor_name].append(arg)
        # Writes the updated config
        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            data["processors"] = processors_dict

            total_data = {
                "customer": data["customer"],
                "src_lang": data["src_lang"],
                "tgt_lang": data["tgt_lang"],
                "flavor": data["flavor"],
                "version": data["version"],
                "processors": data["processors"],
                "tokenizer": data["tokenizer"],
                "truecaser": data["truecaser"],
                "bpe": data["bpe"],
                "translation_model": data["translation_model"],
            }

        with open(project_dir.joinpath("config.yml"), "w") as file_write:
            yaml.dump(total_data, file_write, sort_keys=False)

    # Add the bpe config to the config file
    @staticmethod
    def add_bpe(
        joint: bool,
        num_iterations: int,
        threshold: int,
        project_dir: pathlib.Path,
    ):

        bpe_dict = {
            "joint": joint,
            "threshold": threshold,
            "num_iterations": num_iterations,
        }

        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            data["bpe"] = bpe_dict

            total_data = {
                "customer": data["customer"],
                "src_lang": data["src_lang"],
                "tgt_lang": data["tgt_lang"],
                "flavor": data["flavor"],
                "version": data["version"],
                "processors": data["processors"],
                "tokenizer": data["tokenizer"],
                "truecaser": data["truecaser"],
                "bpe": data["bpe"],
                "translation_model": data["translation_model"],
            }

        with open(project_dir.joinpath("config.yml"), "w") as file_write:
            yaml.dump(total_data, file_write, sort_keys=False)

    # Add the training config to the config file
    @staticmethod
    def add_translation_model(name: str, args: str, project_dir: pathlib.Path):
        translation_model_dict = {
            "name": name,
            "args": args,
        }

        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            data["translation_model"] = translation_model_dict

            total_data = {
                "customer": data["customer"],
                "src_lang": data["src_lang"],
                "tgt_lang": data["tgt_lang"],
                "flavor": data["flavor"],
                "version": data["version"],
                "processors": data["processors"],
                "tokenizer": data["tokenizer"],
                "truecaser": data["truecaser"],
                "bpe": data["bpe"],
                "translation_model": data["translation_model"],
            }

        with open(project_dir.joinpath("config.yml"), "w") as file_write:
            yaml.dump(total_data, file_write, sort_keys=False)

    # Sets to None a section in order to reset it
    @staticmethod
    def reset_section(section: str, project_dir: pathlib.Path):
        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            if section is None:
                for s in [
                    "bpe",
                    "truecaser",
                    "processors",
                    "tokenizer",
                    "translation_model",
                ]:
                    data[s] = None
            else:
                data[section] = None

        with open(project_dir.joinpath("config.yml"), "w") as file_write:
            yaml.dump(data, file_write, sort_keys=False)

    @staticmethod
    def show(project_dir: pathlib.Path):
        with open(project_dir.joinpath("config.yml"), "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        print("Customer -> ", data["customer"])

        print("Source Language -> ", data["src_lang"])

        print("Target Language -> ", data["tgt_lang"])

        print("Flavor -> ", data["flavor"])

        print("Version -> ", data["version"])

        if data["processors"]:
            print("Cleanning processors:")
            for processor, args in data["processors"].items():
                if args != []:
                    print(f" -  {processor}:")
                    for arg in args:
                        print(f"        {arg}")
                else:
                    print(f" -  {processor}")
        else:
            print("Cleanning processors not configured")

        if data["tokenizer"]:
            print("Tokenizer configuration:")
            print(f" -  Source language tokenizer: {data['tokenizer']['src']}")
            print(f" -  Target language tokenizer: {data['tokenizer']['tgt']}")
        else:
            print("Tokenizer not configured")

        if data["truecaser"]:
            print("Truecaser configuration:")
            print(
                f" -  Source language truecaser is {data['truecaser']['src']}"
            )
            print(
                f" -  Target language truecaser is {data['truecaser']['tgt']}"
            )
        else:
            print("Truecaser not configured")

        if data["bpe"]:
            print("BPE configuration:")
            if data["bpe"]["joint"]:
                print(
                    f" -  Joint training, with {data['bpe']['num_iterations']} number "
                    f"of iterations and threshold {data['bpe']['threshold']}"
                )
            else:
                print(
                    f" -  Disjoint training, with {data['bpe']['num_iterations']} "
                    f"number of iterations and threshold {data['bpe']['threshold']}"
                )
        else:
            print("BPE not configured")

        if data["translation_model"]:
            print("Translation model configuration:")
            print(f" -  {data['translation_model']['name']} with arguments:")
            print(f"    {data['translation_model']['args']}")
        else:
            print("Translation model not configured")
