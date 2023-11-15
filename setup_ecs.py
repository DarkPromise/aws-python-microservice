"""Setup for AWS ECS

This file contains the python code to setup AWS ECS cluster and task definition

TODO IMPORTANT:
Implement
Convert this to a AWS Cloudformation template
"""

import boto3
from dotenv import load_dotenv

# Import environment variables from .env
load_dotenv()


def create_cluster():
    pass


def create_task_definition():
    pass


if __name__ == "__main__":
    # Create the cluster
    create_cluster()

    # Create the task definition
    create_task_definition()
