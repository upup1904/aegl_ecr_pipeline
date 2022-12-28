This repo is for aws study group.

It is based on [this tutorial.](https://towardsaws.com/build-push-docker-image-to-aws-ecr-using-github-actions-8396888a8f9e)

The overall goal is to push an image into ECR when a commit to "production" branch is made in GitHub.



## Features:

	- Milestone 0:  Can duplicate the source article - put something in ECR via github actions
		done, tagged MS0
	- Milestone 1:  Restrict commit to branch "production"
		done, tagged MS1
	- Milestone 2:  Can print out the git commit hash 
	    to run this from AWS Command line
		sudo amazon-linux-extras install docker 
		sudo service docker start
	    sudo usermod -aG docker ec2-user
		sudo systemctl enable docker
	    You have to loging to docker -- configure aws:
		aws configure
		aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 948074422901.dkr.ecr.us-east-1.amazonaws.com
		(this gives a warning about stored password)
		docker run 948074422901.dkr.ecr.us-east-1.amazonaws.com/aegl_poc_xmas:current
	    (that tag comes from IMAGE_TAG in deploy.yml that was run from github
		After all that, you can see the output

	- Milestone 3: 	print out configuration info from aws system manager parameter store, and a secret from AWS secrets manager
	  # to get secrets, you can add managed policy SecretsManagerReadWrite
	  # for parms there is no managed policy.  Create a user managed policy  allowing
	           "ssm:DescribeParameters",
                "ssm:GetParametersByPath",
                "ssm:GetParameters",
                "ssm:GetParameter"
	# and attach it to the role
	- Milestone 4:  Cut back ecr_deployer permissions to minimum needed.
	  #create a cloud trail that will capture events used by the service 
	  In Console, IAM, User, Choose to generate a policy.  It will make you 
	  Choose "Generate policy based on CloudTrail events".   You'll have to fill in details about region, account, and container you want the ECR grants to apply to

## Followups?
	- How to use "environment" in github actions
	- what is IMAGE_TAG for in "Build, tag, and push" -- Answered, it's the docker image tag, like "latest"
	- How to run the single job in Fargate as a "batch"
	
	
