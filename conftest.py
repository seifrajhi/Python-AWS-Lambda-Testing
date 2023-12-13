import pytest
import os
from moto import mock_s3

@pytest.fixture(scope='function')
def aws_credentials():
    # Mocked AWS Credentials for Moto
    os.environ['AWS_ACCESS_KEY_ID'] = 'fake-access-key'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'fake-secret-key'
    os.environ['AWS_SECURITY_TOKEN'] = 'fake-security-token'
    os.environ['AWS_SESSION_TOKEN'] = 'fake-session-token'

@pytest.fixture(scope='function')
def s3_mock(aws_credentials):
    with mock_s3():
        yield boto3.client('s3')
