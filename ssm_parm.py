"""function to get a parameter's value from AWS SSM"""
import boto3
from botocore.exceptions import ClientError


def get_param(param_name, region_name="us-east-1"):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='ssm',
        region_name=region_name
    )

    try:
        param_dict = client.get_parameter(Name=param_name, WithDecryption=True)
        return param_dict["Parameter"]["Value"]

    except Exception as e:
        print(f"got exception {e}")
