try:
    from mypy_boto3.boto3_session_gen import Session
except ImportError:
    Session = object
