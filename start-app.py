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




import boto3

s3 = boto3.resource('s3',   region_name='us-east-1')

logme = "holy baloney it is thursday"
blobname = f"log_{datetime.now().strftime('%d%H%M%S.%f')}.txt"
s3.Object('cattoast-logs', blobname).put(Body=logme)








