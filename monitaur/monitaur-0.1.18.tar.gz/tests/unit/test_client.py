import os

import boto3
import pytest
import requests

from monitaur import Monitaur
from monitaur.exceptions import ClientAuthError, ClientValidationError
from monitaur.virgil.alibi.tabular import AnchorTabular

model_data = {
    "name": "Diabetes Classifier",
    "model_type": "random_forest",
    "model_class": "tabular",
    "library": "scikit_learn",
    "trained_model_hash": "7fa8962a",
    "production_file_hash": "ec9b7a68",
    "feature_number": 8,
    "owner": "Anthony Habayeb",
    "developer": "Andrew Clark",
    "influences": True,
}

record_training_data = {
    "credentials": {
        "aws_access_key": "some access key",
        "aws_secret_key": "some secret key",
        "aws_region": "us-east-1",
        "aws_bucket_name": "some bucket name",
    },
    "model_set_id": 1,
    "feature_names": [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeF",
        "Age",
    ],
}

transaction_data = {
    "credentials": {
        "aws_access_key": "some access key",
        "aws_secret_key": "some secret key",
        "aws_region": "us-east-1",
        "aws_bucket_name": "some bucket name",
    },
    "model_set_id": 1,
    "trained_model_hash": "7fa8962a",
    "production_file_hash": "ec9b7a68",
    "prediction": "",
    "features": {},
}


def test_initialize_session():
    monitaur = Monitaur(auth_key="secret")

    assert isinstance(monitaur._session, requests.Session)
    assert monitaur._session.headers["User-Agent"] == "monitaur-client-library"
    assert monitaur._session.headers["Authorization"] == "Token secret"


def test_add_model_returns_model_set_id(mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(response, "json", return_value={"model_set_id": 111})
    mocker.patch.object(monitaur._session, "post", return_value=response)

    model_set_id = monitaur.add_model(**model_data)

    assert model_set_id == 111


def test_add_model_raises_client_auth_error_given_unauthorized_response(mocker):
    monitaur = Monitaur(auth_key="invalid")
    response = requests.Response()
    response.status_code = 401
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "post", return_value=response)

    with pytest.raises(ClientAuthError):
        monitaur.add_model(**model_data)


def test_add_model_raises_client_validation_error_when_400_response_received(mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 400
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "post", return_value=response)

    with pytest.raises(ClientValidationError):
        monitaur.add_model(**model_data)


def test_record_transaction_returns_response_json_given_success_response(mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(
        response, "json", return_value={"version": 1, "influences": True}
    )
    mocker.patch.object(monitaur._session, "get", return_value=response)
    mock_explain_transaction = mocker.patch(
        "monitaur.client.explain_transaction",
        return_value=["Glucose <= 99.00", "BMI <= 27.35"],
    )
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(response, "json", return_value={"id": 1})
    mocker.patch.object(monitaur._session, "post", return_value=response)

    transaction_details = monitaur.record_transaction(**transaction_data)

    assert transaction_details["id"] is not None
    assert mock_explain_transaction.call_count == 1


def test_when_influences_false_record_transaction_skips_explain_transaction(mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(
        response, "json", return_value={"version": 1, "influences": False}
    )
    mocker.patch.object(monitaur._session, "get", return_value=response)
    mock_explain_transaction = mocker.patch("monitaur.client.explain_transaction")
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(response, "json", return_value={"id": 1})
    mocker.patch.object(monitaur._session, "post", return_value=response)

    transaction_details = monitaur.record_transaction(**transaction_data)

    assert transaction_details["id"] is not None
    assert mock_explain_transaction.call_count == 0


def test_record_transaction_raises_client_auth_error_given_unauthorized_response(
    mocker,
):
    monitaur = Monitaur(auth_key="invalid")
    response = requests.Response()
    response.status_code = 401
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "get", return_value=response)

    with pytest.raises(ClientAuthError):
        monitaur.record_transaction(**transaction_data)


def test_record_transaction_raises_client_validation_error_given_bad_request(mocker):
    monitaur = Monitaur(auth_key="secret")
    invalid_data = transaction_data.copy()
    invalid_data["features"] = "invalid features"
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(
        response, "json", return_value={"version": 1, "influences": True}
    )
    mocker.patch.object(monitaur._session, "get", return_value=response)
    mock_explain_transaction = mocker.patch(
        "monitaur.client.explain_transaction",
        return_value=["Glucose <= 99.00", "BMI <= 27.35"],
    )
    response = requests.Response()
    response = requests.Response()
    response.status_code = 400
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "post", return_value=response)

    with pytest.raises(ClientValidationError):
        monitaur.record_transaction(**invalid_data)

    assert mock_explain_transaction.call_count == 1

    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 400
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "get", return_value=response)

    with pytest.raises(ClientValidationError):
        monitaur.record_transaction(**invalid_data)


