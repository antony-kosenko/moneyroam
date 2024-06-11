
import boto3
from botocore.exceptions import ClientError


def clear_none_values(parameters: dict) -> dict:
    """ Takes Dict as parameter and returns the same type of iterable filtering out None values. """
    # removing keys with values equal to 'None'
    not_none_variables_list = {key: value for key, value in parameters.items() if value is not None}
    return not_none_variables_list

def get_django_token():
    """ Pulls a project token from AWS secrets. """
    secret_name = "django/key"
    region_name = "eu-north-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return secret