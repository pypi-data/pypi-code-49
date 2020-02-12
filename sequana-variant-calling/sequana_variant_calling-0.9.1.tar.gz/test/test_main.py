import easydev
import os
import tempfile
import subprocess
import sys


sequana_path = easydev.get_package_location('sequana_variant_calling')
sharedir = os.sep.join([sequana_path , "sequana_pipelines/variant_calling", 'data'])
reference = os.sep.join([sequana_path , "sequana_pipelines/variant_calling", 'data']) + os.sep + "JB409847.fasta"
annotation = os.sep.join([sequana_path , "sequana_pipelines/variant_calling", 'data']) + os.sep + "JB409847.gbk"


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = "sequana_pipelines_variant_calling --input-directory {} "
    cmd += "--working-directory {} --run-mode local --force --annotation {} "
    cmd += " --reference {}"
    cmd = cmd.format(sharedir, directory.name, annotation, reference)
    subprocess.call(cmd.split())



#def test_standalone_script():
#    directory = tempfile.TemporaryDirectory()
#    import sequana_pipelines.variant_calling.main as m
#    sys.argv = ["test", "--fastq-directory", sharedir, "--output-directory",
#        directory.name, "--run-mode", "local", "--force"]
#    m.main()


# For travis, you may want to add this with snakemake:
#if "TRAVIS_PYTHON_VERSION" in os.environ:
#    cmd += ["--snakemake-jobs", "1"]

def test_check_output():

    with tempfile.TemporaryDirectory() as wk:

        cmd = "sequana_pipelines_variant_calling --input-directory {} "
        cmd += "--working-directory {} --run-mode local --force --annotation {} "
        cmd += " --reference {}"
        cmd = cmd.format(sharedir, wk, annotation, reference)
        # create the wokring directory and script
        subprocess.call(cmd.split())

        subprocess.call("sh variant_calling.sh".split(), cwd=wk)


        from sequana.freebayes_vcf_filter import VCF_freebayes, Variant
        vcf = VCF_freebayes(wk + "/report_vc_data/outputs/data.raw.vcf")
        vcf.rewind()
        vv = [Variant(v)._resume for v in vcf]
        # this may change depending on the freebayes version...
        assert len(vv) in (63,)
        vv = vv[0].copy()
        del vv['freebayes_score']
        assert vv == {'alternative': 'T',
             'chr': 'JB409847',
             'depth': 23,
             #'freebayes_score': 2.78452e-14,
             'frequency': '0.26',
             'position': '2221',
             'reference': 'C',
             'strand_balance': '0.33'}


test_check_output()
