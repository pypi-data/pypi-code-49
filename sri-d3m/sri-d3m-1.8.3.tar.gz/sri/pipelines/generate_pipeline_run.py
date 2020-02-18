import logging
import sys
import os
import subprocess
import json

# init logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(name)s -- %(message)s')
_logger = logging.getLogger(__name__)

'''
This script allows us to quickly run a fit-score on a pipeline.
This script relies on 3 environment variables for each mode:

    # Location of the seed datasets
    D3M_Dataset_Home="/datasets/seed_datasets_current"
    # Where the output data should be written
    D3M_Output_Home="./pipelines"
    # What docker image to run
    D3M_Docker_Image="registry.datadrivendiscovery.org/j18_ta2eval/sri_tpot:20191110-devel"

TODO: This script also requires n command line parameters:
'''

class GeneratePipelineRun(object):

    def __init__(self, **args):
        self._add_attrs(args, 'pipeline_name', 'problem_name', 'dataset_home', 'docker_image', 'output_home', 'pipeline_run_outdir')

    def _add_attrs(self, args, *attrs):
        for attr in attrs:
            if attr in args:
                setattr(self, attr, args[attr])

    def main(self):
        _logger.info("Generate Pipeline Run")

        # Generate the run command
        command = self.generate_command()
        if command is None:
            raise Exception("Unable to run pipeline specified")

        _logger.info("Run Command Line:")
        _logger.info(command)

        # Launch the command
        ret_stdout = subprocess.check_output(command, shell=True)
        _logger.info("Run Command completed")


    '''
    This method builds the a command that calls fit-score on a pipeline using the reference runtime.

    For fit-score:
      docker run 
        -i --rm  
        -v /datasets/test/185_baseball:/input/ 
        -v /Users/daraghhartnett/Projects/D3M/evals/012119/tpot-ta2/data/output/185_baseball:/output/ 
        registry.datadrivendiscovery.org/j18_ta2eval/sri_tpot:2019.2.27-devel2 
        python3 -m d3m runtime fit-score 
          -p /output/pipelines_ranked/AWOGCBE3LU.json 
          -r /input/185_baseball_problem/problemDoc.json 
          -i /input/TRAIN/dataset_TRAIN/datasetDoc.json 
          -t /input/TEST/dataset_TEST/datasetDoc.json 
          -a /input/TEST/dataset_TEST/datasetDoc.json
    '''

    def generate_command(self):
        print("Datasethome: " + self.dataset_home)
        print("Problem Name: " + self.problem_name)

        pipeline = "%s/%s.json" % ("/output", self.pipeline_name)

        problem_doc = "/input/%s/%s_problem/problemDoc.json" % (self.problem_name, self.problem_name)
        train_dataset_doc = "%s/%s/TRAIN/dataset_TRAIN/datasetDoc.json" % ("/input", self.problem_name)
        test_dataset_doc = "%s/%s/TEST/dataset_TEST/datasetDoc.json" % ("/input", self.problem_name)
        path_to_score_file = "/SCORE/dataset_TEST/datasetDoc.json"
        scoring_dataset_doc = "%s/%s/%s" % ("/input", self.problem_name, path_to_score_file)

        problem_data_path = "/input/" + self.problem_name
        if not os.path.exists("%s%s" % (problem_data_path, path_to_score_file)):
            scoring_dataset_doc = "%s/%s/SCORE/dataset_SCORE/datasetDoc.json" % ("/input", self.problem_name)

        pipeline_run = "%s/%s%s" % ("/pipeline_run_output", self.pipeline_name, "_pipeline_run.yml")

        # Build the components of the command line
        # output_data_path = self.output_home + "/" + self.problem_name

        input_mount = " -v " + self.dataset_home + ":/input/"
        output_mount = " -v " + self.output_home + ":/output/"
        pipeline_run_output_mount = " -v " + self.pipeline_run_outdir + ":/pipeline_run_output/"

        command = "python3 -m d3m runtime -v /volumes fit-score -p %s -r %s -i %s -t %s -a %s -O %s -o -" % \
                  (pipeline, problem_doc, train_dataset_doc, test_dataset_doc, scoring_dataset_doc,
                   pipeline_run)

        # self.pipeline_run_file = "%s/%s%s" % (self.output_home, self.pipeline_name, "_pipeline_run.yml")

        # Assemble the full command
        testCmd = "docker run -i --rm " + \
                  input_mount + \
                  output_mount + \
                  pipeline_run_output_mount + \
                  " " + self.docker_image + \
                  " " + command

        return testCmd


'''
Entry point - required to make python happy
'''
if __name__ == "__main__":
    # Grab the command line parameters
    problemName = sys.argv[1]
    rank = sys.argv[2]
    GeneratePipelineRun(problemName=problemName, rank=rank).main()
