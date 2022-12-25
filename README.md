This repo is for aws studygroup

It is based on 

   https://towardsaws.com/build-push-docker-image-to-aws-ecr-using-github-actions-8396888a8f9e

Overall goal is to push an image into ECR when a commit to "production" branch is made in github

## Features:

	- Milestone 0:  Can duplicate the source article - put something in ECR via github actions
	- Milestone 1:  Restrict commit to branch "production"
	- Milestone 2:  Can print out the git coimmit hash 
	- Milestone 3: 	print out configuration info from aws system manager parameter store, and a secret from AWS secrets manager
