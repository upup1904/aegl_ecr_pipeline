import os

try:
    commit = os.environ["GIT_COMMIT"]
except KeyError:
    print("there is not GIT_COMMIT DAMMIT")
    commit = "unset"
    

print(f"yippee {commit}")
