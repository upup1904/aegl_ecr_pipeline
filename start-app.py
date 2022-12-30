from datetime import datetime
import os

import boto3
import botocore.errorfactory

from aws_secret import get_secret
from ssm_parm import get_param


try:
    commit = os.environ["GIT_COMMIT"]
except KeyError:
    print("there is not GIT_COMMIT DAMMIT")
    commit = "unset"


secret = "no secrets"

try:
    aegl_port = get_param("aegl_port")
    aegl_port_secret = get_param("aegl_port_secret")
except Exception as e:
    print(f"There was an exception {e}")

print(f"yippee {commit} / {secret}")
print(f"port: {aegl_port}; secret port {aegl_port_secret}")


import boto3

s3 = boto3.resource('s3',   region_name='us-east-1')

logme = f"port: {aegl_port}; secret port {aegl_port_secret} at {datetime.now().strftime('%d%H%M%S.%f')}"
blobname = f"log_{datetime.now().strftime('%d%H%M%S.%f')}.txt"
s3.Object('cattoast-logs', blobname).put(Body=logme)


x





