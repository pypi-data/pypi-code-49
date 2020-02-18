# Output pipelines in JSON.

import argparse
import json
import os
import sys
import subprocess

import sri.pipelines.all
import sri.pipelines.datasets
from sri.pipelines.base import ONLY_CHALLENGE_PROBLEMS
from d3m.runtime import Runtime
from sri.pipelines.generate_pipeline_run import GeneratePipelineRun
from sri.common import config
import logging

# init logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(name)s -- %(message)s')
_logger = logging.getLogger(__name__)

def load_args():
    parser = argparse.ArgumentParser(description = "Output a primitive's pipelines in the standard format.")

    parser.add_argument(
        'primitive', action = 'store', metavar = 'PRIMITIVE',
        help = "the D3M entrypoint of the primitive whose pipelines will be output"
    )

    parser.add_argument(
        'outdir', action = 'store', metavar = 'OUTPUT_DIR',
        help = "where to write the file"
    )

    parser.add_argument(
        'pipelinerunoutdir', action = 'store', metavar = 'PIPELINE_RUN_OUTPUT_DIR',
        help = "where to write the pipeline run file"
    )

    parser.add_argument(
        '-o', '--one', action = "store_true",
        help = "only generate at most one pipeline"
    )

    parser.add_argument(
        '-p', '--prediction', action = "store_true",
        help = "only generate prediction pipelines"
    )

    arguments = parser.parse_args()

    return arguments.primitive, os.path.abspath(arguments.outdir), os.path.abspath(arguments.pipelinerunoutdir), arguments.one, arguments.prediction

def main():
    max_pipelines_per_primitive = 10
    primitive, out_dir, pipelinerunoutdir, only_one, only_prediction = load_args()

    if (primitive not in sri.pipelines.all.get_primitives()):
        print("Could not locate pipelines for primitive: %s." % (primitive), file = sys.stderr)
        # print(sri.pipelines.all.get_primitives())
        return

    os.makedirs(out_dir, exist_ok = True)
    os.makedirs(pipelinerunoutdir, exist_ok = True)

    for pipeline_class in sri.pipelines.all.get_pipelines(primitive):
        # print(pipeline_class, "Only challenge problems:", ONLY_CHALLENGE_PROBLEMS)
        if not hasattr(pipeline_class, 'CHALLENGE_PROBLEMS') or ONLY_CHALLENGE_PROBLEMS is None:
            datasets = set(pipeline_class().get_datasets()) - sri.pipelines.datasets.SLOW_DATASETS
        elif ONLY_CHALLENGE_PROBLEMS:
            datasets = pipeline_class.CHALLENGE_PROBLEMS
        else:
            datasets = ((set(pipeline_class().get_datasets()) - sri.pipelines.datasets.SLOW_DATASETS)
                        | set(pipeline_class.CHALLENGE_PROBLEMS))

        # print("Using datasets:", datasets)

        count = 0
        for dataset in datasets:

            # Masses of pipelines is causing CI to take forever, cap the max number per primitive.
            if count >= max_pipelines_per_primitive:
                break

            pipeline = pipeline_class()

            if (only_prediction and not pipeline.is_prediction_pipeline()):
                continue

            print("\n Working on Problem '%s' and Dataset '%s'" % (pipeline_class, dataset))
            try:
                meta_info = {
                    'problem': sri.pipelines.datasets.get_problem_id(dataset),
                    'full_inputs': [ sri.pipelines.datasets.get_full_dataset_id(dataset) ],
                    'train_inputs': [ sri.pipelines.datasets.get_train_dataset_id(dataset) ],
                    'test_inputs': [ sri.pipelines.datasets.get_test_dataset_id(dataset) ],
                    'score_inputs': [ sri.pipelines.datasets.get_score_dataset_id(dataset) ],
                }

                out_path = os.path.join(out_dir, "%s.json" % (pipeline.get_id()))
                with open(out_path, 'w') as file:
                    file.write(pipeline.get_json())

                # Run the pipelines to generate the pipeline run files
                generate_pipeline_run = GeneratePipelineRun(pipeline_name=pipeline.get_id(),
                                                            problem_name=sri.pipelines.datasets.get_problem_id(dataset).replace("_problem", ""),
                                                            dataset_home=config.DATASET_HOME,
                                                            docker_image=config.DOCKER_IMAGE,
                                                            output_home=out_dir,
                                                            pipeline_run_outdir=pipelinerunoutdir)
                generate_pipeline_run.main()
            except LookupError:
                print("Could not find dataset '%s'" % dataset, file=sys.stderr)
                continue
            except Exception as e:
                print("Some pipelines are not runnable - continue with the next one")
                continue
            finally:
                pipeline_run_file = "%s/%s_pipeline_run.yml" % (pipelinerunoutdir, pipeline.get_id())

                command = "gzip %s" % pipeline_run_file
                _logger.info("GZip Command Line:")
                _logger.info(command)

                # Launch the command
                ret_stdout = subprocess.check_output(command, shell=True)
                _logger.info("GZip Command completed")


            if (only_one):
                break

if __name__ == '__main__':
    main()
