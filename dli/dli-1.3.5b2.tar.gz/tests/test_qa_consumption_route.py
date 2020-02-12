import pytest
import os
import boto3
import jwt as pyjwt

from dli.client.builders import DatasetBuilder
from dli.client.dli_client import DliClient, Session
from dli.client.exceptions import CatalogueEntityNotFoundException


def pytest_generate_tests(metafunc):
    metafunc.parametrize('client', ('QA',), indirect=['client'],
                         scope='function')
    metafunc.parametrize('jwt', ('QA',), indirect=['jwt'], scope='function')


@pytest.fixture
def jwt(request):
    # The env variable QA_OIDC_AUD can be found in gitlab under
    # the settings:CI/CD:Variables section and set locally.
    aud = os.environ[f'{request.param}_OIDC_AUD']
    return {
        "datalake": {
            "accounts": {
                "e452ffba-0f96-4ec5-a20a-e550386dc11e": "rw",
                "datalake-test1": "rw",
                "datalake-test2": "rw",
                "datalake-ops": "rw",
            },
            "groups": [],
            "organisation_id": "9516c0ba-ba7e-11e9-8b34-000c6c0a981f"
        },
        "sub": "api:rollo-qa@ihsmarkit.com",
        "exp": 9564743138,
        "aud": aud
    }


class TestDliClient(DliClient):
    def __init__(self, api_key=None, api_root=None, auth_key=None, host=None,
                 debug=False):
        self.auth_key = auth_key
        super().__init__(api_key, api_root, host=host, debug=debug)

    def _new_session(self):
        return Session(
            self.api_key,
            self._environment,
            self.host,
            self.auth_key,
        )


@pytest.fixture
def client(monkeypatch, jwt, request):
    # This is the S3 address used for the QA environment.
    monkeypatch.setenv(
        'S3_URL',
        'https://test-datalake-read-write-bucket-1.s3.us-east-2.amazonaws.com'
    )
    api_root = os.environ[f'{request.param}_API_URL']
    secret = os.environ[f'{request.param}_OIDC_SECRET']
    auth_key = pyjwt.encode(jwt, secret).decode('utf8')
    api_key = 'itest'
    client = TestDliClient(
        api_key=api_key,
        api_root=api_root,
        auth_key=auth_key
    )
    yield client


@pytest.fixture
def aws_roles(client):
    aws_account = {
        "awsAccountId": '867407613858',
        "awsAccountName": "dl_prod_aws_account",
        "awsRoleArn": "arn:aws:iam::867407613858:role/trust-entity-dev-test",
        "awsRegion": "eu-west-1",
        "accountIds": ['datalake-test1', 'datalake-test2', 'datalake-mgmt']
    }

    client.session.post(
        '__api/me/aws-accounts', json=aws_account
    )


class aws_envs:
    QA = ''


def random_name():
    from secrets import token_urlsafe
    return '-qa-test-cases-{}'.format(token_urlsafe(3))


@pytest.fixture
def boto_sessions():
    qa = boto3.Session(profile_name='qa')
    return {
        aws_envs.QA: qa,
    }


@pytest.fixture
def bucket(boto_sessions):
    bucket = 'test-datalake-read-write-bucket-1'
    session = boto_sessions[aws_envs.QA]
    s3_resource = session.resource('s3')
    bucket_resource = s3_resource.Bucket(bucket)
    yield bucket_resource


@pytest.fixture
def package(client):
    package = client.register_package(
        name=random_name(),
        description="my package description",
        topic="Automotive",
        access="Restricted",
        internal_data="Yes",
        data_sensitivity="Public",
        terms_and_conditions="Terms",
        publisher="my publisher",
        # OMG OMG OMG access_manager_id mustn't be in the JWT
        access_manager_id='datalake-ops',
        tech_data_ops_id='datalake-test2',
        manager_id='datalake-test2'
    )
    yield package
    client.delete_package(package.package_id)


@pytest.fixture
def client_post(client):
    yield client.session.post(
        '{}me/aws-accounts'.format(os.environ.get('QA_API_URL')),
        json={
            "awsAccountId": "867407613858",
            "awsAccountName": "dl_prod_aws_account",
            "awsRoleArn": "arn:aws:iam::867407613858:role/trust-entity-dev-test",
            "awsRegion": "eu-west-1",
            "awsAccessKeyId": None,
            "awsSecretAccessKey": None,
            "accountIds": [
                "datalake-test1",
                "datalake-test2",
                "e452ffba-0f96-4ec5-a20a-e550386dc11e"
            ]
        }
    )


@pytest.fixture
def csv_dataset_builder():
    dataset_builder = DatasetBuilder(
        package_id='6fce23d0-98ea-11e9-a6cc-bea41eadbb57',
        name='dataset-files-test-' + random_name(),
        description="My dataset description",
        content_type="Pricing",
        data_format='CSV',
        publishing_frequency="Weekly",
        taxonomy=[]
    )

    dataset_builder = dataset_builder.with_external_s3_storage(
        bucket_name='test-datalake-read-write-bucket-1',
        aws_account_id='867407613858',
        prefix='abc',
    )
    yield dataset_builder


@pytest.fixture
def empty_dataset(client, client_post, csv_dataset_builder):
    dataset = client.register_dataset(csv_dataset_builder)
    yield dataset


@pytest.fixture
def csv_dataset(client, client_post, csv_dataset_builder):
    dataset = client.register_dataset(csv_dataset_builder)
    client.register_s3_datafile(
        dataset.dataset_id,
        "test_get_s3_datafile",
        ['tests/abc/AAPL.csv'],
        "abc",
        data_as_of='2000-01-01'
    )
    yield dataset


@pytest.mark.integration
def test_files_method_in_dataset_with_qa_env(csv_dataset):
    for x in csv_dataset.instances.all():
        print(x)
    c = csv_dataset.instances.latest()
    c_files = c.files()
    assert c_files is not None


@pytest.mark.integration
def test_files_method_in_empty_dataset_with_qa_env(empty_dataset):
    with pytest.raises(CatalogueEntityNotFoundException):
        empty_dataset.instances.latest().files()
