# -*- coding: utf-8 -*-
import re
from . import pushService_pb2
from .grpc_client import PushServiceGRPCClient, PushServiceException

__all__ = ["init_service", "send_sms_register_code", "send_sms_login_code", "send_sms_change_password_code",
           "send_email_register_code", "send_email_login_code", "send_email_change_password_code"]
_push_service_grpc_client: PushServiceGRPCClient

_phone_number_reg = re.compile(r"^1\d{10}$")
_email_reg = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def _verify_phone_numbers(phone_numbers: str) -> bool:
    return bool(_phone_number_reg.match(phone_numbers))


def _verify_email(email: str) -> bool:
    return bool(_email_reg.match(email))


def init_service(endpoint: str, source: str) -> None:
    global _push_service_grpc_client
    assert type(endpoint) == str, "endpoint must be a str"
    assert type(source) == str, "source must be a str"
    _push_service_grpc_client = PushServiceGRPCClient(endpoint=endpoint, source=source)


def send_sms_register_code(phone_numbers: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(phone_numbers) == str, "phone_numbers must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_phone_numbers(phone_numbers), "illegal phone number"
    _push_service_grpc_client.send_sms(phone_numbers, pushService_pb2.SMSMessageType.SMS_MESSAGE_TYPE_REGISTER_CODE,
                                       {"code": code})


def send_sms_login_code(phone_numbers: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(phone_numbers) == str, "phone_numbers must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_phone_numbers(phone_numbers), "illegal phone number"
    _push_service_grpc_client.send_sms(phone_numbers, pushService_pb2.SMSMessageType.SMS_MESSAGE_TYPE_LOGIN_CODE,
                                       {"code": code})


def send_sms_change_password_code(phone_numbers: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(phone_numbers) == str, "phone_numbers must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_phone_numbers(phone_numbers), "illegal phone number"
    _push_service_grpc_client.send_sms(phone_numbers,
                                       pushService_pb2.SMSMessageType.SMS_MESSAGE_TYPE_CHANGE_PASSWORD_CODE,
                                       {"code": code})


def send_sms_general_verification_code(phone_numbers: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(phone_numbers) == str, "phone_numbers must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_phone_numbers(phone_numbers), "illegal phone number"
    _push_service_grpc_client.send_sms(phone_numbers,
                                       pushService_pb2.SMSMessageType.SMS_MESSAGE_TYPE_GENERAL_VERIFICATION_CODE,
                                       {"code": code})


def send_email_register_code(email: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(email) == str, "email must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_email(email), "illegal email"
    _push_service_grpc_client.send_email(email, pushService_pb2.EmailMessageType.EMAIL_MESSAGE_TYPE_REGISTER_CODE,
                                         {"code": code, "email": email})


def send_email_login_code(email: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(email) == str, "email must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_email(email), "illegal email"
    _push_service_grpc_client.send_email(email, pushService_pb2.EmailMessageType.EMAIL_MESSAGE_TYPE_LOGIN_CODE,
                                         {"code": code, "email": email})


def send_email_change_password_code(email: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(email) == str, "email must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_email(email), "illegal email"
    _push_service_grpc_client.send_email(email,
                                         pushService_pb2.EmailMessageType.EMAIL_MESSAGE_TYPE_CHANGE_PASSWORD_CODE,
                                         {"code": code, "email": email})


def send_email_general_verification_code(email: str = "", code: str = "") -> None:
    global _push_service_grpc_client
    assert _push_service_grpc_client is not None, "push service sdk must be init first"
    assert type(email) == str, "email must be a str"
    assert type(code) == str, "code must be a str"
    assert _verify_email(email), "illegal email"
    _push_service_grpc_client.send_email(email,
                                         pushService_pb2.EmailMessageType.EMAIL_MESSAGE_TYPE_GENERAL_VERIFICATION_CODE,
                                         {"code": code, "email": email})
