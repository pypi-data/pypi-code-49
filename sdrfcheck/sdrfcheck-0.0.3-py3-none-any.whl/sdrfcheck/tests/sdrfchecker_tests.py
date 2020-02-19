from click.testing import CliRunner
from sdrfcheck.sdrfchecker import cli


def validate_srdf():
    """
    Test the default behaviour of the vcf-to-proteindb tool
    :return:
    """
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['validate-sdrf', '--sdrf_file', 'testdata/sdrf.txt'])
    print(result.exception)
    assert result.exit_code == 0


if __name__ == '__main__':
    validate_srdf()