def test_record_training(trained_model, training_data, mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(response, "json", return_value={"version": 1})
    mocker.patch.object(monitaur._session, "get", return_value=response)
    mocker.patch.object(AnchorTabular, "__init__", return_value=None)
    mocker.patch.object(AnchorTabular, "fit")
    boto3_client_mock = mocker.patch.object(boto3, "client")
    upload_fileobj_mock = boto3_client_mock.return_value.upload_fileobj

    result = monitaur.record_training(
        trained_model=trained_model, training_data=training_data, **record_training_data
    )

    assert result is True
    assert upload_fileobj_mock.call_count == 2

    filename = f"{record_training_data['model_set_id']}.joblib"
    filename_anchors = f"{record_training_data['model_set_id']}.anchors"
    os.remove(filename)
    os.remove(filename_anchors)


def test_record_training_with_re_train_true(trained_model, training_data, mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 200
    mocker.patch.object(response, "json", return_value={"version": 1})
    mocker.patch.object(monitaur._session, "get", return_value=response)
    mocker.patch.object(AnchorTabular, "__init__", return_value=None)
    mocker.patch.object(AnchorTabular, "fit")
    boto3_client_mock = mocker.patch.object(boto3, "client")
    upload_fileobj_mock = boto3_client_mock.return_value.upload_fileobj
    increase_model_version_mock = mocker.patch.object(
        monitaur, "_increase_model_version"
    )

    result = monitaur.record_training(
        trained_model=trained_model,
        training_data=training_data,
        re_train=True,
        **record_training_data,
    )

    assert result is True
    increase_model_version_mock.assert_called_with(1)
    assert upload_fileobj_mock.call_count == 2

    filename = f"{record_training_data['model_set_id']}.joblib"
    filename_anchors = f"{record_training_data['model_set_id']}.anchors"
    os.remove(filename)
    os.remove(filename_anchors)


@pytest.mark.parametrize("version, expected_result", [("1.2", 1.3), (2, 2.1)])
def test_eval(version, expected_result):
    monitaur = Monitaur(auth_key="secret")

    assert monitaur._increase_model_version(version) == expected_result


def test_get_credentials_returns_credentials(mocker):
    monitaur = Monitaur(auth_key="secret")
    response = requests.Response()
    response.status_code = 200
    credentials = {
        "aws_access_key": "foo",
        "aws_secret_key": "bar",
        "aws_region": "us-east-1",
        "aws_bucket_name": "monitaur-demo",
    }
    mocker.patch.object(response, "json", return_value={"credentials": credentials})
    mocker.patch.object(monitaur._session, "get", return_value=response)

    results = monitaur.get_credentials(1)

    assert results == {
        "aws_access_key": "foo",
        "aws_bucket_name": "monitaur-demo",
        "aws_region": "us-east-1",
        "aws_secret_key": "bar",
    }


def test_get_credentials_raises_client_auth_error_given_unauthorized_response(mocker,):
    monitaur = Monitaur(auth_key="invalid")
    response = requests.Response()
    response.status_code = 401
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "get", return_value=response)

    with pytest.raises(ClientAuthError):
        monitaur.get_credentials(1)


def test_get_credentials_raises_client_validation_error_given_bad_request(mocker):
    monitaur = Monitaur(auth_key="secret")
    invalid_data = transaction_data.copy()
    invalid_data["features"] = "invalid features"
    response = requests.Response()
    response.status_code = 400
    mocker.patch.object(response, "json", return_value={})
    mocker.patch.object(monitaur._session, "get", return_value=response)

    with pytest.raises(ClientValidationError):
        monitaur.get_credentials("bad")
