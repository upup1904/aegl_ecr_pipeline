import os

import botocore.errorfactory

from aws_secret import get_secret
from ssm_parm import get_param


try:
    commit = os.environ["GIT_COMMIT"]
except KeyError:
    print("there is not GIT_COMMIT DAMMIT")
    commit = "unset"

try:
    secret = get_secret("xmas_shhh")
except botocore.errorfactory.ClientError as ce:
    print(ce)
    secret = "not found"

try:
    aegl_port = get_param("aegl_port")
    aegl_port_secret = get_param("aegl_port_secret")
except Exception as e:
    print(f"There was an exception {e}")

print(f"yippee {commit} / {secret}")
print(f"port: {aegl_port}; secret port {aegl_port_secret}")


