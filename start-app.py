import os

import botocore.errorfactory

from aws_secret import get_secret    


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

print(f"yippee {commit} / {secret}")

