import subprocess
import os
import click
from pathos.multiprocessing import Pool
from pangeamt_nlp.tokenizer.tokenizer_factory import TokenizerFactory
from pangeamt_tea.project.workflow.stage.base_stage import BaseStage
from pangeamt_nlp.multilingual_resource.tmx.tmx_reader_bilingual import (
    TmxReaderBilingualText,
)
from pangeamt_nlp.multilingual_resource.af.af_reader import AfReader
from pangeamt_nlp.multilingual_resource.bilingual.bilingual_reader import (
    BilingualReader,
)
from pangeamt_nlp.multilingual_resource.dataset.dataset_reader import (
    DatasetReader,
)
from pangeamt_nlp.multilingual_resource.dataset.dataset import Dataset
from pangeamt_nlp.truecaser.truecaser import Truecaser
from pangeamt_nlp.bpe.bpe import BPE
from pangeamt_nlp.data_batcher.batcher import batch


class PrepareStage(BaseStage):
    NAME = "prepare"
    NUM_LINES = 0
    CHUNKSIZE = 500

    def __init__(self, workflow):
        super().__init__(workflow, self.NAME)

    async def run(self, max_workers):
        project = self.workflow.project
        project_dir = project.config.project_dir

        # Make preparation Directory
        workflow_dir = self.workflow.get_dir(project_dir)
        self.stage_dir = os.path.join(workflow_dir, "02_prepared")

        if os.path.isdir(self.stage_dir):
            raise WorkflowAlreadyExists(project_dir)

        os.mkdir(self.stage_dir)

        await self.shuffle()
        await self.tokenize(max_workers)
        await self.truecase(max_workers)
        await self.bpe(max_workers)
        await self.prep_batch()

        # Create the file handlers for every dataset
        def get_dir(project_dir):
            return os.path.join(project_dir, Workflow.DIR)

        return {}

    # Read the clean data and join both langs in a file to shuffle it without losing
    # the alignment
    async def shuffle(self):
        project = self.workflow.project
        project_dir = project.config.project_dir

        workflow_dir = self.workflow.get_dir(project_dir)
        cleaned_dir = os.path.join(workflow_dir, "01_cleaned")

        dir = os.path.join(self.stage_dir, "01_raw")
        os.mkdir(dir)

        all_lines_path = os.path.join(dir, "all_lines.txt")
        all_lines_shuf = os.path.join(dir, "all_lines_shuf.txt")
        all_lines = open(all_lines_path, "w+")

        # Reads the cleaned files and joins them in a file
        with open(os.path.join(cleaned_dir, "data_src.txt"), "r") as src_file:
            with open(
                os.path.join(cleaned_dir, "data_tgt.txt"), "r"
            ) as tgt_file:
                for src_line, tgt_line in zip(src_file, tgt_file):
                    # Writes src_line###SEPARATOR###tgt_line
                    all_lines.write(
                        f"{src_line[:-1]}###SEPARATOR###{tgt_line}"
                    )

        all_lines.close()

        # Shuffle the data
        print("Shufling and splitting data...")
        subprocess.run(
            f'cat {all_lines_path} | sed -e "s/\r//g" | sed "s/\t//g" '
            f"| sort | uniq | shuf  > {all_lines_shuf}",
            shell=True,
        )

        train_src = open(
            os.path.join(dir, "train_src.txt"), "w+", encoding="utf-8"
        )
        train_tgt = open(
            os.path.join(dir, "train_tgt.txt"), "w+", encoding="utf-8"
        )
        test_src = open(
            os.path.join(dir, "test_src.txt"), "w+", encoding="utf-8"
        )
        test_tgt = open(
            os.path.join(dir, "test_tgt.txt"), "w+", encoding="utf-8"
        )
        dev_src = open(
            os.path.join(dir, "dev_src.txt"), "w+", encoding="utf-8"
        )
        dev_tgt = open(
            os.path.join(dir, "dev_tgt.txt"), "w+", encoding="utf-8"
        )

        # Open the shuffled file
        with open(all_lines_shuf, "r") as all_lines:
            for i, line in enumerate(all_lines):
                line = line.split("###SEPARATOR###")
                src = line[0]
                tgt = line[1]

                # Take first 2000 lines for dev
                if i < 2000:
                    # Only src need to be appended a new line
                    dev_src.write(src + "\n")
                    dev_tgt.write(tgt)
                # Take second 2000 lines for test
                elif i < 4000:
                    test_src.write(src + "\n")
                    test_tgt.write(tgt)
                # Take the rest of the lines for train
                else:
                    train_src.write(src + "\n")
                    train_tgt.write(tgt)

        self.NUM_LINES = i

        # Close all the file handlers
        train_src.close()
        train_tgt.close()
        test_src.close()
        test_tgt.close()
        dev_src.close()
        dev_tgt.close()

        # Remove the files used to shuffle the data
        subprocess.run(
            f"rm {all_lines_path} && rm {all_lines_shuf}", shell=True
        )
        print("Finished shufling and splitting data")

    # Tokenize corpus
    async def tokenize(self, max_workers):
        dir = os.path.join(self.stage_dir, "02_tokenized")
        os.mkdir(dir)

        # Directory of the previous stage
        prev_dir = os.path.join(self.stage_dir, "01_raw")

        project = self.workflow.project

        # Take the name of the tokenizer to use from the config file
        src_tok_name = project.config.tokenizer["src"]
        tgt_tok_name = project.config.tokenizer["tgt"]

        # Initialize the tokenizer for each language and pair it with the files with
        # a tuple
        files = (
            (
                [
                    ("train_src.txt", self.NUM_LINES),
                    ("test_src.txt", 2000),
                    ("dev_src.txt", 2000),
                ],
                TokenizerFactory.new(project.config.src_lang, src_tok_name),
            ),
            (
                [
                    ("train_tgt.txt", self.NUM_LINES),
                    ("test_tgt.txt", 2000),
                    ("dev_tgt.txt", 2000),
                ],
                TokenizerFactory.new(project.config.tgt_lang, tgt_tok_name),
            ),
        )

        # Tokenize each line
        for pair in files:
            tokenizer = pair[1]
            for file, size in pair[0]:
                in_path = os.path.join(prev_dir, file)
                out_path = os.path.join(dir, file)
                with open(in_path, "r", encoding="utf-8") as in_file:
                    with open(out_path, "w+", encoding="utf-8") as out_file:
                        with Pool(max_workers) as pool:
                            with click.progressbar(
                                pool.imap(
                                    lambda x: tokenizer.tokenize(x),
                                    in_file,
                                    chunksize=self.CHUNKSIZE,
                                ),
                                length=size,
                                label=f"Tokenizing: {file}",
                            ) as bar:
                                for tokenized_line in bar:
                                    out_file.write(tokenized_line + "\n")

    # Apply the truecase to the data
    async def truecase(self, max_workers):
        dir = os.path.join(self.stage_dir, "03_truecased")
        os.mkdir(dir)

        prev_dir = os.path.join(self.stage_dir, "02_tokenized")

        print("Training truecase models if enabled...")

        (src_model_path, tgt_model_path) = self.create_truecase_model(prev_dir)

        print("Finished training")

        # Initialize the truecaser for the different languages if the truecaser is
        # enabled, if not, let it None
        files = (
            (
                [
                    ("train_src.txt", self.NUM_LINES),
                    ("test_src.txt", 2000),
                    ("dev_src.txt", 2000),
                ],
                Truecaser(src_model_path)
                if (self.workflow.project.config.truecaser["src"] == "enabled")
                else None,
            ),
            (
                [
                    ("train_tgt.txt", self.NUM_LINES),
                    ("test_tgt.txt", 2000),
                    ("dev_tgt.txt", 2000),
                ],
                Truecaser(tgt_model_path)
                if (self.workflow.project.config.truecaser["tgt"] == "enabled")
                else None,
            ),
        )

        for pair in files:
            truecaser = pair[1]
            if truecaser:
                for file, size in pair[0]:
                    in_path = os.path.join(prev_dir, file)
                    out_path = os.path.join(dir, file)
                    with open(in_path, "r", encoding="utf-8") as in_file:
                        with open(
                            out_path, "w+", encoding="utf-8"
                        ) as out_file:
                            with Pool(max_workers) as pool:
                                with click.progressbar(
                                    pool.imap(
                                        lambda x: truecaser.truecase(x),
                                        in_file,
                                        chunksize=self.CHUNKSIZE,
                                    ),
                                    length=size,
                                    label=f"Truecasing: {file}",
                                ) as bar:
                                    for truecased_line in bar:
                                        out_file.write(truecased_line + "\n")
                                pool.close()

    # Create truecase model
    def create_truecase_model(self, prev_dir: str):
        dir = os.path.join(self.stage_dir, "truecase_model")
        os.mkdir(dir)
        src_model_path = os.path.join(dir, "src_model.txt")
        tgt_model_path = os.path.join(dir, "tgt_model.txt")

        def make_path(file: str):
            return os.path.join(prev_dir, file)

        if self.workflow.project.config.truecaser["src"] == "enabled":
            Truecaser().train_from_file(
                make_path("train_src.txt"), save_to=src_model_path, processes=4
            )

        if self.workflow.project.config.truecaser["tgt"] == "enabled":
            Truecaser().train_from_file(
                make_path("train_tgt.txt"), save_to=tgt_model_path, processes=4
            )

        return (src_model_path, tgt_model_path)

    # Apply bpe to data
    async def bpe(self, max_workers):
        dir = os.path.join(self.stage_dir, "04_bpe")
        os.mkdir(dir)

        # Directory of the previous stage
        prev_dir = os.path.join(self.stage_dir, "03_truecased")
        # BPE joint and threshold parameter from config
        joint = self.workflow.project.config.bpe["joint"]
        threshold = self.workflow.project.config.bpe["threshold"]

        print("Training bpe models if enabled...")

        model_dir = self.create_bpe_model(prev_dir, joint)

        print("Finished training bpe model")

        # If joint, train the bpe with all the corpus, else, train with the corpus split
        # by language
        if joint:
            src_bpe = BPE(
                os.path.join(model_dir, "codes32k.txt"),
                os.path.join(model_dir, "src_vocab.txt"),
                threshold,
            )
            tgt_bpe = BPE(
                os.path.join(model_dir, "codes32k.txt"),
                os.path.join(model_dir, "tgt_vocab.txt"),
                threshold,
            )
        else:
            src_bpe = BPE(
                os.path.join(model_dir, "src_codes.txt"),
                bpe_threshold=threshold,
            )
            tgt_bpe = BPE(
                os.path.join(model_dir, "tgt_codes.txt"),
                bpe_threshold=threshold,
            )

        # Pair src and tgt files with the corresponding BPE objects
        files = (
            (
                [
                    ("train_src.txt", self.NUM_LINES),
                    ("test_src.txt", 2000),
                    ("dev_src.txt", 2000),
                ],
                src_bpe,
            ),
            (
                [
                    ("train_tgt.txt", self.NUM_LINES),
                    ("test_tgt.txt", 2000),
                    ("dev_tgt.txt", 2000),
                ],
                tgt_bpe,
            ),
        )

        for pair in files:
            bpe = pair[1]
            if bpe:
                for file, size in pair[0]:
                    in_path = os.path.join(prev_dir, file)
                    out_path = os.path.join(dir, file)
                    with open(in_path, "r", encoding="utf-8") as in_file:
                        with open(
                            out_path, "w+", encoding="utf-8"
                        ) as out_file:
                            with Pool(max_workers) as pool:
                                with click.progressbar(
                                    pool.imap(
                                        lambda x: bpe.apply(x),
                                        in_file,
                                        chunksize=self.CHUNKSIZE,
                                    ),
                                    length=size,
                                    label=f"Applying bpe: {file}",
                                ) as bar:
                                    for bpe_line in bar:
                                        out_file.write(bpe_line)

    # Create BPE model
    def create_bpe_model(self, prev_dir, joint):
        dir = os.path.join(self.stage_dir, "bpe_model")
        os.mkdir(dir)

        iterations = self.workflow.project.config.bpe["num_iterations"]

        src_input_path = os.path.join(prev_dir, "train_src.txt")
        tgt_input_path = os.path.join(prev_dir, "train_tgt.txt")

        if joint:
            codes_path = os.path.join(dir, "codes32k.txt")
            src_vocab_path = os.path.join(dir, "src_vocab.txt")
            tgt_vocab_path = os.path.join(dir, "tgt_vocab.txt")
            BPE.learn_joint(
                src_input_path,
                tgt_input_path,
                codes_path,
                src_vocab_path,
                tgt_vocab_path,
                iterations,
            )
        else:
            src_model_path = os.path.join(dir, "src_codes.txt")
            tgt_model_path = os.path.join(dir, "tgt_codes.txt")
            BPE.learn(src_input_path, src_model_path, iterations)
            BPE.learn(tgt_input_path, tgt_model_path, iterations)

        return dir

    # Split the corpus in shards
    async def prep_batch(self):
        dir = os.path.join(self.stage_dir, "05_batched")
        os.mkdir(dir)
        prev_dir = os.path.join(self.stage_dir, "04_bpe")

        args = [
            "-train_src",
            os.path.join(prev_dir, "train_src.txt"),
            "-train_tgt",
            os.path.join(prev_dir, "train_tgt.txt"),
            "-valid_src",
            os.path.join(prev_dir, "dev_src.txt"),
            "-valid_tgt",
            os.path.join(prev_dir, "dev_tgt.txt"),
            "-shard_size",
            "100000",
            "-src_seq_length",
            "100",
            "-tgt_seq_length",
            "100",
            "-save_data",
            os.path.join(dir, "data"),
            "-log_file",
            os.path.join(dir, "prep.log"),
        ]

        batch(self.stage_dir, *args)
