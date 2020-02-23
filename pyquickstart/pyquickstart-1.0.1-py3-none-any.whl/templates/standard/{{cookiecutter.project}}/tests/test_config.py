from {{cookiecutter.project}}.config import PACKAGE_ROOT


def test_package_root_is_valid():
    assert PACKAGE_ROOT.is_dir()
    assert PACKAGE_ROOT.stem == '{{cookiecutter.project}}'
