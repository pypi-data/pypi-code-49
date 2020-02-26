import argparse
import warnings
from pathlib import Path
from typing import List
from shutil import make_archive

from ehealthkd.utils import Collection


class Algorithm:
    def run(
        self, collection: Collection, *args, taskA: bool, taskB: bool, **kargs
    ) -> Collection:
        raise NotImplementedError()


class Run:
    def __init__(
        self,
        user: str,
        run_name: str,
        algorithm: Algorithm,
        *,
        gold: Path,
        mode: str,
        scenarios: List[str]
    ):
        self.user = user
        self.run_name = run_name
        self.algorithm = algorithm

        self.gold = gold
        self.mode = mode
        self.scenarios = scenarios

    def __call__(self, *args, **kargs):
        for scenario in self.scenarios:
            collection = self._load_collection(scenario)
            output = self.algorithm.run(
                collection,
                taskA=(not scenario.endswith("-taskB")),
                taskB=(not scenario.endswith("-taskA")),
                *args,
                **kargs
            )
            output.dump(
                Path(
                    "../evaluation/submissions/{0}/{1}/{2}/{3}/scenario.txt".format(
                        self.user, self.run_name, self.mode, scenario
                    )
                )
            )

    def _load_collection(self, scenario):
        gold = self.gold.format(scenario)

        return Collection().load(
            Path(gold),
            legacy=False,
            keyphrases=scenario.endswith("-taskB"),
            relations=False,
            attributes=False,
        )

    @staticmethod
    def on(user: str, run_name: str, algorithm, config):
        return Run(user, run_name, algorithm, **config)

    @staticmethod
    def exec(run: "Run", *args, **kargs):
        run(*args, **kargs)

    @staticmethod
    def zip(user: str):
        make_archive(
            "../evaluation/submissions/{0}".format(user),
            "zip",
            "../evaluation/submissions/{0}".format(user),
        )

    @staticmethod
    def submit(usr: str, configurations, run_name, algorithm):
        for config in configurations:
            Run.exec(Run.on(usr, run_name, algorithm, config=config))
        # Run.zip('baseline')

    @staticmethod
    def testing():
        yield dict(
            gold="../corpus/testing/{0}/scenario.txt",
            mode="test",
            scenarios=["scenario1-main", "scenario2-taskA", "scenario3-taskB",],
        )

    @staticmethod
    def development():
        yield dict(
            gold="../corpus/development/main/scenario.txt",
            mode="dev",
            scenarios=["scenario1-main", "scenario2-taskA", "scenario3-taskB"],
        )

    @staticmethod
    def training():
        yield dict(
            gold="../corpus/training/scenario.txt",
            mode="train",
            scenarios=["scenario1-main", "scenario2-taskA", "scenario3-taskB"],
        )


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true")
    parser.add_argument("--dev", action="store_true")
    parser.add_argument("--test", action="store_true")
    parser.add_argument(
        "--custom",
        action="append",
        nargs=3,
        metavar=("GOLD", "MODE", "SCENARIOS"),
        help="""
        GOLD: path to gold file (use `{0}` for scenario template).
        MODE: name of the directory inside the user submit folder.
        SCENARIOS: name (or ',' separated list of names) for the run scenario(s).
        """,
    )
    args = parser.parse_args()

    tasks = []

    if args.train:
        tasks.extend(Run.training())

    if args.dev:
        tasks.extend(Run.development())

    if args.test:
        tasks.extend(Run.testing())

    if args.custom is not None:
        tasks.extend(
            dict(gold=gold, mode=mode, scenarios=scenarios.split(","))
            for gold, mode, scenarios in args.custom
        )

    return tasks
